from utils.model import *
from PIL import Image


class View:
    model: Model

    def __init__(self, model):
        self.model = model

    def canvas_update(self):
        x1, y1 = 0, 0

        pg.draw.rect(self.model.screen, (36, 36, 36), (0, self.model.screen_size[1] - 20, self.model.screen_size[0], 20))
        pg.draw.rect(self.model.screen, (150, 0, 0), (self.model.screen_size[0] - 20, self.model.screen_size[1] - 20, 20, 20))
        self.model.screen.blit(self.model.small_font.render("Rendering", True, (0, 0, 0)),
                               (self.model.screen_size[0] - 135, self.model.screen_size[1] - 20))
        pg.display.update()
        self.model.screen.fill((133, 133, 133))
        pg.draw.rect(self.model.screen, (255, 255, 255),
                     (self.model.pos[0][0], self.model.pos[0][1], self.model.size[0], self.model.size[1]))

        for j in self.model.mouse_data:
            for y in range(j[0][1] - j[1][1], j[0][1] + j[1][1]):
                for x in range(j[0][0] - j[1][1], j[0][0] + j[1][1]):
                    if (x - j[0][0]) ** 2 + (y - j[0][1]) ** 2 <= j[1][1] ** 2:
                        try:
                            self.model.data[y - self.model.pos[0][1]][x - self.model.pos[0][0]] = j[1][0]
                        except IndexError:
                            pass

        self.model.mouse_data = set()

        for i in self.model.data:
            for color in i:
                if color != (255, 255, 255):
                    self.model.screen.set_at((x1 + self.model.pos[0][0], y1 + self.model.pos[0][1]), color)

                x1 += 1

            y1 += 1
            x1 = 0

        pg.draw.rect(self.model.screen, (36, 36, 36),
                     (0, self.model.screen_size[1] - 20, self.model.screen_size[0], 20))
        self.model.screen.blit(self.model.small_font.render("Waiting", True, (0, 0, 0)),
                           (self.model.screen_size[0] - 135, self.model.screen_size[1] - 20))
        pg.draw.rect(self.model.screen, (0, 150, 0),
                     (self.model.screen_size[0] - 20, self.model.screen_size[1] - 20, 20, 20))
        pg.display.update()

    def ui_update(self):
        pg.draw.rect(self.model.screen, (36, 36, 36), (0, 0, 400, 30))
        pg.draw.rect(self.model.screen, (36, 36, 36), (0, 30, 100, 100))
        pg.draw.line(self.model.screen, (0, 0, 0), (0, 30), (100, 30), width=2)
        pg.draw.line(self.model.screen, (0, 0, 0), (99, 30), (99, 0), width=2)
        pg.draw.line(self.model.screen, (0, 0, 0), (199, 30), (199, 0), width=2)
        pg.draw.line(self.model.screen, (0, 0, 0), (299, 30), (299, 0), width=2)
        self.model.screen.blit(self.model.big_font.render("Brush", True, (0, 0, 0)), (0, 0))
        self.model.screen.blit(self.model.big_font.render("New", True, (0, 0, 0)), (100, 0))
        self.model.screen.blit(self.model.big_font.render("Save", True, (0, 0, 0)), (200, 0))
        self.model.screen.blit(self.model.big_font.render("Load", True, (0, 0, 0)), (300, 0))

        pg.draw.circle(self.model.screen, self.model.color, (50, 80), self.model.width)
        pg.display.update()

    def load_image(self):
        self.model.data = []
        file_name = ""
        flag = True
        while flag:
            pg.draw.rect(self.model.screen, (36, 36, 36),
                         (self.model.screen_size[0] // 2 - 300, self.model.screen_size[1] // 2 - 100, 600, 200))
            self.model.screen.blit(self.model.big_font.render("Enter file name", True, (0, 0, 0)),
                          (self.model.screen_size[0] // 2 - 100, self.model.screen_size[1] // 2 - 90))
            self.model.screen.blit(self.model.big_font.render(file_name, True, (0, 0, 0)),
                          (self.model.screen_size[0] // 2 - 100 - len(file_name) ** 1.6, self.model.screen_size[1] // 2 - 60))
            pg.display.update()
            for e in pg.event.get():
                if e.type == pg.KEYDOWN:
                    letter = pg.key.name(e.key)
                    if letter == "return":
                        flag = False

                    if letter == "backspace":
                        file_name = file_name[:-1]

                    if letter == "escape":
                        print("user exited loading screen")
                        return True

                    if not len(letter) > 1 and len(file_name) != 27:
                        file_name += letter

        if file_name[-4:] == ".jpg":
            try:
                image = Image.open(file_name)

                self.model.size = image.size
                self.model.pos = [(self.model.screen_size[0] // 2 - self.model.size[0] // 2, self.model.screen_size[1] // 2 - self.model.size[1] // 2),
                         (self.model.screen_size[0] // 2 + self.model.size[0] // 2, self.model.screen_size[1] // 2 + self.model.size[1] // 2)]

                pix = image.load()
                pg.draw.rect(self.model.screen, (36, 36, 36),
                             (self.model.screen_size[0] // 2 - 300, self.model.screen_size[1] // 2 - 100, 600, 200))
                self.model.screen.blit(self.model.big_font.render("Loading " + file_name, True, (0, 0, 0)),
                              (self.model.screen_size[0] // 2 - 100, self.model.screen_size[1] // 2))
                for y in range(self.model.size[1]):
                    _ = []
                    for x in range(self.model.size[0]):
                        _.append((pix[x, y]))

                    self.model.data.append(_)

                print("image loaded successfully")
                return True

            except FileNotFoundError:
                print("file not found")
                return False

    def save_image(self):
        file_count = 1
        image_saved = False
        mode = False
        while not mode:
            mode = "jpg"
            if mode == "jpg":
                while not image_saved:
                    try:
                        pg.draw.rect(self.model.screen, (36, 36, 36),
                                     (self.model.screen_size[0] // 2 - 300, self.model.screen_size[1] // 2 - 100, 600, 200))
                        self.model.screen.blit(self.model.big_font.render("Saving", True, (0, 0, 0)),
                                      (self.model.screen_size[0] // 2 - 50, self.model.screen_size[1] // 2))
                        pg.display.update()

                        __ = Image.open(f"new-image{file_count}.jpg")
                        file_count += 1
                    except FileNotFoundError:
                        saving_image_jpg = Image.new("RGB", self.model.size, color="white")
                        pix = saving_image_jpg.load()
                        for y in range(self.model.size[1]):
                            for x in range(self.model.size[0]):
                                pix[x, y] = self.model.data[y][x]

                        saving_image_jpg.save(f"new-image{file_count}.jpg")

                        image_saved = True

    def new_image(self):
        new_size = ["_", "_"]
        state = 0
        flag = True
        state_one = "<"
        state_two = " "
        while flag:
            pg.draw.rect(self.model.screen, (36, 36, 36),
                         (self.model.screen_size[0] // 2 - 300, self.model.screen_size[1] // 2 - 100, 600, 200))
            self.model.screen.blit(self.model.big_font.render("Enter size, previous image will be deleted", True, (0, 0, 0)),
                          (self.model.screen_size[0] // 2 - 290, self.model.screen_size[1] // 2 - 30))
            self.model.screen.blit(self.model.big_font.render(f"{new_size[0] + state_one}, {new_size[1] + state_two}",
                                            True, (0, 0, 0)),
                          (self.model.screen_size[0] // 2 + 18 - len(new_size[0]) * 9 - len(new_size[0]) * 9,
                           self.model.screen_size[1] // 2))
            pg.display.update()
            for e in pg.event.get():
                if e.type == pg.KEYDOWN:
                    letter = pg.key.name(e.key)
                    if letter == "return":
                        if state == 1:
                            self.model.size = (int(new_size[0]), int(new_size[1]))
                            self.model.pos = ((self.model.screen_size[0] // 2 - self.model.size[0] // 2,
                                      self.model.screen_size[1] // 2 - self.model.size[1] // 2),
                                     (self.model.screen_size[0] // 2 + self.model.size[0] // 2,
                                      self.model.screen_size[1] // 2 + self.model.size[1] // 2))
                            self.model.data = [[(255, 255, 255) for _ in range(self.model.size[0])] for __ in range(self.model.size[1])]
                            flag = False
                            print("created new image successfully")

                        elif new_size[0] != "_":
                            state = 1
                            state_one = " "
                            state_two = "<"

                    if letter == "backspace":
                        new_size[state] = new_size[state][:-1]
                        if new_size[state] == "":
                            new_size[state] = "_"

                    if letter == "escape":
                        print("user exited size screen")
                        flag = False

                    if letter.isdigit():
                        if new_size[state] == "_":
                            new_size[state] = ""

                        new_size[state] += letter

        return self.model.pos

    def changing_settings(self):
        red, green, blue = self.model.color
        width = self.model.width
        flag = 0
        curr_state_r = ""
        curr_state_g = ""
        curr_state_b = ""
        curr_state_w = ""
        while True:
            if flag == 4:
                break

            if flag <= 0:
                flag = 0
                curr_state_r = "<"
                curr_state_g = ""
                curr_state_b = ""
                curr_state_w = ""

            if flag == 1:
                curr_state_r = ""
                curr_state_g = "<"
                curr_state_b = ""
                curr_state_w = ""

            if flag == 2:
                curr_state_r = ""
                curr_state_g = ""
                curr_state_b = "<"
                curr_state_w = ""

            if flag == 3:
                curr_state_r = ""
                curr_state_g = ""
                curr_state_b = ""
                curr_state_w = "<"

            pg.draw.rect(self.model.screen, (36, 36, 36),
                         (self.model.screen_size[0] // 2 - 300, self.model.screen_size[1] // 2 - 100, 600, 200))
            self.model.screen.blit(self.model.big_font.render("R: " + str(red) + curr_state_r, True, (0, 0, 0)),
                          (self.model.screen_size[0] // 2 - 200, self.model.screen_size[1] // 2 - 90))
            self.model.screen.blit(self.model.big_font.render("G: " + str(green) + curr_state_g, True, (0, 0, 0)),
                          (self.model.screen_size[0] // 2 - 200, self.model.screen_size[1] // 2 - 60))
            self.model.screen.blit(self.model.big_font.render("B: " + str(blue) + curr_state_b, True, (0, 0, 0)),
                          (self.model.screen_size[0] // 2 - 200, self.model.screen_size[1] // 2 - 30))
            self.model.screen.blit(self.model.big_font.render("Width: " + str(width) + curr_state_w, True, (0, 0, 0)),
                          (self.model.screen_size[0] // 2 - 200, self.model.screen_size[1] // 2))
            pg.draw.circle(self.model.screen, (red, green, blue),
                           (self.model.screen_size[0] // 2, self.model.screen_size[1] // 2), width)
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        return

                    if event.key == pg.K_SPACE:
                        flag += 1

                    if event.key == pg.K_b:
                        flag -= 1

                if event.type == pg.MOUSEWHEEL:
                    if flag == 0:
                        red += event.y * 3
                        if red < 0:
                            red = 0

                        if red > 255:
                            red = 255

                    if flag == 1:
                        green += event.y * 3
                        if green < 0:
                            green = 0

                        if green > 255:
                            green = 255

                    if flag == 2:
                        blue += event.y * 3
                        if blue < 0:
                            blue = 0

                        if blue > 255:
                            blue = 255

                    if flag == 3:
                        width += event.y
                        if width < 5:
                            width = 5

                        if width > 50:
                            width = 50

        self.model.color = (red, green, blue)
        self.model.width = width
