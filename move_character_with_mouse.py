from pico2d import *
import random
import time

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')


def handle_events():
    global running
    global character_x, character_y  # 캐릭터 좌표
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            hand_x, hand_y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


running = True
character_x, character_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()

hand_x = 0
hand_y = 0

prev_time = time.time()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    # 캐릭터 이동
    if character_x < hand_x:
        character_x += 1
    elif character_x > hand_x:
        character_x -= 1
    if character_y < hand_y:
        character_y += 1
    elif character_y > hand_y:
        character_y -= 1

    character.clip_draw(frame * 100, 100 * 1, 100, 100, character_x, character_y)

    current_time = time.time()
    if current_time - prev_time >= 5.0:
        hand_x = random.randint(0, TUK_WIDTH - 1)
        hand_y = random.randint(0, TUK_HEIGHT - 1)
        prev_time = current_time

    hand.draw(hand_x, hand_y)

    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()