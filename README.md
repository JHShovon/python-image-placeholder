# ⚡ Python Image Placeholder

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/JHShovon/python-image-placeholder?style=for-the-badge)](https://github.com/JHShovon/python-image-placeholder/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/JHShovon/python-image-placeholder?style=for-the-badge)](https://github.com/JHShovon/python-image-placeholder/network)
[![GitHub issues](https://img.shields.io/github/issues/JHShovon/python-image-placeholder?style=for-the-badge)](https://github.com/JHShovon/python-image-placeholder/issues)
[![GitHub license](https://img.shields.io/github/license/JHShovon/python-image-placeholder?style=for-the-badge)](LICENSE)

**A simple command-line tool to generate placeholder images using Python.**

</div>

## 📖 Overview

This Python script generates placeholder images of specified dimensions and color. It's designed for quick prototyping and development, providing a simple way to fill image slots with visually representative placeholders without needing external resources.  The tool is command-line driven for easy integration into workflows.


## ✨ Features

- Generates placeholder images with customizable dimensions.
- Sets a solid background color for the placeholder.
- Simple command-line interface for ease of use.
- Outputs images in PNG format.


## 🖥️ Screenshots

![Placeholder Image Example](python-placeholder-image-generate.png)


## 🛠️ Tech Stack

- **Language:** Python


## 🚀 Quick Start

### Prerequisites

- Python 3.x (Specific version not explicitly stated, but 3.x is assumed based on common Python usage)
- Pillow library (`pip install Pillow`)


### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/JHShovon/python-image-placeholder.git
   cd python-image-placeholder
   ```

2. **Install dependencies:**
   ```bash
   pip install Pillow
   ```


### Usage

The script takes width, height and color as command line arguments. The color can be specified as a hex code, an RGB tuple (R,G,B), or a color name.

```bash
python img-placeholder/main.py <width> <height> <color>
```

**Examples:**

- Generate a 300x200 placeholder image with a red background:
  ```bash
  python img-placeholder/main.py 300 200 red
  ```

- Generate a 500x500 placeholder image with a background color specified by hex code:
  ```bash
  python img-placeholder/main.py 500 500 #00FF00
  ```

- Generate a 100x100 placeholder image with a background color specified by an RGB tuple (Blue):
  ```bash
  python img-placeholder/main.py 100 100 (0,0,255)
  ```


## 📁 Project Structure

```
python-image-placeholder/
├── img-placeholder/
│   └── main.py       # Main script for image generation.
├── README.md          # This file.
├── command-line.txt    # Description of command-line usage (redundant - included in README).
└── python-placeholder-image-generate.png # Example image
```

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.  (Note: No LICENSE file found in provided repository data.  This needs to be added)

---

<div align="center">

**Made with ❤️ by JHShovon**

</div>
