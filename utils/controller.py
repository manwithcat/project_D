from utils.model import *
from utils.view import *


class Controller:
    model: Model
    view: View

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def flag_1(self):
        ui = False

        for e in pg.event.get():
            if pg.key.get_pressed()[pg.K_LCTRL]:
                ui = True
                self.view.ui_update()
                mouse_pos = pg.mouse.get_pos()
                button_pressed = pg.mouse.get_pressed(num_buttons=3)
                pg.draw.rect(self.model.screen, (133, 133, 133), (0, 0, 400, 31))
                pg.draw.rect(self.model.screen, (133, 133, 133), (0, 30, 101, 100))

                if mouse_pos[1] <= 30 and 300 <= mouse_pos[0] <= 400 and button_pressed[0] == 1:
                    print("flag: 0")
                    return ui, 0

                elif mouse_pos[1] <= 30 and 200 <= mouse_pos[0] <= 300 and button_pressed[0] == 1:
                    print("flag: 2")
                    return ui, 2

                elif mouse_pos[1] <= 30 and 100 <= mouse_pos[0] <= 200 and button_pressed[0] == 1:
                    print("flag: 3")
                    return ui, 3

                elif mouse_pos[1] <= 30 and 0 <= mouse_pos[0] <= 100 and button_pressed[0] == 1:
                    print("flag: 4")
                    return ui, 4

            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_SPACE:
                    self.view.canvas_update()

            elif e.type == pg.MOUSEMOTION:
                pg.display.update()
                mouse_pos = pg.mouse.get_pos()
                button_pressed = pg.mouse.get_pressed(num_buttons=3)

                if self.model.pos[0][1] <= mouse_pos[1] <= self.model.pos[1][1] and self.model.pos[0][0] <= mouse_pos[0] <= self.model.pos[1][0] and button_pressed[0] == 1:
                    return ui, (mouse_pos, (self.model.color, self.model.width))
