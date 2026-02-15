# 🏓 Ping Pong Game

A classic two-player Pong game built with Pygame featuring smooth gameplay, score tracking, and a clean minimalist design.

## 🎮 Features

- **Two-Player Local Multiplayer**: Play against a friend on the same keyboard
- **Score Tracking**: First player to 5 points wins
- **Smooth Animations**: 120 FPS gameplay for responsive controls
- **Ball Reset Delay**: 1-second pause after each point
- **Random Ball Angles**: Unpredictable vertical trajectories keep the game exciting
- **Clean UI**: Minimalist black and white design with centered scoreboard
- **Start Screen**: Welcome screen with clickable start button

## 🎯 How to Play

1. Launch the game to see the start screen
2. Click the **START** button to begin
3. Player 1 (left side) uses **W** and **S** keys to move up and down
4. Player 2 (right side) uses **UP** and **DOWN** arrow keys
5. Hit the ball back and forth - don't let it pass your paddle!
6. First player to score **5 points** wins
7. Winner is displayed at the end of the game

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Pygame library

### Installation

1. **Install Pygame**:
```bash
pip install pygame
```

2. **Download the game file**

3. **Run the game**

### Running the Game

```bash
python pong.py
```

## 🕹️ Controls

### Player 1 (Left Paddle)
| Key | Action |
|-----|--------|
| **W** | Move paddle up |
| **S** | Move paddle down |

### Player 2 (Right Paddle)
| Key | Action |
|-----|--------|
| **↑ (Up Arrow)** | Move paddle up |
| **↓ (Down Arrow)** | Move paddle down |

### General Controls
| Action | Control |
|--------|---------|
| **Start Game** | Click START button |
| **Close Game** | Click window close button |

## 🎨 Game Elements

### Display Settings
- **Window Size**: 800x600 pixels
- **Frame Rate**: 120 FPS for smooth gameplay
- **Color Scheme**: Black background with white elements

### Paddles
- **Size**: 10 pixels wide, 80 pixels tall
- **Speed**: 5 pixels per frame
- **Position**: 10 pixels from screen edges

### Ball
- **Radius**: 10 pixels
- **Initial Speed**: 4 pixels/frame horizontally, 3 pixels/frame vertically
- **Behavior**: Bounces off top/bottom walls and paddles
- **Reset Delay**: 1000ms (1 second) after each point

## 🏆 Winning the Game

- **Victory Condition**: First player to reach **5 points**
- **Scoring**: 
  - Player 1 scores when the ball passes Player 2's paddle (right side)
  - Player 2 scores when the ball passes Player 1's paddle (left side)
- **Game Over**: Winner is displayed for 2 seconds before the game closes

## ⚙️ Configuration

### Adjust Game Speed

Change paddle speed (lines 21 and 25):
```python
player1_speed = 5  # Increase for faster movement
player2_speed = 5
```

Change ball speed (lines 33-34):
```python
ball_speed_x = 4  # Horizontal speed
ball_speed_y = 3  # Vertical speed
```

### Change Winning Score

Modify the victory condition (line 92):
```python
if player1_score == 5 or player2_score == 5:  # Change 5 to desired score
```

### Adjust Paddle Size

Change paddle dimensions (lines 18 and 23):
```python
player1_size = 80  # Paddle height in pixels
player2_size = 80
```

### Modify Ball Reset Delay

Change the delay after scoring (line 36):
```python
ball_delay = 1000  # Time in milliseconds (1000 = 1 second)
```

### Window Size

Adjust display dimensions (line 6):
```python
WIDTH, HEIGHT = 800, 600  # Width x Height in pixels
```

### Font Style

Change the font (line 15):
```python
font = pygame.font.SysFont("Chalkboard SE", 50)
# Replace with any system font and size
```

## 🛠️ Technical Details

### Game States

| State | Description |
|-------|-------------|
| **Intro** | Start screen with title and button |
| **Play** | Active gameplay with ball and paddles |
| **Game Over** | Winner announcement screen |

### Collision Detection

- **Ball-Paddle**: Uses `pygame.Rect.colliderect()` for precise collision detection
- **Ball-Wall**: Checks ball position against screen boundaries
- **Paddle Bounds**: Prevents paddles from moving off-screen

### Ball Physics

- Ball bounces off top and bottom walls by reversing vertical velocity
- Ball bounces off paddles by reversing horizontal velocity
- Ball resets to center after scoring with random vertical angle
- Vertical speed randomized between -3 and 3 after each reset

### Score Management

- Scores tracked independently for each player
- Score displayed at top center of screen
- Game ends when either player reaches 5 points

## 🎨 Visual Elements

### Start Screen
- Title: "Ping Pong" centered at top
- Interactive START button with hover effect
- Button highlights on mouse hover

### Game Screen
- Dashed center line dividing the court
- Score display above center line
- White paddles and ball on black background

### End Screen
- Winner announcement: "Winner is Player X"
- Displays for 2 seconds before closing

## 🐛 Troubleshooting

### "No module named 'pygame'"
```bash
pip install pygame
```

### Game runs too fast/slow
- Adjust the `clock.tick(120)` value (line 167)
- Lower numbers = slower game, higher numbers = faster game

### Paddle moves too fast/slow
- Modify `player1_speed` and `player2_speed` values
- Higher values = faster paddle movement

### Ball is too fast/unpredictable
- Reduce `ball_speed_x` and `ball_speed_y` values
- Adjust random range in lines 124 and 131: `random.randrange(-3, 3)`

### Font not displaying correctly
- Change to a different system font or use default:
```python
font = pygame.font.Font(None, 50)  # Uses pygame default font
```

## 💡 Gameplay Tips

- **Positioning**: Keep your paddle centered to cover more court area
- **Anticipation**: Watch the ball's angle to predict where it will go
- **Edge Hits**: Hitting the ball with the edge of your paddle can change angles
- **Defense First**: Focus on returning the ball rather than trick shots

## 🔮 Future Enhancements

- [ ] Add sound effects for ball hits and scoring
- [ ] Implement AI opponent for single-player mode
- [ ] Add difficulty levels (faster ball, smaller paddles)
- [ ] Include power-ups (paddle size, ball speed changes)
- [ ] Add particle effects on ball collisions
- [ ] Implement replay/rematch option
- [ ] Add pause functionality
- [ ] Include background music
- [ ] Track statistics (longest rally, average speed)
- [ ] Add customizable themes and colors

## 🤝 Contributing

Feel free to fork this project and submit pull requests with improvements!

### Ideas for Contribution
- Single-player mode with AI
- Customizable controls
- Settings menu
- High score tracking
- Tournament mode (best of 3/5/7)
- Special effects and animations

## 📄 License

This project is open source and available for personal and educational use.

---