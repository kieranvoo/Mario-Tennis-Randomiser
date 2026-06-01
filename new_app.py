import streamlit as st

from models.player import Player
from services.csv_loader import CSVLoader
from services.randomiser import Randomiser


st.set_page_config(
    page_title="Mario Tennis Fever Randomiser",
    page_icon="🎾",
    layout="wide"
)


def create_players(mode, total_players, number_of_humans):
    players = []
    cpu_count = 1

    for player_number in range(1, total_players + 1):
        if player_number <= number_of_humans:
            name = st.session_state.get(f"player_{player_number}_name", "").strip()

            if name == "":
                name = f"User {player_number}"

            is_human = True
        else:
            name = f"CPU {cpu_count}"
            cpu_count += 1
            is_human = False

        player = Player(
            player_number=player_number,
            name=name,
            is_human=is_human
        )

        players.append(player)

    return players


def show_player_input(player_number, number_of_humans):
    if player_number <= number_of_humans:
        st.text_input(
            f"P{player_number} Name",
            key=f"player_{player_number}_name",
            placeholder=f"Enter Player {player_number} name"
        )
    else:
        cpu_number = player_number - number_of_humans
        st.text_input(
            f"P{player_number}",
            value=f"CPU {cpu_number}",
            disabled=True
        )


def show_player_inputs(mode, total_players, number_of_humans):
    st.header("👥 Player Setup")

    if mode == "2v2":
        col1, col2 = st.columns(2)

        with col1:
            with st.container(border=True):
                st.subheader("🏆 Team 1")
                show_player_input(1, number_of_humans)
                show_player_input(2, number_of_humans)

        with col2:
            with st.container(border=True):
                st.subheader("⚔️ Team 2")
                show_player_input(3, number_of_humans)
                show_player_input(4, number_of_humans)

    else:
        col1, col2 = st.columns(2)

        with col1:
            with st.container(border=True):
                st.subheader("Player 1")
                show_player_input(1, number_of_humans)

        with col2:
            with st.container(border=True):
                st.subheader("Player 2")
                show_player_input(2, number_of_humans)


def show_player_card(player):
    with st.container(border=True):
        player_type = "👤 Human" if player.is_human else "🤖 CPU"

        st.markdown(f"### {player.label}")
        st.caption(player_type)
        st.write(f"🎾 **Character:** {player.character}")
        st.write(f"🔥 **Fever Racket:** {player.racket}")


def show_results(mode, players):
    st.header("🎲 Randomised Results")

    if mode == "1v1":
        col1, col2 = st.columns(2)

        with col1:
            show_player_card(players[0])

        with col2:
            show_player_card(players[1])

    elif mode == "2v2":
        team_1 = players[:2]
        team_2 = players[2:]

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🏆 Team 1")
            for player in team_1:
                show_player_card(player)

        with col2:
            st.subheader("⚔️ Team 2")
            for player in team_2:
                show_player_card(player)


def reset_results():
    if "players" in st.session_state:
        del st.session_state["players"]

    if "mode" in st.session_state:
        del st.session_state["mode"]


def main():
    st.title("🎾 Mario Tennis Fever Randomiser")
    st.write("Randomly assign characters and Fever Rackets for 1v1 or 2v2 matches.")

    loader = CSVLoader()
    randomiser = Randomiser()

    try:
        characters = loader.load("data/characters.csv")
        rackets = loader.load("data/rackets.csv")

    except FileNotFoundError as error:
        st.error(error)
        return

    except ValueError as error:
        st.error(error)
        return

    with st.sidebar:
        st.header("🎮 Game Setup")

        mode = st.selectbox(
            "Select game mode",
            ["1v1", "2v2"]
        )

        if mode == "1v1":
            total_players = 2
        else:
            total_players = 4

        number_of_humans = st.number_input(
            "How many human players?",
            min_value=0,
            max_value=total_players,
            value=total_players,
            step=1
        )

        st.divider()

        randomise_clicked = st.button(
            "Randomise 🎲",
            use_container_width=True
        )

        reset_clicked = st.button(
            "Reset Results",
            use_container_width=True
        )

        st.divider()

        st.caption(f"Characters loaded: {len(characters)}")
        st.caption(f"Rackets loaded: {len(rackets)}")

    if reset_clicked:
        reset_results()

    show_player_inputs(mode, total_players, number_of_humans)

    st.divider()

    if randomise_clicked:
        players = create_players(mode, total_players, number_of_humans)
        randomiser.assign(players, characters, rackets)

        st.session_state["players"] = players
        st.session_state["mode"] = mode

    if "players" in st.session_state:
        show_results(st.session_state["mode"], st.session_state["players"])
    else:
        st.info("Set up your players, then click Randomise in the sidebar.")


if __name__ == "__main__":
    main()