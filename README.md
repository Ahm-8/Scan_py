# Document Scanner Project
Overview
This project provides a set of Python scripts to transform images of documents into scanned, high-quality copies. The primary script, scan.py, processes an image to detect the document's edges, applies a perspective transformation, and converts the image to a clean black and white version. The helper script transform.py contains functions for performing the four-point perspective transform.

Project Structure
The project consists of three main files:

scan.py: Main script to process and scan the document from an image.
transform.py: Contains utility functions for performing perspective transformations.
transform_example.py: Example script demonstrating the use of the four_point_transform function.
Dependencies
To run this project, you need the following Python packages:

numpy
argparse
opencv-python (cv2)
scikit-image
imutils

You can install these dependencies using pip:
pip install numpy argparse opencv-python scikit-image imutils


Usage
1. scan.py
This script processes an image to detect the document and applies a perspective transform to get a top-down view.

Arguments
-i, --image: Path to the image to be scanned (required).

Example: python scan.py --image path/to/your/image.jpg

2. transform_example.py
This script demonstrates the usage of the four_point_transform function with specified coordinates.

Arguments
-i, --image: Path to the image file.
-c, --coords: Comma-separated list of source points for the transformation.
Example: python transform_example.py --image path/to/your/image.jpg --coords "[[x1, y1], [x2, y2], [x3, y3], [x4, y4]]"


Detailed Script Descriptions
1. scan.py
Argument Parsing: Uses argparse to handle command-line arguments.
Image Loading and Resizing: Loads the image and resizes it for processing.
Edge Detection: Converts the image to grayscale, blurs it, and detects edges.
Contour Detection: Finds contours in the edged image and identifies the document contour.
Perspective Transformation: Applies the four-point transform to get a top-down view of the document.
Thresholding: Converts the transformed image to a black and white version to simulate a scanned document.
Display Results: Shows the original, edged, and final scanned images.

2. transform.py
Contains utility functions:
order_points(pts): Orders points in a consistent manner.
four_point_transform(image, pts): Applies a perspective transform to the image based on the provided four points.
Functions
order_points(pts)

Takes an array of four points and returns them in a consistent order: top-left, top-right, bottom-right, bottom-left.
This ordering is necessary for the perspective transform to work correctly.
four_point_transform(image, pts)

Takes an image and an array of four points.
Orders the points using order_points.
Computes the dimensions of the new transformed image.
Constructs the perspective transform matrix.
Applies the perspective transformation to the image.
Returns the transformed (warped) image.
transform_example.py
This script demonstrates how to use the four_point_transform function from transform.py with hardcoded source points.

Steps
1. Argument Parsing: Uses argparse to handle command-line arguments for the image path and coordinates.
2. Image Loading: Loads the image using OpenCV.
3. Coordinate Parsing: Converts the provided coordinate string into a NumPy array.
4. Perspective Transformation: Applies the four_point_transform to the image using the provided coordinates.
5. Display Results: Shows the original and warped images.
   
Example Workflow
To scan a document using the scan.py script:

1.Prepare the Image: Ensure your image is clear and contains a well-defined document.
2. Run the Script: python scan.py --image path/to/your/document.jpg

3. View the Results: The script will display the original image, edge-detected image, and the final scanned image. Press any key to close the displayed images.
To test the perspective transformation manually using transform_example.py:

1. Prepare the Image: Choose an image and determine the coordinates of the document corners.
2. Run the Script: python transform_example.py --image path/to/your/image.jpg --coords "[[x1, y1], [x2, y2], [x3, y3], [x4, y4]]"
3. View the Results: The script will display the original and the warped (transformed) images. Press any key to close the displayed images.

