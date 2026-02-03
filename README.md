# Image Color Detector

## Overview

This project is a simple Python program that detects the dominant color in an image using OpenCV and NumPy. It calculates the average color of an image and identifies whether Red, Green, or Blue is the dominant color.

## How It Works

1. Reads and resizes the input image to 300x300 pixels.
2. Converts the image from BGR to RGB color space.
3. Calculates the average RGB color values.
4. Compares the average values to detect the dominant color.
5. Prints the dominant color name and the average RGB values.

## Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- NumPy

## Installation

Install the required Python libraries using pip:

```bash
pip install opencv-python numpy
