# Image Resizer Tool

A simple command-line utility written in Python to resize images to a specified resolution.

## Features

*   Resize any image supported by the Pillow library (e.g., JPEG, PNG, BMP).
*   Specify the exact width and height for the output image.
*   Command-line interface for easy integration into scripts or workflows.

## Prerequisites

You need to have **Python 3.6 or higher** installed on your system.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [YOUR_REPOSITORY_URL]
    cd image-resizer-tool
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

The tool is executed from the command line. You must provide the input file path, the desired output file path, and the new dimensions (width and height).

### Command Syntax

```bash
python resize_tool.py <INPUT_FILE> <OUTPUT_FILE> --width <WIDTH> --height <HEIGHT>
```

### Example

To resize an image named `original.jpg` to a resolution of 1920x1080 and save it as `resized.jpg`:

```bash
python resize_tool.py original.jpg resized.jpg --width 1920 --height 1080
```

### Example for Portrait Orientation

To resize an image to a portrait resolution of 1080x2400:

```bash
python resize_tool.py original.png phone_wallpaper.png --width 1080 --height 2400
```

## Dependencies

This tool relies on the following Python package:

| Package | Purpose |
| :--- | :--- |
| `Pillow` | Image processing functionality |

The exact version requirements are listed in `requirements.txt`.

## License

This project is licensed under the MIT License - see the LICENSE file for details (Note: A LICENSE file is not included in this initial setup, but is recommended for open-source projects).
