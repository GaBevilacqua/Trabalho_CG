import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Variáveis globais para o movimento do triângulo
pos_x = 0.0
pos_y = 0.0
angle = 0.0  # Ângulo inicial
angular_speed = 0.01  # Velocidade angular (ajuste conforme necessário)
radius = 1.5  # Raio do círculo

def inicializar():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Define a cor de fundo (preto)
    glEnable(GL_DEPTH_TEST)  # Habilita o teste de profundidade

def desenhar():
    global pos_x, pos_y, angle  # Agora usamos angle como variável global

    # Atualiza o ângulo continuamente
    angle += angular_speed

    # Calcula a posição usando seno e cosseno
    pos_x = radius * math.cos(angle)
    pos_y = radius * math.sin(angle)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Limpa o buffer de cor e profundidade
    glLoadIdentity()  # Reseta a matriz
    glTranslatef(pos_x, pos_y, -5.0)  # Move o triângulo para a nova posição

    # Desenha um triângulo
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 1.0, 0.0) 
    glVertex3f(0.0, 1.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)  
    glVertex3f(-1.0, -1.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(1.0, -1.0, 0.0)
    glEnd()

    pygame.display.flip()  # Atualiza a tela
    pygame.time.wait(10)  # Espera um pouco para limitar a taxa de quadros

def main():
    # Inicializa o pygame e configura a janela
    pygame.init()
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Triângulo Quicando com OpenGL e Pygame")

    # Configura a perspectiva
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (800 / 600), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    inicializar()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        desenhar()

    pygame.quit()  

if __name__ == "__main__":
    main()
