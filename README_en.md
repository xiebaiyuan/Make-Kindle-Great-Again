# Kindle Wallpaper Tool

![License](https://img.shields.io/github/license/xiebaiyuan/kindle-wallpaper-tool)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)

A tool to convert color images to grayscale wallpaper images suitable for Kindle devices.

## Features

- Convert color images to grayscale
- Smartly crop images to fit Kindle screen aspect ratios (avoiding image distortion)
- Supports all major Kindle models
- Does not modify original images
- Interactive specification of save path (default is ~/Downloads/KindleBG)
- Interactive Kindle model selection
- Output filenames include device model for easy identification

## Supported Kindle Models

### Basic Kindle:
- `kindle1` - Kindle 1 (600x800)
- `kindledx` - Kindle DX/DX Graphite (824x1200)
- `kindle234578` - Kindle 2/3/4/5/7/8/Touch (600x800)
- `kindle10` - Kindle 10 (600x800)
- `kindle11` - Kindle 11 (2022/2024) (1072x1448)

### Paperwhite Series:
- `pw12` - Kindle Paperwhite 1/2 (758x1024)
- `pw3` - Kindle Paperwhite 3/Voyage/Oasis 1 (1072x1448)
- `pw4` - Kindle Paperwhite 4 (default) (1072x1448)
- `pw5` - Kindle Paperwhite 5 (1236x1648)
- `pw6` - Kindle Paperwhite 6 (1236x1648)

### Oasis Series:
- `oasis1` - Kindle Oasis 1 (1072x1448)
- `oasis2` - Kindle Oasis 2 (1264x1680)
- `oasis3` - Kindle Oasis 3 (1264x1680)

### Special Models:
- `scribe` - Kindle Scribe (1860x2480)
- `colorsoft` - Kindle Colorsoft (1264x1680)

### Generic Sizes:
- `cover` - Cover Image (600x800)

## Installation

### Clone the Repository

```bash
git clone https://github.com/xiebaiyuan/kindle-wallpaper-tool.git
cd kindle-wallpaper-tool
```

### Install Dependencies

There are two ways to install dependencies:

#### Automatic Installation (Recommended)

```bash
# Run the setup script (only needs to be run once)
./setup_kindle_converter.sh
```

The script will automatically detect the environment and prioritize the following methods:
1. conda base environment (if conda is installed)
2. pyenv environment (if pyenv is installed)
3. Local virtual environment (default option)

#### Manual Installation

```bash
# Install dependencies using pip
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
# Run using the launch script (recommended)
./run_kindle_converter.sh

# Or run the Python script directly (requires activating the appropriate environment first)
python kindle_image_converter.py
```

The script will interactively ask for the input directory, Kindle model, and output directory.

### Command Line Arguments

```bash
# List all supported Kindle models
./run_kindle_converter.sh --list

# Specify input directory
./run_kindle_converter.sh /path/to/images

# Specify Kindle model
./run_kindle_converter.sh /path/to/images -m oasis2

# Specify output directory
./run_kindle_converter.sh /path/to/images -o /path/to/output

# Combined usage
./run_kindle_converter.sh /path/to/images -m scribe -o /path/to/output
```

### Image Processing Method

The script intelligently processes images to fit the target device's screen aspect ratio:

1. Convert color images to grayscale
2. Smartly crop the center portion of the image according to the target device's aspect ratio
3. Resize the cropped image to match the device's screen resolution
4. Save the processed image

This method avoids simple stretching distortion and preserves the most important parts of the image.

### Output Filename Format

The format of converted filenames is: `[original_filename]_kindle_[device_model].[original_extension]`

For example, converting `vacation.jpg` using the Scribe model will generate `vacation_kindle_scribe.jpg`

## Resolution Sources

The resolution information for Kindle devices comes from: https://bookfere.com/post/694.html

## Contributing

Issues and Pull Requests are welcome to improve this tool.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.