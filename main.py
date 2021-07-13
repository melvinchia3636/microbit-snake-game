def updateScreen():
    basic.clear_screen()
    updateSnakePos()
    drawFood()
    drawSnake()
    music.set_tempo(400)
    music.start_melody(["C7:1"], MelodyOptions.ONCE)
def updateSnakePos():
    if direction == 0:
        snake_head[1] = snake_head[1] - 1
        if snake_head[1] < 0:
            snake_head[1] = 4
    if direction == 1:
        snake_head[1] = snake_head[1] + 1
        if snake_head[1] > 4:
            snake_head[1] = 0
    if direction == 2:
        snake_head[0] = snake_head[0] - 1
        if snake_head[0] < 0:
            snake_head[0] = 4
    if direction == 3:
        snake_head[0] = snake_head[0] + 1
        if snake_head[0] > 4:
            snake_head[0] = 0
    snake_pos.unshift(JSON.parse(JSON.stringify(snake_head)))
    snake_pos.pop()

def on_button_pressed_a():
    global direction
    direction = 2
    music.stop_all_sounds()
    music.set_tempo(400)
    music.start_melody(["C8:1"], MelodyOptions.ONCE_IN_BACKGROUND)
input.on_button_pressed(Button.A, on_button_pressed_a)

def drawFood():
    led.plot_brightness(food[0], food[1], 220)
    if JSON.stringify(food) == JSON.stringify(snake_head):
        recursiveFoodGenerate()
        snake_pos.append(food)
        music.stop_all_sounds()
        music.set_tempo(400)
        music.start_melody(["C7:1", "E7:1", "C8:2"], MelodyOptions.ONCE_IN_BACKGROUND)

def on_pin_pressed_p2():
    global direction
    direction = 1
    music.stop_all_sounds()
    music.set_tempo(400)
    music.start_melody(["C8:1"], MelodyOptions.ONCE_IN_BACKGROUND)
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_b():
    global direction
    direction = 3
    music.stop_all_sounds()
    music.set_tempo(400)
    music.start_melody(["C8:1"], MelodyOptions.ONCE_IN_BACKGROUND)
input.on_button_pressed(Button.B, on_button_pressed_b)

def recursiveFoodGenerate():
    global _food, food
    _food = [randint(0, 4), randint(0, 4)]
    if not (searchForArray(snake_pos, _food)):
        food = _food
        return 0
    recursiveFoodGenerate()
    return 0
def drawSnake():
    for k in snake_pos:
        led.plot_brightness(k[0], k[1], 70)
    led.plot_brightness(snake_head[0], snake_head[1], 255)

def on_logo_pressed():
    global direction
    direction = 0
    music.stop_all_sounds()
    music.set_tempo(400)
    music.start_melody(["C8:1"], MelodyOptions.ONCE_IN_BACKGROUND)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

_food: List[number] = []
food: List[number] = []
snake_pos: List[List[number]] = []
snake_head: List[number] = []
direction = 0
def searchForArray(array: List[any], target: List[any]):
    array_str = JSON.stringify(array)
    target_str = JSON.stringify(target)
    return array_str.includes(target_str)
_is_target = False
direction = 0
speed = 700
snake_head = [2, 2]
snake_pos = [[2, 2], [2, 3]]
recursiveFoodGenerate()

def on_every_interval():
    updateScreen()
loops.every_interval(speed, on_every_interval)
