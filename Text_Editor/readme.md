# 📝 Simple Text Editor

A lightweight, user-friendly text editor built with Python's Tkinter featuring file opening, editing, and auto-save functionality.

## ✨ Features

- **File Browser**: Open any text file through a graphical file dialog
- **Text Editing**: Full-featured text box with word wrapping
- **Auto-Save**: Automatically saves changes to the opened file
- **Save Confirmation**: Prompts before closing to prevent data loss
- **Centered Windows**: All windows automatically center on screen
- **Clean Interface**: Minimalist design with Georgia font styling
- **Modal Dialogs**: Popup windows that require user response

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Tkinter (usually included with Python)

### Installation

1. **Verify Tkinter is installed**:
```bash
python -m tkinter
```
If a small window appears, Tkinter is installed. If not:

**macOS/Linux:**
```bash
sudo apt-get install python3-tk  # Ubuntu/Debian
```

**Windows:** Tkinter comes pre-installed with Python

2. **Download the script**

3. **Run the editor**

### Running the Text Editor

```bash
python text_editor.py
```

## 📝 How to Use

### Basic Workflow

1. **Launch the editor** - A 500x500 window appears with an empty text box
2. **Open a file** - Click "Open File" button and select a text file
3. **Edit the text** - Type, delete, and modify content freely
4. **Save and exit** - Click "Done" button
5. **Confirm save** - Choose "YES" to save changes or "NO" to discard

### Opening Files

1. Click the **"Open File"** button
2. Navigate to your desired file in the file dialog
3. Select a text file and click "Open"
4. File contents will appear in the text box

### Saving Files

- The editor **auto-saves** to the currently opened file
- No need to use "Save As" - changes write directly to the original file
- Click **"Done"** button when finished editing
- Confirm save by clicking **"YES"** in the popup

### Closing Without Saving

1. Click the **"Done"** button
2. In the confirmation popup, click **"NO"**
3. A message appears: "No Changes Made - Ending Program..."
4. Editor closes after 2 seconds

## 🎨 Interface Elements

### Main Window (500x500 pixels)
- **Title**: "Text Editor" at the top in large Georgia font
- **Text Box**: Large editable area with word wrapping (60 columns × 20 rows)
- **Open File Button**: Left button at bottom
- **Done Button**: Right button at bottom

### Confirmation Popup (350x200 pixels)
- Appears when clicking "Done"
- Question: "Do you want to save the file?"
- Two buttons: **YES** (saves and closes) and **NO** (closes without saving)

### No Changes Popup (250x150 pixels)
- Appears when clicking "NO" in confirmation
- Message: "No Changes Made - Ending Program..."
- Auto-closes after 2 seconds

## ⚙️ Configuration

### Change Font Style

Modify the font constant at the top (line 1):
```python
FONT = 'Georgia'  # Change to any system font
```

Common alternatives:
- `'Arial'`
- `'Times New Roman'`
- `'Courier New'`
- `'Helvetica'`

### Adjust Window Size

Modify main window dimensions (lines 58-59):
```python
win_width = 500   # Window width in pixels
win_height = 500  # Window height in pixels
```

### Change Text Box Size

Modify text box dimensions (line 72):
```python
text_box = tk.Text(root, wrap='word', width=60, height=20)
# width = characters per line
# height = number of visible lines
```

### Adjust Button Sizes

Modify button font sizes (lines 75 and 78):
```python
open_btn = tk.Button(root, text='Open File', command=showfile, font=(FONT, 25))
# Change 25 to desired size

submit_btn = tk.Button(root, text='Done', command=confirm, font=(FONT, 25), width=7)
# Adjust both font size and width
```

### Modify Auto-Close Timer

Change the "No Changes" popup duration (line 46):
```python
no_popup.after(2000, root.destroy)  # 2000ms = 2 seconds
```

## 🛠️ Technical Details

### Key Functions

**`showfile()`**
- Opens file dialog for file selection
- Reads file contents
- Clears text box and inserts file data
- Stores file path as text_box attribute

**`save()`**
- Checks if a file is currently open
- Writes text box contents to the file
- Overwrites original file with edits

**`center_popup(win, width, height)`**
- Calculates screen center position
- Centers popup windows on screen
- Works with any window size

**`confirm()`**
- Creates confirmation dialog
- Handles YES/NO user choice
- Manages save workflow

### Data Flow

1. **File Open** → Read file → Display in text box → Store file path
2. **User Edits** → Text box updates in real-time
3. **Click Done** → Confirmation popup appears
4. **Click YES** → Save function writes to file → Close editor
5. **Click NO** → Show "No Changes" message → Close editor

### Window Management

- **Modal dialogs**: Use `grab_set()` to prevent interaction with main window
- **Auto-centering**: All windows calculate screen dimensions for perfect centering
- **Timed closing**: Some popups close automatically after delays

## 📋 Supported File Types

The editor can open and edit any **plain text file**, including:
- `.txt` - Plain text files
- `.py` - Python scripts
- `.md` - Markdown files
- `.html` - HTML files
- `.css` - CSS files
- `.js` - JavaScript files
- `.json` - JSON data files
- `.csv` - CSV files
- `.log` - Log files

**Note**: Binary files (images, executables, etc.) will not display correctly.

## 🐛 Troubleshooting

### "No module named 'tkinter'"

**Python 3:**
```bash
sudo apt-get install python3-tk  # Linux
brew install python-tk@3.x       # macOS
```

**Windows:** Reinstall Python with Tkinter option checked

### File won't open

- Ensure the file is a text file (not binary)
- Check file permissions (must have read access)
- Verify file path is correct

### Changes not saving

- Make sure you opened a file first using "Open File" button
- Editor only saves to opened files, not new unsaved content
- Check file write permissions

### Window appears off-screen

- Check your screen resolution settings
- Modify window size in configuration if too large

### Text appears cut off

- Increase text box width/height in configuration
- Enable scroll bars (see Future Enhancements)

## ⚠️ Important Notes

### No "Save As" Feature
- The editor saves directly to the opened file
- Cannot create new files or save with different names
- Always overwrites the original file

### No New File Creation
- Must open an existing file to edit
- Cannot start with blank document and save as new file

### Auto-Overwrite
- Clicking "YES" in confirmation immediately overwrites the original file
- No undo after saving - changes are permanent

### Recommended Workflow
1. Make a backup of important files before editing
2. Open the file you want to edit
3. Make your changes
4. Save and close

## 💡 Use Cases

- **Quick Text Edits**: Make fast changes to configuration files
- **Code Snippets**: Edit small scripts and code files
- **Note Taking**: Simple note editing without distractions
- **Log File Review**: View and edit log files
- **Configuration Files**: Modify .txt config files
- **Learning Tool**: Study Python GUI programming with Tkinter

## 🔮 Future Enhancements

- [ ] Add "Save As" functionality for new files
- [ ] Implement "New File" option
- [ ] Add scrollbars to text box
- [ ] Include undo/redo functionality
- [ ] Add search and replace features
- [ ] Implement syntax highlighting for code files
- [ ] Add line numbers
- [ ] Include keyboard shortcuts (Ctrl+S, Ctrl+O)
- [ ] Add recent files menu
- [ ] Implement multiple tabs for editing multiple files
- [ ] Add font size controls
- [ ] Include word count display
- [ ] Add dark mode theme

## 🤝 Contributing

Feel free to fork this project and submit pull requests with improvements!

### Ideas for Contribution
- File encoding detection and support
- Drag-and-drop file opening
- Auto-backup before saving
- Customizable themes
- Plugin system
- Multi-file editing with tabs

## 📄 Example Usage

```bash
$ python text_editor.py

# Editor window opens
# Click "Open File"
# Select: /Users/john/notes.txt
# Edit the text
# Click "Done"
# Click "YES" to save
# Program closes
```

## 📄 License

This project is open source and available for personal and educational use.

---