import pygame
import sys


class MainScreen:

    def __init__(self, res_width, res_height):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Lights Out!')
        window = pygame.display.set_mode([res_width, res_height])
        width_mid = (res_width / 2)
        height_mid = (res_height / 2)

        input_box = pygame.Rect(0, 0, 200, 32)
        input_box.center = (width_mid, height_mid)

        base_font = pygame.font.SysFont("monospace", 22)
        label_font = pygame.font.SysFont("monospace", 18)
        user_text = ''

        input_color_active = pygame.Color((207, 168, 98))
        input_color_passive = pygame.Color((231, 192, 122))

        active = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = True
                    else:
                        active = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode

            window.fill((255, 215, 145))

            if active:
                color = input_color_active
            else:
                color = input_color_passive

            label = label_font.render("Ingrese el tamaño del tablero:", True, (255, 255, 255))
            label_box = label.get_rect()
            label_box.center = (width_mid, height_mid - 40)
            window.blit(label, label_box)

            pygame.draw.rect(window, color, input_box)
            text_surface = base_font.render(user_text, True, (255, 255, 255))

            window.blit(text_surface, (input_box.x + 5, input_box.y + 5))
            # input_box.w = max(100, text_surface.get_width() + 10)

            pygame.display.flip()

            clock.tick(60)
