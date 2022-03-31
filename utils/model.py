import ctypes
import pygame as pg


class Model:
    data: list
    mouse_data: set
    size: tuple
    screen_size: tuple
    screen: pg.display.set_mode
    pos: tuple
    color: tuple
    width: int
    big_font: pg.font.SysFont
    small_font: pg.font.SysFont
    zoom: float

    def __init__(self):
        self.mouse_data = set()
        self.size = 720, 720
        self.screen_size = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
        self.big_font = pg.font.SysFont("Aerial", 40)
        self.small_font = pg.font.SysFont("Aerial", 30)
        self.color = (0, 0, 0)
        self.width = 15
        self.zoom = 1
        self.data = [[(255, 255, 255) for _ in range(self.size[0])] for __ in range(self.size[1])]
        self.screen = pg.display.set_mode((self.screen_size[0], self.screen_size[1]))
        self.pos = ((self.screen_size[0] // 2 - self.size[0] // 2, self.screen_size[1] // 2 - self.size[1] // 2),
                    (self.screen_size[0] // 2 + self.size[0] // 2, self.screen_size[1] // 2 + self.size[1] // 2))
