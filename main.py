# Importing Library
import numpy as np
import cv2

# Define the input and output paths
inputPath = 'static/img6.png'

# Load the color image
orignalImage = cv2.imread(inputPath)



# ------------Convert image to Grayscale --------------

# Convert the color image to grayscale image
grayscaleImage = cv2.cvtColor(orignalImage, cv2.COLOR_BGR2GRAY)

# Save the color image to disk
outputPath = 'converted/grayScale.png'
cv2.imwrite(outputPath, grayscaleImage)

# Display the converted image
cv2.imshow('Grayscale Image', grayscaleImage)
cv2.waitKey(0)


# Display a message indicating that the image has been saved
print('Converted Grayscale image saved to disk : ' + outputPath)


# # ----------------- Convert image to Oil Painting -----------------------


# Apply the oil painting effect
oilImg = cv2.xphoto.oilPainting(orignalImage, size=7, dynRatio=1)

# Save the oil painting effect image to disk
outputPath = 'converted/oilPainting.png'
cv2.imwrite(outputPath, oilImg)

# Display the converted image
cv2.imshow('Oil Paint Image', oilImg)
cv2.waitKey(0)

# Display a message indicating that the image has been saved
print('Converted Oil Paint image saved to disk: ' + outputPath)



# # ----------------- Convert image to Sketch Image ---------------

# Invert the grayscale image
invertedImg = 255 - grayscaleImage

# Apply Gaussian blur
blurredImg = cv2.GaussianBlur(invertedImg, (21, 21), 0)

# Blend the grayscale image and the blurred image using the color dodge blend mode
sketchImg = cv2.divide(grayscaleImage, 255 - blurredImg, scale=256)

# Save the sketch image to disk
outputPath = 'converted/sketch.png'
cv2.imwrite(outputPath, sketchImg)

# Display the converted image
cv2.imshow('Sketch Image', sketchImg)
cv2.waitKey(0)

# Display a message indicating that the image has been saved
print('Converted Sketch image saved to disk: ' + outputPath)