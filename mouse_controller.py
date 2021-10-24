import pyautogui

def img_point_to_mouse_point(img, img_point):
    img_w, img_h, _ = img.shape
    img_x, img_y = img_point
    x_ratio = img_x / img_w
    y_ratio = img_y / img_h

    # flip horizontally
    x_ratio = 1 - x_ratio

    screen_w, screen_h = pyautogui.size()
    x = int(screen_w * x_ratio)
    y = int(screen_h * y_ratio)

    return (x, y)

def move_mouse(point):
    x, y = point
    pyautogui.moveTo(x, y)

if __name__ == "__main__":
    print(pyautogui.size())
    pyautogui.moveTo(100, 150)