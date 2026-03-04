import cv2
import json

img = cv2.imread('c:/Users/jarad/Desktop/Mapa/layout.jpg')

units = [
    {"id": "10", "line": "B", "unit": 10, "x": 234, "y": 228, "width": 94, "height": 208},
    {"id": "9", "line": "B", "unit": 9, "x": 328, "y": 228, "width": 56, "height": 208},
    {"id": "1", "line": "B", "unit": 1, "x": 776, "y": 228, "width": 57, "height": 208},
    {"id": "10", "line": "A", "unit": 10, "x": 234, "y": 466, "width": 94, "height": 208},
    {"id": "9", "line": "A", "unit": 9, "x": 328, "y": 466, "width": 56, "height": 208},
    {"id": "1", "line": "A", "unit": 1, "x": 776, "y": 466, "width": 57, "height": 208},
]

for u in units:
    x, y, w, h = u['x'], u['y'], u['width'], u['height']
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

cv2.rectangle(img, (29, 137), (1251, 694), (0, 255, 0), 2)
cv2.imwrite('c:/Users/jarad/Desktop/Mapa/layout_test.jpg', img)
