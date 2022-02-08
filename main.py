import random
import pygame

WIDTH = 600
HEIGHT = 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
SNAKE_BLOCK = 10
SNAKE_SPEED = 30
FONT_SIZE = 30


def message(msg, color):
    text = font_style.render(msg, True, color)
    scene.blit(text, [(WIDTH / 2) - FONT_SIZE, (HEIGHT / 2) - FONT_SIZE])


def game_loop():
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    food_x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0

    while not game_over:

        while game_close:
            scene.fill(BLACK)
            message("You Lost! Press Q-Quit or C-Play Again", WHITE)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -SNAKE_BLOCK
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = SNAKE_BLOCK

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change

        scene.fill(BLACK)

        pygame.draw.rect(scene, WHITE, [x1, y1, SNAKE_BLOCK, SNAKE_BLOCK])
        pygame.draw.rect(scene, BLUE, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])
        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            print("Yummy!")

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()


if __name__ == '__main__':
    pygame.init()
    scene = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake game by reberu')

    clock = pygame.time.Clock()

    font_style = pygame.font.SysFont(None, FONT_SIZE)

    game_loop()
