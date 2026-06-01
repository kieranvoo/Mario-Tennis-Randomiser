Mario Tennis Fever Randomiser 🎾

A simple Python mini application that randomly assigns Mario Tennis Fever characters and Fever Rackets to players.

This project includes both a terminal interface and Streamlit web interfaces.

Project Structure
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
│   └── player.py
│
├── services/
│   ├── csv_loader.py
│   └── randomiser.py
│
└── README.md
Features
Choose between 1v1 and 2v2
Select the number of human players
Auto-fills remaining slots as CPU players
Randomly assigns each player:
A character
A Fever Racket
Supports both terminal and Streamlit interfaces
Uses CSV files for the character and racket database
Requirements

Make sure Python is installed.

This project was built using:

Python 3.11

For the Streamlit versions, install Streamlit first:

pip install streamlit
How to Run the Terminal Version

Use this if you want to run the simple console interface.

python basic_app.py

This version will run directly in the terminal.

How to Run the Streamlit Version

Use this if you want to open the app in a browser interface.

python -m streamlit run app.py

After running the command, Streamlit will provide a local link such as:

http://localhost:8501

Open the link in your browser.

How to Run the Updated Streamlit Version

Use this if you want to run the newer or improved Streamlit interface.

python -m streamlit run new_app.py

This version also opens in your browser through a local Streamlit link.

Notes

The app reads character and racket data from:

data/characters.csv
data/rackets.csv

Make sure these CSV files remain inside the data folder. If they are moved or renamed, the app may not be able to load the data.

Suggested Usage

For the simplest experience:

python basic_app.py

For the nicer interface:

python -m streamlit run new_app.py