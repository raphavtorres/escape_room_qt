# x = raiz(4,84)
# conta => 3 * 2/4 + x = y
# resposta: y = 3,7


def open_error_screen(window):
    window.spaceship_window.main_screen_frame.show()
    window.spaceship_window.close_btn.show()
    

def open_math_screen(window):
    window.spaceship_window.math_frame.show()
    window.spaceship_window.close_btn.show()


def close_frames(window):
    window.spaceship_window.main_screen_frame.close()
    window.spaceship_window.math_frame.close()
    window.spaceship_window.close_btn.close()


def read_user_input(window):
    if window.spaceship_window.user_input.text() == "3.7":
        # change background_img
        ...
    else:
        print("WRONG ANSWEAR")
    close_frames(window)