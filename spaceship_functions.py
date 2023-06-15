from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QTimer

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
    if window.spaceship_window.user_input.text() == "3.7" or window.spaceship_window.user_input.text() == "3,7":
        # change background_img
        img = QPixmap('images\spaceship_opened.png')
        window.spaceship_window.bg_img_lb.setPixmap(img)
        window.spaceship_window.get_tractor_btn.show()
    else:
        print("WRONG ANSWEAR")
    close_frames(window)


def enter_portal(window):
    window.spaceship_window.close()
    window.end_window.show()


def glitch_screen_spaceship(window):
    window.spaceship_window.main_screen_frame.close()
    window.spaceship_window.math_frame.close()
    window.movie = QMovie("images/gifs/glitch_gif.gif")
    window.spaceship_window.bg_img_lb.setMovie(window.movie)
    window.movie.start()
    timer = QTimer()
    timer.singleShot(2000, lambda: enter_portal(window))
