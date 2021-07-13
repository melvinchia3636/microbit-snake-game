function updateScreen () {
    basic.clearScreen()
    updateSnakePos()
    drawSnake()
    drawFood()
    music.setTempo(400)
    music.startMelody(["C7:1"], MelodyOptions.Once)
}
function updateSnakePos () {
    if (direction == 0) {
        snake_head[1] = snake_head[1] - 1
        if (snake_head[1] < 0) {
            snake_head[1] = 4
        }
    }
    if (direction == 1) {
        snake_head[1] = snake_head[1] + 1
        if (snake_head[1] > 4) {
            snake_head[1] = 0
        }
    }
    if (direction == 2) {
        snake_head[0] = snake_head[0] - 1
        if (snake_head[0] < 0) {
            snake_head[0] = 4
        }
    }
    if (direction == 3) {
        snake_head[0] = snake_head[0] + 1
        if (snake_head[0] > 4) {
            snake_head[0] = 0
        }
    }
    snake_pos.unshift(JSON.parse(JSON.stringify(snake_head)))
    snake_pos.pop()
}
input.onButtonPressed(Button.A, function () {
    direction = 2
    music.stopAllSounds()
    music.setTempo(400)
    music.startMelody(["C8:1"], MelodyOptions.OnceInBackground)
})
function drawFood () {
    led.plotBrightness(food[0], food[1], 220)
    if (JSON.stringify(food) == JSON.stringify(snake_head)) {
        recursiveFoodGenerate()
        snake_pos.push(food)
        music.stopAllSounds()
        music.setTempo(400)
        music.startMelody(["C7:1", "E7:1", "C8:2"], MelodyOptions.OnceInBackground)
    }
}
input.onPinPressed(TouchPin.P2, function () {
    direction = 1
    music.stopAllSounds()
    music.setTempo(400)
    music.startMelody(["C8:1"], MelodyOptions.OnceInBackground)
})
input.onButtonPressed(Button.B, function () {
    direction = 3
    music.stopAllSounds()
    music.setTempo(400)
    music.startMelody(["C8:1"], MelodyOptions.OnceInBackground)
})
function recursiveFoodGenerate () {
    _food = [randint(0, 4), randint(0, 4)]
    if (!(searchForArray(snake_pos, _food))) {
        food = _food
        return 0
    }
    recursiveFoodGenerate()
    return 0
}
function drawSnake () {
    for (let k of snake_pos) {
        led.plotBrightness(k[0], k[1], 70)
    }
    led.plotBrightness(snake_head[0], snake_head[1], 255)
}
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    direction = 0
    music.stopAllSounds()
    music.setTempo(400)
    music.startMelody(["C8:1"], MelodyOptions.OnceInBackground)
})
let _food: number[] = []
let food: number[] = []
let snake_pos: number[][] = []
let snake_head: number[] = []
let direction = 0
function searchForArray (array: any[], target: any[]) {
    const array_str = JSON.stringify(array)
    const target_str = JSON.stringify(target)

    return array_str.includes(target_str)
}
let _is_target = false
direction = 0
let speed = 700
snake_head = [2, 2]
snake_pos = [[2, 2], [2, 3]]
recursiveFoodGenerate()
loops.everyInterval(speed, function () {
    updateScreen()
})
