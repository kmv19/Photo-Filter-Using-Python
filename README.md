# Photo-Filter-GUI-Application-Using-Python
A simple image filter with interactive GUI and incredible features!. 

## Overview
This Python application provides a graphical user interface (GUI) for applying various image filters using OpenCV. Users can open an image file, choose from several filters, and view the processed image in real-time. 

The supported filters include:
- Brightness adjustment
- Contrast adjustment
- Gaussian blur
- Edge detection
- Original image view (reset)

## Features
- **User-Friendly GUI**: Built using Tkinter for an intuitive experience.
- **Filter Options**: Select from multiple filters using a dropdown menu.
- **Image Processing**: Leverages OpenCV and NumPy for efficient image manipulation.
- **Dynamic Display**: Processes and displays the filtered image in real-time.

---

## Requirements
- **Python**: 3.6 or later
- **Dependencies**:
  - OpenCV: `pip install opencv-python`
  - NumPy: `pip install numpy`
  - Pillow: `pip install pillow`

---

## Installation
1. Clone the repository or copy the code into a Python script.
2. Install the required dependencies using:
   ```bash
   pip install opencv-python numpy pillow
   ```

---

## How to Use
1. Run the script:
   ```bash
   python script_name.py
   ```
2. The application window will open.
3. Use the "File" menu to load an image file.
4. Choose a filter from the dropdown menu and click **Apply** to see the effect.
5. The modified image will be displayed in the application window.

---

## Code Structure
### Main Components:
1. **Class `GUI`**: 
   - Initializes the GUI and sets up the interface.
   - Handles user interactions and applies selected filters.

2. **Methods**:
   - `open_image`: Opens and loads an image file.
   - `display_image`: Converts and displays the current image in the GUI.
   - `apply_filter`: Applies the selected filter and updates the display.

3. **Filters**:
   - **Brightness**: Adjusts the brightness of the image using HSV color space.
   - **Contrast**: Enhances the image contrast using scaling.
   - **Blur**: Applies Gaussian blur to smooth the image.
   - **Edges**: Detects edges in the image using the Canny edge detection method.
   - **Original**: Resets the image to its original state.

---

## Notes
- Ensure the images to be processed are accessible on your system. The `filedialog` opens a file explorer to select images.
- Adjust filter parameters like brightness, contrast or blur amount within the code for customization.
- The GUI is initialized with a default image directory for easy access. Update the `initialdir` parameter in the `filedialog` call to change this.

Enjoy experimenting with your images using this Image Filter GUI!
