from utils.controller import *

pg.init()

model = Model()
view = View(model)
controller = Controller(model, view)

view.canvas_update()
# view.ui_update()

running = True
clock = pg.time.Clock()
flag = 1
while running:
    clock.tick(100000000)

    if flag == 0:
        view.load_image()
        view.canvas_update()
        flag = 1
        print("flag: 1")

    elif flag == 1:
        changes = controller.flag_1()

        if changes is not None:
            if changes[0]:
                flag = changes[1]

            else:
                model.mouse_data.add(changes[1])

    elif flag == 2:
        view.save_image()
        view.canvas_update()
        flag = 1
        print("flag: 1")

    elif flag == 3:
        view.new_image()
        view.canvas_update()
        flag = 1
        print("flag: 1")

    elif flag == 4:
        view.changing_settings()
        view.canvas_update()
        flag = 1
        print("flag: 1")
