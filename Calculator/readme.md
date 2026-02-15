# 🧮 Terminal Calculator

A simple, interactive command-line calculator with a typewriter effect for a retro computing experience.

## ✨ Features

- **Basic Operations**: Addition, subtraction, multiplication, and division
- **Typewriter Effect**: Smooth character-by-character text animation
- **Division by Zero Handling**: Safely returns "undefined" for invalid divisions
- **Clean Interface**: Auto-clearing terminal for a focused experience
- **Continuous Mode**: Solve multiple problems without restarting

## 🚀 Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone or download the calculator script
2. Navigate to the directory containing the file

### Usage

Run the calculator:

```bash
python calculator.py
```

## 📝 How to Use

1. Enter your mathematical expression when prompted
2. **Important**: Don't include spaces in your expression
3. Type `STOP` to exit the program

### Input Format

```
Valid:   12+5
Valid:   100-25
Valid:   7*8
Valid:   50/2

Invalid: 12 + 5  (contains spaces)
Invalid: 12 +5   (contains spaces)
```

## 💡 Examples

```
: 15+25
 15+25  =  40.0

: 100/4
 100/4  =  25.0

: 8*7
 8*7  =  56.0

: 10/0
 10/0  =  undefined

: STOP
Ending Program...
```

## 🛠️ Technical Details

### Supported Operations

| Operator | Operation      | Example |
|----------|---------------|---------|
| `+`      | Addition      | 5+3 = 8 |
| `-`      | Subtraction   | 9-4 = 5 |
| `*`      | Multiplication| 6*7 = 42|
| `/`      | Division      | 20/5 = 4|

### Key Functions

- `add(x, y)` - Returns sum of two numbers
- `subtract(x, y)` - Returns difference of two numbers
- `multiply(x, y)` - Returns product of two numbers
- `divide(x, y)` - Returns quotient, handles division by zero
- `find_operator(operation)` - Identifies the operator in the expression
- `typewrite(string)` - Creates typewriter effect for text output

## ⚠️ Limitations

- Only supports single operations per input (no complex expressions like `2+3*4`)
- Spaces in expressions will cause invalid input errors
- Works with integers and decimals

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements!

## 📄 License

This project is open source and available for personal and educational use.

---