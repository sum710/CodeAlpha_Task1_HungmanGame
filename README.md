🕹️ Hangman Game – CodeAlpha Internship Task 1

👩‍💻 Created by: Sumbal Murtaza

📌 Task Overview

This repository contains a text-based Hangman Game, developed as Task 1 for the CodeAlpha Internship program.

🎯 Goal
Build a simple console-based Hangman game where the player guesses a hidden word, one letter at a time, with a limited number of incorrect attempts.

🧠 Concepts Used
random module

while loop

if-else conditions

String and list manipulations

Basic console input/output

📋 Features
A fixed list of 5 predefined words (randomly selected each round)

Maximum of 6 incorrect guesses

Real-time display of:

Correctly guessed letters in their positions

Remaining incorrect guesses

Already guessed letters

Game ends with a win or loss message

🔧 How to Run
Make sure you have Python 3 installed.

Clone this repository or download the .py file.

Open your terminal or command prompt.

Navigate to the folder containing the code.

Run the script:

bash
Copy
Edit
python hangman.py
📁 File Structure
bash
Copy
Edit
hangman-game/
├── Hangmangame.py        # Main Python script
└── README.md         # Project documentation (this file)
📝 Example Gameplay
yaml
Copy
Edit
Welcome to Hangman!

Word: _ _ _ _ _
Incorrect guesses left: 6
Guessed letters: []

Enter a letter: a
Good guess!

Word: _ a _ _ _
Incorrect guesses left: 6
Guessed letters: [a]
...
📌 Notes
This project is part of CodeAlpha Internship Task 1.

No external libraries are used.

The focus is on logic building and core Python fundamentals.

