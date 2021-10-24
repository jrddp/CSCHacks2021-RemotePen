import cv2
import cv2.aruco as aruco

def draw_corners(img, bboxs):
    aruco.drawDetectedMarkers(img, bboxs)

def circle_point(img, point, color=(255, 0, 255), radius=5, thickness=50):
    x, y = point
    x, y = int(x), int(y)
    cv2.circle(img, (x, y), radius=radius, color=color, thickness=thickness)


def circle_points(img, points):
    for point in points:
        circle_point(img, point)
