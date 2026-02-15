# 🎮 Hangman Game

A classic word-guessing game built with Pygame featuring a clean GUI, smooth animations, and progressive hangman drawings.

## 📸 Features

- **Interactive GUI**: Clean, user-friendly interface with custom buttons
- **Visual Feedback**: Progressive hangman drawings for each wrong guess
- **Word Bank**: Loads random words from an external word list
- **Smooth Animations**: Polished transitions between game states
- **Win/Loss Detection**: Automatic game-over detection with result display
- **Custom Styling**: Elegant fonts and color scheme

## 🎯 How to Play

1. Launch the game to see the welcome screen
2. Click the **Start** button to begin
3. Guess letters by pressing keys on your keyboard
4. Try to complete the word before the hangman is fully drawn
5. You have **6 wrong guesses** before losing
6. Click the **End** button to quit at any time

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Pygame library

### Installation

1. **Install Pygame**:
```bash
pip install pygame
```

2. **Clone or download the game files**

3. **Set up the required files** (see Project Structure below)

### Running the Game

```bash
python hangman.py
```

## 📁 Project Structure

```
Hangman/
├── hangman.py                    # Main game file
├── hangman_words.txt             # Word list (one word per line)
├── 0.jpg                         # Hangman image (0 wrong guesses)
├── 1.jpg                         # Hangman image (1 wrong guess)
├── 2.jpg                         # Hangman image (2 wrong guesses)
├── 3.jpg                         # Hangman image (3 wrong guesses)
├── 4.jpg                         # Hangman image (4 wrong guesses)
├── 5.jpg                         # Hangman image (5 wrong guesses)
├── 6.jpg                         # Hangman image (6 wrong guesses - complete)
├── 5360348.png                   # Start button image
└── image-removebg-preview.png    # End button image
```

### Required Files

#### 1. Word List (`hangman_words.txt`)
Create a text file with one word per line:
```
python
javascript
programming
computer
algorithm
developer
```

#### 2. Hangman Images (`0.jpg` through `6.jpg`)
- Seven images showing progressive stages of the hangman drawing
- `0.jpg`: Empty gallows
- `1.jpg` through `5.jpg`: Progressive body parts
- `6.jpg`: Complete hangman (game over)

#### 3. Button Images
- `5360348.png`: Start button graphic
- `image-removebg-preview.png`: End button graphic

**Note**: Update the file paths in `hangman.py` to match your directory structure.

## ⚙️ Configuration

### File Paths
Update these lines in the code to match your setup:

```python
# Line 10: Word list path
with open('path/to/your/hangman_words.txt', 'r') as f:

# Lines 20-26: Button images
start_btn_image = pygame.image.load("path/to/start_button.png")
end_btn_image = pygame.image.load("path/to/end_button.png")

# Lines 27-33: Hangman progression images
img0 = pygame.image.load("path/to/0.jpg")
# ... and so on for img1 through img6
```

### Display Settings
Customize the game window and colors:

```python
WIDTH = 800          # Window width
HEIGHT = 600         # Window height
BG_COLOR = (238, 240, 204)  # Background color (RGB)
```

### Fonts
The game uses system fonts:
- **Title**: Apple Chancery (80pt)
- **Word Display**: Bradley Hand (50pt)

You can change these in lines 16-17:
```python
title_font = pygame.font.SysFont("Your Font", 80)
word_font = pygame.font.SysFont("Your Font", 50)
```

## 🎨 Game States

| State | Description |
|-------|-------------|
| **Intro** | Welcome screen with title and start button |
| **Main** | Active gameplay with word display and hangman drawing |
| **Game Over** | Results screen showing win/loss and the correct word |

## 🕹️ Controls

| Input | Action |
|-------|--------|
| **A-Z Keys** | Guess a letter |
| **Start Button** | Begin new game |
| **End Button** | Quit current game |
| **Close Window** | Exit application |

## 🏆 Winning and Losing

### You Win When:
- All letters in the word are guessed correctly
- Message displays: "You Guessed Correctly!"

### You Lose When:
- You make 6 incorrect guesses
- The hangman drawing is complete
- Message displays: "You Lost!" with the correct word revealed

## 🛠️ Technical Details

### Key Classes

**`Button`**: Custom button class with hover effects
- Handles mouse collision detection
- Changes cursor on hover
- Manages click events

### Game Flow

1. **Initialization**: Load assets, select random word
2. **Intro Screen**: Display title and wait for start
3. **Main Game Loop**:
   - Accept letter inputs
   - Check if letter is in word
   - Update display or increment wrong guesses
   - Check win/loss conditions
4. **Game Over**: Display results and exit

### Features Implementation

- **Letter Tracking**: Each letter can only be guessed once
- **Input Validation**: Only accepts lowercase letters a-z
- **Visual Feedback**: Immediate display updates for each guess
- **Smooth Transitions**: 750ms delay between screens

## 🐛 Troubleshooting

### Common Issues

**"FileNotFoundError"**
- Ensure all image and text files exist in the correct locations
- Update file paths in the code to match your directory structure

**"pygame.error: Couldn't open file"**
- Check that image files are in supported formats (.png, .jpg)
- Verify file names match exactly (case-sensitive)

**Font not found**
- If system fonts aren't available, use `pygame.font.Font(None, size)` for default font

**Game window doesn't appear**
- Make sure Pygame is properly installed: `pip install --upgrade pygame`

## 💡 Future Enhancements

- [ ] Add difficulty levels (word length selection)
- [ ] Implement high score tracking
- [ ] Add sound effects and background music
- [ ] Include hint system
- [ ] Multi-player mode
- [ ] Word categories selection
- [ ] Replay button without restarting program

## 🤝 Contributing

Feel free to fork this project and submit pull requests with improvements!

### Ideas for Contribution
- Better graphics and animations
- Additional word lists by category
- Scoring system
- Difficulty settings
- Internationalization support

## 📄 License

This project is open source and available for personal and educational use.

---