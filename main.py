import cv2
import aruco_detector
import image_drawer
import mouse_controller

pen_top_aruco_id = 43
# ordered CCW starting from top left as shown on PrintOut.pdf
pen_side_arcuo_ids = [31, 4, 10, 8]

render_video = True

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()

        bboxs, ids, rejected = aruco_detector.findArucoMarkers(img)

        top_detected = ids is not None and pen_top_aruco_id in ids
        side_detected = ids is not None and any((id in ids for id in pen_side_arcuo_ids))

        centers = aruco_detector.get_bbox_centers(bboxs)
        true_center = aruco_detector.find_center_of_all_bboxs(bboxs)

        if render_video:
            image_drawer.draw_corners(img, bboxs)
            image_drawer.circle_points(img, centers)

        button_down = top_detected and not side_detected
        if true_center is not None:

            if render_video:
                image_drawer.circle_point(img, true_center, color=(255, 255, 0))

            screen_point = mouse_controller.img_point_to_mouse_point(img, true_center)

            mouse_controller.move_mouse(screen_point, button_down=button_down)
        else:
            mouse_controller.move_mouse((None, None), button_down=button_down)

        if render_video:
            # horizontal flip
            img = cv2.flip(img, 1)

            # draw screen point as text
            if true_center is None:
                image_drawer.draw_text(img, (100, 100), "Markers not detected")
            else:
                image_drawer.draw_text(img, (100, 100), str(screen_point))

            cv2.imshow('img', img)
            k = cv2.waitKey(30) & 0xff

            if k == 27:
                break
    cap.release()
    cv2.destroyAllWindows()
