import pyautogui

# the inner portion of the video output that corresponds to the computer screen translation
screen_ratio_x = 0.8
screen_ratio_y = 0.8

def img_point_to_mouse_point(img, img_point):
    img_h, img_w, _ = img.shape
    img_x, img_y = img_point


    screen_w, screen_h = pyautogui.size()

    virtual_w = img_w * screen_ratio_x
    virtual_h = img_h * screen_ratio_y

    virtual_edge_w = (img_w - virtual_w) / 2
    virtual_edge_h = (img_h - virtual_h) / 2

    virtual_ratio_x = min(max(0, (img_x - virtual_edge_w) / virtual_w), 1)
    virtual_ratio_y = min(max(0, (img_y - virtual_edge_h) / virtual_h), 1)

    print(f"{virtual_ratio_x}, {virtual_ratio_y}")

    x = screen_w * virtual_ratio_x
    y = screen_h * virtual_ratio_y

    # flip horizontally
    x = screen_w - x

    x = int(x)
    y = int(y)

    return (x, y)

def move_mouse(point, button_down=False):
    x, y = point
    if button_down:
        pyautogui.dragTo(x, y, button='left')
    else:
        pyautogui.moveTo(x, y)


if __name__ == "__main__":
    print(pyautogui.size())
    pyautogui.moveTo(100, 150)