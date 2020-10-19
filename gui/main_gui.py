import sys
import pygame
from basic_inserts import insert_rows

def main():
    #icon = pygame.image.load("C:\\Users\\Nikita\\Pictures\\drx.png")

    res = (720,720)
    background = (40, 44, 52)
    pygame.init()
    screen = pygame.display.set_mode(res)

    pygame.display.set_caption("Practica Vara")
    # pygame.display.set_icon(icon)

    button = pygame.Rect(100, 100, 50, 50)



    while True:
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if button.collidepoint(mouse_pos):
                    insert_rows()

        screen.fill(background)

        pygame.draw.rect(screen,[255, 0, 0], button)

        pygame.display.update()

if __name__ == '__main__':
    main()