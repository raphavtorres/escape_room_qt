from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QTimer


def open_computer(window):
    window.gamer_room_window.close()
    window.computer_screen.show()
    window.computer_screen.password_frame.close()
    window.computer_screen.file_opened_frame.close()


def show_clock(window):
    window.gamer_room_window.clock_lb.show()
    window.gamer_room_window.close_paper_clock_btn.show()


def get_paper(window):
    window.gamer_room_window.opened_paper_lb.show()
    window.gamer_room_window.close_paper_clock_btn.show()


def close_paper_clock(window):
    window.gamer_room_window.clock_lb.close()
    window.gamer_room_window.opened_paper_lb.close()
    window.gamer_room_window.close_paper_clock_btn.close()


def open_street_window(window):
    window.gamer_room_window.close()
    window.street_window.show()


def back_to_room(window, won=False):
    window.computer_screen.close()
    window.street_window.close()
    open_portal(window) if won else window.gamer_room_window.show()


def open_file_click(window):
    window.computer_screen.password_frame.show()


def check_input(window):
    if window.computer_screen.pass_input.text() == "python":
        window.computer_screen.file_opened_frame.show()
    else:
        print("WRONG PASS")
    window.computer_screen.password_frame.close()


def finish_level(window):
    back_to_room(window, won=True)


def enter_portal(window):
    window.gamer_room_portal.close()
    window.two_story_house_window.show()


def glitch_screen(window):
    window.movie = QMovie("images/gifs/glitch_gif.gif")
    window.gamer_room_portal.bg_gif_lb.setMovie(window.movie)
    window.movie.start()
    timer = QTimer()
    timer.singleShot(2000, lambda: enter_portal(window))


def open_portal(window):
    window.gamer_room_portal.show()
    window.movie = QMovie("images/gifs/gamer_room_portal_gif.gif")
    window.gamer_room_portal.bg_gif_lb.setMovie(window.movie)
    window.movie.start()
