import cv2
import aruco_detector
import image_drawer
import mouse_controller

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()

        bboxs, ids, rejected = aruco_detector.findArucoMarkers(img)
        centers = aruco_detector.get_bbox_centers(bboxs)
        true_center = aruco_detector.find_center_of_all_bboxs(bboxs)

        image_drawer.draw_corners(img, bboxs)
        image_drawer.circle_points(img, centers)
        if true_center is not None:
            image_drawer.circle_point(img, true_center, color=(255, 255, 0))
            screen_point = mouse_controller.img_point_to_mouse_point(img, true_center)
            mouse_controller.move_mouse(screen_point)

        cv2.imshow('img', img)
        k = cv2.waitKey(30) & 0xff

        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
