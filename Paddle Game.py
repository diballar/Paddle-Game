import pygame
import sys
import keyboard
import os
from pathlib import Path
from playsound import playsound
import random
from threading import Thread

# Initialize Pygame
pygame.init()

dir = Path(__file__).resolve().parents[0]
print(dir)
os.chdir(dir)

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
pygame.display.set_caption("Paddle Game")

# Set up colors
WHITE = (255, 255, 255)
defa = (0, 0, 0)
def_ = 200

# Set up clock for controlling frame rate
clock = pygame.time.Clock()

font_ = pygame.font.Font("Daydream.ttf", 20)
font = font_.render("poop", False, defa)
font_rect = font.get_rect(left = 5, top = 5)

font_sub = pygame.font.Font("Daydream.ttf", 10)

def sound_(folder):
    return os.listdir(folder)

sounds_ = sound_("sound")
sounds = []
for i in sounds_:
    sounds.append("sound/" + str(i))
print(sounds)

def play_sound_():
    rand = random.choice(sounds)
    playsound(rand)

def thread():
        thread = Thread(target= play_sound_)
        thread.start()

# Variables
score = 0
sub = ""

grav = 0.5
drag = 1
ball_scale = 25
ball_velx = 0
ball_vely = 0
ball = pygame.Rect(WIDTH/2 - ball_scale/2, 20, ball_scale, ball_scale)

rect_vel = 0
rect_width = 125
rect_height = 25
rect = pygame.Rect(WIDTH/2 - rect_width/2, HEIGHT - (10 + rect_height), rect_width, rect_height)

# Main game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if keyboard.is_pressed("escape"):
            pygame.quit()
            sys.exit()

    # Game logic (update variables, check for collisions, etc.)
    if keyboard.is_pressed("left"):
        rect_vel -= 2
    elif keyboard.is_pressed("right"):
        rect_vel += 2
    rect_vel = rect_vel * 0.9
    
    rect.x += rect_vel

    if ball.colliderect(rect):
        if ball.bottom >= rect.top and ball.top <= rect.bottom:
            ball_vely = ball_vely * -1.25
            ball.bottom = rect.top + 1
            ball_velx += rect_vel * 1.1

            if abs(ball_vely) > 4:
                score += 20
                sub = "+20! paddle hit"
                def_ = 0
                thread()

        

    if ball.left <= 0 or ball.right >= WIDTH:
        ball_velx = ball_velx * -1
        if ball.left <= 0:
            ball.left = 0
        if ball.right >= WIDTH:
            ball.right = WIDTH
        
        score += 10
        sub = "+10! wall hit!"
        def_ = 0
        thread()

    if ball.top <= 0:
        ball_vely = ball_vely * -0.5
        ball.top = 0

        score += 10
        sub = "+10! wall hit!"
        def_ = 0
        thread()

    if ball.bottom >= HEIGHT:
        ball_vely = ball_vely * -0.9
        ball.bottom = HEIGHT
        if abs(ball_vely) > 2:
            thread()
    ball_vely += grav
    ball_velx -= ball_velx / 200
    ball.y += ball_vely
    ball.x += ball_velx

    if rect.right >= WIDTH - 10:
        rect.right = WIDTH - 10
    elif rect.left <= 10:
        rect.left = 10

    # Fill the screen with a color (clear the screen)
    screen.fill(WHITE)

    font = font_.render(f"{score}", False, defa)
    font_rect = font.get_rect(left = 5, top = 5)


    def__ = (def_, def_, def_)
    fontsub = font_sub.render(sub, False, def__)
    fontsub_rect = fontsub.get_rect(left = 5, top = 30)

    if def_ < 255:
        def_ += 5

    # Drawing (add game objects here)
    pygame.draw.rect(screen, defa, rect)
    screen.blit(font, font_rect)
    screen.blit(fontsub, fontsub_rect)
    pygame.draw.rect(screen, defa, ball)

    # Update the screen display
    pygame.display.flip()

    # Cap the frame rate (FPS)
    clock.tick(60)

