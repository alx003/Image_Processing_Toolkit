# Image Processing and KNN Classification Toolkit

## Overview
This project, completed as part of the DSC 20 course at UC San Diego, features a custom-built image processing library and a K-Nearest Neighbors (KNN) classifier implemented from scratch using Python.

## Key Features
- **Custom RGBImage Class**: Managed raw pixel data and implemented core functionalities like deep copying and pixel manipulation.
- **Image Transformation Suite**: 
  - Standard Filters: Grayscale, 180-degree rotation, brightness adjustment, and negation.
  - Advanced Effects: Edge detection (using kernels) and pixelation.
- **KNN Image Classifier**: A machine learning model that classifies images (e.g., distinguishing between 'daytime' and 'nighttime') by calculating Euclidean distances between pixel arrays.
- **Interactive GUI**: A Tkinter-based image viewer with zoom functionality and real-time pixel color inspection.

## Project Structure
- `knn_data/`: Dataset used for training and testing the KNN classifier.
- `img/`: Sample images and validation sets for image processing functions.

## Technical Skills
- Python (NumPy, Pillow, Tkinter)
- Object-Oriented Programming (Inheritance, Abstract Templates)
- Machine Learning Basics (KNN Algorithm)
- Data Structures (3D Matrix manipulation for RGB channels)

## Usage
To run the interactive image viewer:
```bash
python3 image_viewer.py <path_to_image>
