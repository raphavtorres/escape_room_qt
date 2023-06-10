from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QTimer


def open_shelf(window, shelf_window):
    window.two_story_house_window.close()
    shelf_window.show()


def back_to_two_story_house(window, shelf_window, won=False):
    shelf_window.close()
    open_portal(window) if won else window.two_story_house_window.show()


def get_two_story_paper(window):
    window.two_story_house_window.paper_frame.show()
    window.two_story_house_window.close_paper_btn.show()
    window.two_story_house_window.demon_btn.show()
    window.two_story_house_window.demon_lb.show()


def close_paper_key_cabinet(window):
    window.two_story_house_window.paper_frame.close()
    window.two_story_house_window.key_frame.close()
    window.two_story_house_window.close_paper_btn.close() 


def death_window(window):
    window.two_story_house_window.close()
    window.movie = QMovie("images/gifs/death_wolf.gif")
    window.death_window.bg_gif_lb.setMovie(window.movie)
    window.movie.start()
    window.death_window.show()


def show_key(window):
    window.two_story_house_window.key_frame.show()
    window.two_story_house_window.close_paper_btn.show()



def open_portal(window):
    # window.gamer_room_portal.show()
    # window.movie = QMovie("images/gifs/gamer_room_portal_gif.gif")
    # window.gamer_room_portal.bg_gif_lb.setMovie(window.movie)
    # window.movie.start()
    ...