import pygame
import random
import sys

pygame.init()

# Configuración de la pantalla
width = 640
height = 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego de Operaciones")

# Configuración de la fuente
font = pygame.font.SysFont(None, 32)

# Función para generar una operación matemática aleatoria
def generate_operation():
    operations = ["+", "-", "*", "/"]
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(operations)
    operation_str = str(num1) + " " + operator + " " + str(num2)
    result = eval(operation_str)
    return operation_str, result

# Variables del juego
score = 0
time_left = 30000
current_operation, current_result = generate_operation()

# Crear un cuadro de entrada de texto para la respuesta del usuario
input_box = pygame.Rect(width/2 - 50, 100, 100, 50)
input_text = ""
input_active = False

# Configuración del reloj
clock = pygame.time.Clock()

# Loop principal del juego
while True:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Comprobar si la respuesta es correcta
                answer = input_text
                if answer != "":
                    if int(answer) == current_result:
                        score += 1
                    current_operation, current_result = generate_operation()
                    input_text = ""

            elif event.key == pygame.K_BACKSPACE:
                # Borrar el último carácter de la entrada
                input_text = input_text[:-1]
            else:
                # Añadir el carácter ingresado a la entrada
                input_text += event.unicode

    # Lógica del juego
    time_left -= clock.tick(60)

    # Renderizado del juego
    screen.fill((255, 255, 255))

    # Dibujar la operación actual
    operation_text = font.render(current_operation, True, (0, 0, 0))
    screen.blit(operation_text, (width/2 - operation_text.get_width()/2, 50))

    # Dibujar el cuadro de entrada de texto para la respuesta
    pygame.draw.rect(screen, (0, 0, 0), input_box, 2)
    input_text_surface = font.render(input_text, True, (0, 0, 0))
    screen.blit(input_text_surface, (input_box.x + 5, input_box.y + 5))

    # Dibujar el puntaje y el tiempo restante
    score_text = font.render("Puntaje: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    time_text = font.render("Tiempo: " + str(int(time_left/1000)), True, (0, 0, 0))
    screen.blit(time_text, (width - time_text.get_width() - 10, 10))

    pygame.display.flip()
