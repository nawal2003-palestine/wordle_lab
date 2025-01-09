
# 🎮 Wordle Game

Welcome to **Wordle**, a Python implementation of the popular word-guessing game. Players have 6 attempts to guess a secret 5-letter word. Feedback is provided after each guess with color-coded hints:

- 🟩 **GREEN**: Correct letter in the correct position.  
- 🟨 **YELLOW**: Correct letter in the wrong position.  
- 🟥 **RED**: Incorrect letter.

---

## ✨ Features  
- Validate player input to ensure valid guesses.  
- Provide detailed feedback for each attempt.  
- Display winning and losing messages.  
- Handles invalid inputs gracefully.  

---

## 🚀 How to Play  
1. Clone this repository:  
   ```bash
   git clone https://github.com/nawal2003-palestine/Wordle-game.git
   cd Wordle-game
   ```
2. Ensure you have Python 3 installed.  
3. Run the game:  
   ```bash
   python main.py
   ```
4. Follow the prompts to guess the secret word!  

---

## ⚙️ How it Works  
The game includes the following modules:  
1. **`word_choice.py`**:  
   - Reads all valid 5-letter words from a file (`words.txt`).  
   - Randomly selects the secret word.  
   
2. **`validate_guess.py`**:  
   - Validates player input to ensure guesses are 5-letter words.  
   - Ensures the word exists in the word list and hasn’t been guessed before.  

3. **`wordle.py`**:  
   - Checks if the guess matches the secret word.  
   - Generates feedback for each letter in the guess.  

4. **`display.py`**:  
   - Prints game instructions and feedback with color formatting.  
   - Displays win/lose messages.  



---

## 🗂️ File Structure  
```
.
├── main.py                     # Main game logic
├── wordle_package/             # Package containing game modules
│   ├── word_choice.py          # Handles word selection
│   ├── validate_guess.py       # Input validation
│   ├── wordle.py               # Core game mechanics
│   ├── display.py              # Handles display and feedback
│   ├── assets/
│   │   └── words.txt           # List of valid 5-letter words
└── README.md                   # Project documentation
```


---

## 🎮 Example Gameplay  
```
![Alt text](<img width="458" alt="1" src="https://github.com/user-attachments/assets/742dd0c8-103c-4ab5-b2ae-b48eca23aabd" />)
```

---

## 🤝 Contributions  
Contributions are welcome! To contribute:  
1. Fork this repository.  
2. Create a new branch:  
   ```bash
   git checkout -b feature-name
   ```  
3. Commit your changes and push:  
   ```bash
   git commit -m "Add feature-name"
   git push origin feature-name
   ```  
4. Open a Pull Request.  

---

## 📜 License  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  

---

## 🙌 Acknowledgements  
Inspired by the original **Wordle** game created by Josh Wardle. This implementation is for educational purposes only.  

