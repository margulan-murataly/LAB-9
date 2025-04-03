import pygame
import pygame.gfxdraw
from datetime import datetime

grey = (128, 128, 128)
black = (0, 0, 0)
white = (255, 255, 255)

pygame.init()

size = 500
center = (size // 2, size // 2)
window = pygame.display.set_mode((size, size))
clock = pygame.time.Clock()

def draw_hand(surface, angle, length, color, width):

    end_x = center[0] + length * pygame.math.Vector2(0, -1).rotate(angle).x
    end_y = center[1] + length * pygame.math.Vector2(0, -1).rotate(angle).y
    pygame.draw.line(surface, color, center, (end_x, end_y), width)

def draw_clock(surface):
    """Рисует часы с секундной, минутной и часовой стрелками."""
    now = datetime.now()
    
    second_angle = now.second * 6  # 360 / 60 = 6 градусов за секунду
    minute_angle = now.minute * 6 + now.second * 0.1  # 6 градусов за минуту + плавное движение
    hour_angle = (now.hour % 12) * 30 + now.minute * 0.5  # 30 градусов за час + сдвиг по минутам
    
    # Рисуем стрелки
    draw_hand(surface, hour_angle, size * 0.3, black, 8)    # Часовая стрелка
    draw_hand(surface, minute_angle, size * 0.4, grey, 5)   # Минутная стрелка
    draw_hand(surface, second_angle, size * 0.45, grey, 2)  # Секундная стрелка

def main():
    running = True
    while running:
        window.fill(white)
        draw_clock(window)
        pygame.display.flip()
        clock.tick(60)  # Обновление 60 раз в секунду

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

main()
