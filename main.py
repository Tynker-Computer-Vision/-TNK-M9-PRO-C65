# Importing Library
import cv2

# Define the input and output paths
input_path = 'static/img1.png'
output_path = 'converted/convertedImg.jpg'


# ------------Convert image to Grayscale --------------

# Load the image
gray_img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

# Convert the grayscale image to color
color_img = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)

# Save the color image to disk
cv2.imwrite(output_path, color_img)

# Display the converted image
cv2.imshow('Converted Image', color_img)
cv2.waitKey(0)

# Display a message indicating that the image has been saved
print(f'Converted image saved to disk: {output_path}')


# # ----------------- Convert image to Sketch Image ---------------

# Load the image
img = cv2.imread(input_path)

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
inverted_img = 255 - gray_img

# Apply Gaussian blur
blurred_img = cv2.GaussianBlur(inverted_img, (21, 21), 0)

# Blend the grayscale image and the blurred image using the color dodge blend mode
sketch_img = cv2.divide(gray_img, 255 - blurred_img, scale=256)

# Save the sketch image to disk
cv2.imwrite(output_path, sketch_img)

# Display the converted image
cv2.imshow('Converted Image', sketch_img)
cv2.waitKey(0)

# Display a message indicating that the image has been saved
print(f'Sketch image saved to disk: {output_path}')


# # ----------------- Convert image to Oil Painting -----------------------


# Load the image
img = cv2.imread(input_path)

# Apply the oil painting effect
oil_img = cv2.xphoto.oilPainting(img, size=7, dynRatio=1)

# Save the oil painting effect image to disk
cv2.imwrite(output_path, oil_img)

# Display the converted image
cv2.imshow('Converted Image', oil_img)
cv2.waitKey(0)

# Display a message indicating that the image has been saved
print(f'Oil painting effect image saved to disk: {output_path}')


# ------------Convert image to RGB  --------------

# Load the image
gray_img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

# Convert the grayscale image to color
RGBcolor_img = cv2.cvtColor(gray_img, cv2.COLOR_BGR2RGB)

# Save the color image to disk
cv2.imwrite(output_path, RGBcolor_img)

# Display the converted image
cv2.imshow('Converted Image', RGBcolor_img)
cv2.waitKey(0)

# Display a message indicating that the image has been saved
print(f'Converted image saved to disk: {output_path}')
