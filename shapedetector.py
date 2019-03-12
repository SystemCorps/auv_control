import cv2

class ShapeDetector:
# https://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/

    def __init__(self):
        pass
    
    def detect(self, c):
        # Initialize the shape name and approximate the contour
        # c: Contour
        shape = "unidentified"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
        
        if len(approx) == 3:
            shape = "triangle"
            
        elif len(approx) == 4:
            # computing bounding box of the contour
            # and use the box to compute the apect ratio
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)
            
            shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
            
        elif len(approx) == 5:
            shape = "pentagon"
            
        else:
            shape = "circle"
            
        return shape