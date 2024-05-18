import pygame
import random

# Инициализация pygame
pygame.init()

# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
DOOR_WIDTH = 150
DOOR_HEIGHT = 300
STATUS_BAR_HEIGHT = 50

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Настройка окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + STATUS_BAR_HEIGHT))
pygame.display.set_caption("Игра: Приведение Монти Холла")

font = pygame.font.Font(None, 36)

def load_image(path, width, height):
    image = pygame.image.load(path)
    return pygame.transform.scale(image, (width, height))

def draw_text(text, x, y, color=BLACK):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def draw_button(text, x, y, w, h, color, action=None):
    pygame.draw.rect(screen, color, (x, y, w, h))
    draw_text(text, x + 10, y + 10)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if click[0] == 1 and action is not None:
            action()

def main():
    running = True
    current_room = 1
    ghost_door = random.randint(1, 3)
    game_over = False

    # Загрузка и масштабирование изображений
    door_image = load_image('door.png', DOOR_WIDTH, DOOR_HEIGHT)
    ghost_image = load_image('ghost.png', DOOR_WIDTH, DOOR_HEIGHT)

    def restart_game():
        nonlocal game_over, current_room, ghost_door
        game_over = False
        current_room = 1
        ghost_door = random.randint(1, 3)

    def quit_game():
        nonlocal running
        running = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                if 150 <= x <= 300 and 150 <= y <= 450:
                    choice = 1
                elif 325 <= x <= 475 and 150 <= y <= 450:
                    choice = 2
                elif 500 <= x <= 650 and 150 <= y <= 450:
                    choice = 3
                else:
                    continue

                if choice == ghost_door:
                    game_over = True
                else:
                    current_room += 1
                    ghost_door = random.randint(1, 3)

        screen.fill(WHITE)

        # Отрисовка статус-бара
        pygame.draw.rect(screen, BLACK, (0, SCREEN_HEIGHT, SCREEN_WIDTH, STATUS_BAR_HEIGHT))  # Контур статус-бара
        fill_width = (current_room / 10) * SCREEN_WIDTH  # Ширина заполнения статус-бара в зависимости от текущей комнаты
        pygame.draw.rect(screen, GREEN, (0, SCREEN_HEIGHT, fill_width, STATUS_BAR_HEIGHT))  # Заполнение статус-бара
        draw_text(f"Текущая комната: {current_room}", 10, SCREEN_HEIGHT + 10, color=WHITE)

        if game_over:
            draw_text(f"Вы выбрали дверь с привидением! Игра закончена.", 150, 50)
            draw_text(f"Вы дошли до комнаты {current_room}.", 300, 100)
            draw_text("Нажмите на кнопку для новой игры или выхода.", 150, 150)
            ghost_position = ((SCREEN_WIDTH - DOOR_WIDTH) // 2, (SCREEN_HEIGHT - DOOR_HEIGHT) // 2 + 50)
            screen.blit(ghost_image, ghost_position)
            draw_button("Restart", 200, 500, 100, 50, GREEN, restart_game)
            draw_button("Quit", 500, 500, 100, 50, RED, quit_game)
        else:
            draw_text(f"Выберите дверь:", 150, 50)
            screen.blit(door_image, (150, 150))
            screen.blit(door_image, (325, 150))
            screen.blit(door_image, (500, 150))

        pygame.display.flip()
        pygame.time.delay(100)

    pygame.quit()

if __name__ == "__main__":
    main()