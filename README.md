# 🚀 Projects

A collection of Python projects ranging from simple command-line tools to interactive games and GUI applications.

## 📂 Project List

### 🧮 Terminal Calculator
A command-line calculator with typewriter effect for basic arithmetic operations.
- **Language**: Python
- **Features**: Addition, subtraction, multiplication, division, division by zero handling
- **Interface**: Terminal-based with animated text output

### 🎮 Hangman Game
Classic word-guessing game with visual feedback and custom graphics.
- **Language**: Python (Pygame)
- **Features**: Progressive hangman drawings, random word selection, GUI interface
- **Players**: Single-player

### 📷 Image Viewer
Recursive directory scanner that displays JPG images in a fullscreen slideshow.
- **Language**: Python (OpenCV, Pillow)
- **Features**: Auto-advance slideshow, recursive search, fullscreen display
- **Use Case**: Quick photo browsing, digital picture frame

### 🏓 Ping Pong
Two-player Pong game with score tracking and smooth gameplay.
- **Language**: Python (Pygame)
- **Features**: Local multiplayer, 120 FPS gameplay, collision detection
- **Players**: Two-player (same keyboard)

### 📝 Text Editor
Lightweight GUI text editor with file opening and auto-save functionality.
- **Language**: Python (Tkinter)
- **Features**: File browser, auto-save, save confirmation dialog
- **Use Case**: Quick text file editing

## 🛠️ Technologies Used

- **Python 3.x** - Core programming language
- **Pygame** - Game development (Hangman, Pong)
- **Tkinter** - GUI development (Text Editor)
- **OpenCV** - Image processing (Image Viewer)
- **Pillow** - Image handling (Image Viewer)

## 🚀 Getting Started

Each project has its own directory with a detailed README. To get started:

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/Projects.git
cd Projects
```

2. **Navigate to a project**:
```bash
cd Calculator  # or Hangman, ImageViewer, PingPong, TextEditor
```

3. **Read the project README** for specific installation and usage instructions

4. **Install dependencies** (if required):
```bash
pip install pygame  # For Hangman and Pong
pip install opencv-python pillow  # For Image Viewer
```

## 📋 Requirements

### All Projects
- Python 3.x

### Specific Projects
- **Hangman**: Pygame, image files, word list
- **Pong**: Pygame
- **Image Viewer**: OpenCV, Pillow
- **Text Editor**: Tkinter (usually pre-installed)
- **Calculator**: No external dependencies

## 🎯 Project Structure

```
Projects/
├── Calculator/
│   ├── calculator.py
│   └── README.md
├── Hangman/
│   ├── hangman.py
│   ├── hangman_words.txt
│   ├── *.jpg (hangman images)
│   ├── *.png (button images)
│   └── README.md
├── ImageViewer/
│   ├── image_viewer.py
│   └── README.md
├── PingPong/
│   ├── pong.py
│   └── README.md
├── TextEditor/
│   ├── text_editor.py
│   └── README.md
└── README.md (this file)
```

## 💡 Learning Outcomes

These projects demonstrate:
- **Basic Python Programming**: Variables, functions, control flow
- **GUI Development**: Tkinter and Pygame interfaces
- **Game Development**: Game loops, collision detection, state management
- **File I/O**: Reading and writing files
- **Image Processing**: Working with images using OpenCV and Pillow
- **Event Handling**: Keyboard and mouse input processing

## 🤝 Contributing

Feel free to fork this repository and submit pull requests with improvements or new projects!

## 📄 License

All projects are open source and available for personal and educational use.

---
