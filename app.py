import streamlit as st

from models.player import Player
from services.csv_loader import CSVLoader
from services.randomiser import Randomiser


st.set_page_config(
    page_title="Mario Tennis Fever Randomiser",
    page_icon="🎾",
    layout="centered"
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


def show_player_inputs(mode, total_players, number_of_humans):
    st.subheader("Player Setup")

    if mode == "2v2":
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Team 1")

            for player_number in range(1, 3):
                if player_number <= number_of_humans:
                    st.text_input(
                        f"P{player_number} Name",
                        key=f"player_{player_number}_name"
                    )
                else:
                    cpu_number = player_number - number_of_humans
                    st.text_input(
                        f"P{player_number}",
                        value=f"CPU {cpu_number}",
                        disabled=True
                    )

        with col2:
            st.markdown("### Team 2")

            for player_number in range(3, 5):
                if player_number <= number_of_humans:
                    st.text_input(
                        f"P{player_number} Name",
                        key=f"player_{player_number}_name"
                    )
                else:
                    cpu_number = player_number - number_of_humans
                    st.text_input(
                        f"P{player_number}",
                        value=f"CPU {cpu_number}",
                        disabled=True
                    )

    else:
        for player_number in range(1, total_players + 1):
            if player_number <= number_of_humans:
                st.text_input(
                    f"P{player_number} Name",
                    key=f"player_{player_number}_name"
                )
            else:
                cpu_number = player_number - number_of_humans
                st.text_input(
                    f"P{player_number}",
                    value=f"CPU {cpu_number}",
                    disabled=True
                )


def show_results(mode, players):
    st.subheader("Randomised Results")

    if mode == "1v1":
        for player in players:
            with st.container(border=True):
                st.markdown(f"### {player.label}")
                st.write(f"**Character:** {player.character}")
                st.write(f"**Fever Racket:** {player.racket}")

    elif mode == "2v2":
        team_1 = players[:2]
        team_2 = players[2:]

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("## Team 1")

            for player in team_1:
                with st.container(border=True):
                    st.markdown(f"### {player.label}")
                    st.write(f"**Character:** {player.character}")
                    st.write(f"**Fever Racket:** {player.racket}")

        with col2:
            st.markdown("## Team 2")

            for player in team_2:
                with st.container(border=True):
                    st.markdown(f"### {player.label}")
                    st.write(f"**Character:** {player.character}")
                    st.write(f"**Fever Racket:** {player.racket}")


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

    st.subheader("Game Setup")

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

    show_player_inputs(mode, total_players, number_of_humans)

    if st.button("Randomise 🎲", use_container_width=True):
        players = create_players(mode, total_players, number_of_humans)
        randomiser.assign(players, characters, rackets)
        st.session_state["players"] = players
        st.session_state["mode"] = mode

    if "players" in st.session_state:
        show_results(st.session_state["mode"], st.session_state["players"])


if __name__ == "__main__":
    main()