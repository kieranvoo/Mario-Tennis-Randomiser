# 🎾 Mario Tennis Fever Randomiser

A simple Python mini application that randomly assigns **Mario Tennis Fever characters** and **Fever Rackets** to players.

This project includes both a **terminal interface** and **Streamlit web interfaces**, allowing users to choose between a lightweight console experience or a cleaner browser-based layout.

---

## ✨ Features

* Choose between **1v1** and **2v2** game modes
* Select the number of human players
* Automatically fills remaining player slots as **CPU**
* Randomly assigns each player:

  * A Mario Tennis Fever character
  * A Fever Racket
* Supports both:

  * Terminal interface
  * Streamlit browser interface
* Uses CSV files as the character and racket database
* Structured with simple OOP principles using `models` and `services`

---

## 📁 Project Structure

```text
Mario Tennis/
│
├── basic_app.py        # Terminal version
├── app.py              # Streamlit version
├── new_app.py          # Updated Streamlit version
│
├── data/
│   ├── characters.csv  # Character database
│   └── rackets.csv     # Fever Racket database
│
├── models/
│   └── player.py       # Player class
│
├── services/
│   ├── csv_loader.py   # Loads CSV data
│   └── randomiser.py   # Handles random character/racket assignment
│
└── README.md
```

---

## 🧰 Requirements

Make sure Python is installed on your computer.

This project was built using:

```bash
Python 3.11
```

For the Streamlit versions, install Streamlit first:

```bash
pip install streamlit
```

---

## 🚀 How to Run

### 1. Terminal Version

Use this if you want to run the simple console interface.

```bash
python basic_app.py
```

This version runs directly in the terminal.

---

### 2. Streamlit Version

Use this if you want to open the app in a browser interface.

```bash
python -m streamlit run app.py
```

After running the command, Streamlit will provide a local link such as:

```text
http://localhost:8501
```

Open the link in your browser.

---

### 3. Updated Streamlit Version

Use this if you want to run the newer or improved Streamlit interface.

```bash
python -m streamlit run new_app.py
```

This version also opens in your browser through a local Streamlit link.

---

## 🎮 Suggested Usage

For the simplest experience:

```bash
python basic_app.py
```

For the nicer browser-based interface:

```bash
python -m streamlit run new_app.py
```

---

## 🗂️ Data Files

The app reads character and racket data from:

```text
data/characters.csv
data/rackets.csv
```

Make sure these CSV files remain inside the `data` folder.

If they are moved or renamed, the app may not be able to load the data correctly.

---

## 🧠 How It Works

The app follows a simple flow:

1. User selects the game mode: `1v1` or `2v2`
2. User selects the number of human players
3. Remaining slots are automatically assigned as CPU players
4. The app loads characters and rackets from CSV files
5. Each player is randomly assigned:

   * One character
   * One Fever Racket
6. Results are displayed based on the chosen interface

---

## 🏗️ Project Design

The project is organised using a simple OOP-style structure:

| Component      | Purpose                                     |
| -------------- | ------------------------------------------- |
| `Player`       | Represents each human or CPU player         |
| `CSVLoader`    | Loads characters and rackets from CSV files |
| `Randomiser`   | Assigns random characters and rackets       |
| `basic_app.py` | Runs the terminal interface                 |
| `app.py`       | Runs the first Streamlit interface          |
| `new_app.py`   | Runs the improved Streamlit interface       |

---

## 📌 Notes

* `localhost` links only work while the Streamlit app is running on your computer.
* If `streamlit run app.py` does not work, use:

```bash
python -m streamlit run app.py
```

* The updated interface is recommended for the best user experience:

```bash
python -m streamlit run new_app.py
```

---


