# 📷 Recursive Image Viewer

A simple Python tool that recursively searches through directories to find and display all JPG images in a fullscreen slideshow.

## ✨ Features

- **Recursive Directory Search**: Automatically finds all JPG images in a directory and its subdirectories
- **Fullscreen Slideshow**: Displays images in fullscreen mode for an immersive viewing experience
- **Auto-Advance**: Automatically switches to the next image every 2 seconds
- **Preserves Aspect Ratio**: Images maintain their original dimensions
- **Simple Interface**: Just provide a path and watch your photos

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- OpenCV (cv2)
- Pillow (PIL)

### Installation

1. **Install required libraries**:
```bash
pip install opencv-python pillow
```

2. **Download the script**

3. **Run the program**

### Usage

Run the image viewer:

```bash
python image_viewer.py
```

When prompted, enter the path to the directory you want to search:

```
Path: /Users/username/Pictures
```

The program will:
1. Search through all subdirectories
2. Find all `.jpg` files
3. Display them in fullscreen, one by one
4. Automatically advance every 2 seconds

## 📝 How It Works

### Workflow

1. **Input**: User provides a directory path
2. **Recursive Search**: Program walks through all subdirectories using `os.walk()`
3. **File Filtering**: Identifies all files with `.jpg` extension
4. **Display**: Opens each image in fullscreen mode
5. **Auto-Advance**: Shows each image for 2 seconds before moving to the next

### Example Directory Structure

```
Photos/
├── Vacation/
│   ├── beach.jpg     ✓ Found
│   ├── sunset.jpg    ✓ Found
│   └── notes.txt     ✗ Skipped
├── Family/
│   ├── reunion.jpg   ✓ Found
│   └── video.mp4     ✗ Skipped
└── portrait.jpg      ✓ Found
```

All 4 JPG files will be displayed in the slideshow.

## ⚙️ Configuration

### Change Display Duration

Modify the delay time (in milliseconds) in line 23:

```python
cv2.waitKey(2000)  # 2000ms = 2 seconds
```

Examples:
- `1000` = 1 second per image
- `5000` = 5 seconds per image
- `0` = Wait for keypress to advance

### Support Additional Image Formats

To include other image types, modify the file extension check:

```python
# Original (JPG only)
if split[1] == '.jpg':
    jpglist.append(i)

# Support multiple formats
if split[1].lower() in ['.jpg', '.jpeg', '.png', '.bmp', '.gif']:
    jpglist.append(i)
```

### Window Mode

To display in a resizable window instead of fullscreen, replace lines 20-21 with:

```python
cv2.namedWindow("Photos", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Photos", 1280, 720)
```

## 🕹️ Controls

While the slideshow is running:

| Key | Action |
|-----|--------|
| **Any Key** | Skip to next image (if waitKey is set to 0) |
| **ESC** | Force quit (may need to press multiple times) |
| **Q** | Quit (works if you modify code to check for key) |

### Adding Manual Control

To add keyboard controls, replace `cv2.waitKey(2000)` with:

```python
key = cv2.waitKey(2000) & 0xFF
if key == ord('q') or key == 27:  # 'q' or ESC to quit
    break
if key == ord('n'):  # 'n' for next
    continue
```

## 🛠️ Technical Details

### Key Functions

- **`os.walk(path)`**: Recursively traverses directory tree
- **`os.path.join()`**: Creates full file paths
- **`os.path.splitext()`**: Separates filename from extension
- **`Image.open()`**: Gets image dimensions using Pillow
- **`cv2.imread()`**: Loads image for display
- **`cv2.resize()`**: Ensures proper image sizing
- **`cv2.imshow()`**: Displays image in window

### Performance Notes

- Images are loaded one at a time (memory efficient)
- Original dimensions are preserved
- Works with large directory structures
- No caching (images reload each run)

## 📋 Supported Formats

Currently supports:
- ✅ `.jpg` files

Can be easily modified to support:
- `.jpeg`
- `.png`
- `.bmp`
- `.gif`
- `.tiff`

See Configuration section for instructions.

## 🐛 Troubleshooting

### "No module named 'cv2'"
```bash
pip install opencv-python
```

### "No module named 'PIL'"
```bash
pip install pillow
```

### "Invalid path" or no images found
- Ensure the path exists and is spelled correctly
- Check that there are actually `.jpg` files in the directory
- On Windows, use forward slashes or double backslashes: `C:/Users/...` or `C:\\Users\\...`

### Images display too quickly/slowly
- Modify the `cv2.waitKey(2000)` value to adjust timing
- Value is in milliseconds (1000 = 1 second)

### Window doesn't close properly
- Press ESC multiple times
- Use Task Manager/Activity Monitor to force close if needed
- Consider adding explicit quit key (see Controls section)

### Images appear stretched or distorted
- The script preserves original dimensions, but if issues occur, you can modify the resize logic
- Try removing the resize line entirely to use OpenCV's default sizing

## 💡 Use Cases

- **Quick Photo Review**: Browse through vacation photos without opening each file
- **Digital Picture Frame**: Set up an automated slideshow
- **Photo Organization**: Preview images before sorting or editing
- **Backup Verification**: Ensure all photos copied correctly
- **Client Presentations**: Quick portfolio review

## 🔮 Future Enhancements

- [ ] Add support for multiple image formats
- [ ] Implement shuffle/random order
- [ ] Add image metadata display (filename, dimensions, date)
- [ ] Include progress indicator (Image 5 of 100)
- [ ] Add pause/resume functionality
- [ ] Save favorite images to a list
- [ ] Add zoom and pan controls
- [ ] Include directory exclusion filters
- [ ] Create GUI for easier path selection
- [ ] Add transition effects between images

## 🤝 Contributing

Feel free to fork this project and submit pull requests with improvements!

### Ideas for Contribution
- Support for video files
- Image filtering options (by date, size, etc.)
- Recursive depth limiter
- Thumbnail preview mode
- Export selected images to new folder

## 📄 Example Usage

```bash
$ python image_viewer.py
Path: /Users/john/Documents/Photos

# Program finds and displays:
# - /Users/john/Documents/Photos/summer/beach.jpg
# - /Users/john/Documents/Photos/summer/vacation/sunset.jpg
# - /Users/john/Documents/Photos/family/reunion.jpg
# - /Users/john/Documents/Photos/portrait.jpg
# (Each displayed for 2 seconds in fullscreen)
```

## 📄 License

This project is open source and available for personal and educational use.

---