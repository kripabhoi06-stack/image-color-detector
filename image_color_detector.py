import cv2
import numpy as np

# Read image
image = cv2.imread("img1.jpeg")

# Resize image
image = cv2.resize(image, (300, 300))

# Convert to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Calculate average color
avg_color = np.mean(image_rgb, axis=(0, 1))

# Convert to integer
avg_color = avg_color.astype(int)

# Detect color name
def detect_color(rgb):
    r, g, b = rgb
    if r > g and r > b:
        return "Red"
    elif g > r and g > b:
        return "Green"
    elif b > r and b > g:
        return "Blue"
    else:
        return "Mixed Color"

color_name = detect_color(avg_color)

print("Dominant Color:", color_name)
print("RGB Values:", avg_color)
