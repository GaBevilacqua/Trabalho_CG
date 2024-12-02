import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def draw_half_sphere_upper(radius, slices, stacks, position):
    """
    Renderiza uma esfera cortada ao meio, mostrando a metade superior.
    :param radius: Raio da esfera.
    :param slices: Número de fatias longitudinais.
    :param stacks: Número de fatias latitudinais.
    :param position: Posição da esfera (x, y, z).
    """
    glPushMatrix()
    glTranslatef(position[0], position[1], position[2])
    quadric = gluNewQuadric()
    
    # Desenhando a metade superior
    for stack in range(stacks // 2):  # Apenas a parte superior da esfera
        latitude1 = (stack / stacks) * (math.pi / 2)  # De 0 a pi/2
        latitude2 = ((stack + 1) / stacks) * (math.pi / 2)
        sin_lat1, cos_lat1 = math.sin(latitude1), math.cos(latitude1)
        sin_lat2, cos_lat2 = math.sin(latitude2), math.cos(latitude2)

        glBegin(GL_QUAD_STRIP)
        for slice_ in range(slices + 1):
            longitude = (slice_ / slices) * (2 * math.pi)
            sin_long, cos_long = math.sin(longitude), math.cos(longitude)

            x1, y1, z1 = cos_long * sin_lat1, cos_lat1, sin_long * sin_lat1
            x2, y2, z2 = cos_long * sin_lat2, cos_lat2, sin_long * sin_lat2

            glVertex3f(x1 * radius, y1 * radius, z1 * radius)
            glVertex3f(x2 * radius, y2 * radius, z2 * radius)
        glEnd()

    gluDeleteQuadric(quadric)
    glPopMatrix()

def draw_half_sphere_lower(radius, slices, stacks, position):
    """
    Renderiza uma esfera cortada ao meio, mostrando a metade inferior.
    :param radius: Raio da esfera.
    :param slices: Número de fatias longitudinais.
    :param stacks: Número de fatias latitudinais.
    :param position: Posição da esfera (x, y, z).
    """
    glPushMatrix()
    glTranslatef(position[0], position[1], position[2])
    quadric = gluNewQuadric()
    
    # Desenhando a metade inferior
    for stack in range(stacks // 2, stacks):  # Apenas a parte inferior da esfera
        latitude1 = (stack / stacks) * math.pi  # De pi/2 até pi
        latitude2 = ((stack + 1) / stacks) * math.pi
        sin_lat1, cos_lat1 = math.sin(latitude1), math.cos(latitude1)
        sin_lat2, cos_lat2 = math.sin(latitude2), math.cos(latitude2)

        glBegin(GL_QUAD_STRIP)
        for slice_ in range(slices + 1):
            longitude = (slice_ / slices) * (2 * math.pi)
            sin_long, cos_long = math.sin(longitude), math.cos(longitude)

            x1, y1, z1 = cos_long * sin_lat1, cos_lat1, sin_long * sin_lat1
            x2, y2, z2 = cos_long * sin_lat2, cos_lat2, sin_long * sin_lat2

            glVertex3f(x1 * radius, y1 * radius, z1 * radius)
            glVertex3f(x2 * radius, y2 * radius, z2 * radius)
        glEnd()

    gluDeleteQuadric(quadric)
    glPopMatrix()

def draw_rectangle(width, height, depth, position):
    """
    Desenha um retângulo 3D (paralelogramo) entre as esferas.
    :param width: Largura do retângulo.
    :param height: Altura do retângulo.
    :param depth: Profundidade do retângulo.
    :param position: Posição do retângulo (x, y, z).
    """
    glPushMatrix()
    glTranslatef(position[0], position[1], position[2])

    # Retângulo (Cubo) branco
    glBegin(GL_QUADS)

    # Frente
    glVertex3f(-width / 2, -height / 2, -depth / 2)
    glVertex3f(width / 2, -height / 2, -depth / 2)
    glVertex3f(width / 2, height / 2, -depth / 2)
    glVertex3f(-width / 2, height / 2, -depth / 2)

    # Trás
    glVertex3f(-width / 2, -height / 2, depth / 2)
    glVertex3f(width / 2, -height / 2, depth / 2)
    glVertex3f(width / 2, height / 2, depth / 2)
    glVertex3f(-width / 2, height / 2, depth / 2)

    # Lados
    glVertex3f(-width / 2, -height / 2, -depth / 2)
    glVertex3f(-width / 2, height / 2, -depth / 2)
    glVertex3f(-width / 2, height / 2, depth / 2)
    glVertex3f(-width / 2, -height / 2, depth / 2)

    glVertex3f(width / 2, -height / 2, -depth / 2)
    glVertex3f(width / 2, height / 2, -depth / 2)
    glVertex3f(width / 2, height / 2, depth / 2)
    glVertex3f(width / 2, -height / 2, depth / 2)

    # Cima e baixo
    glVertex3f(-width / 2, height / 2, -depth / 2)
    glVertex3f(width / 2, height / 2, -depth / 2)
    glVertex3f(width / 2, height / 2, depth / 2)
    glVertex3f(-width / 2, height / 2, depth / 2)

    glVertex3f(-width / 2, -height / 2, -depth / 2)
    glVertex3f(width / 2, -height / 2, -depth / 2)
    glVertex3f(width / 2, -height / 2, depth / 2)
    glVertex3f(-width / 2, -height / 2, depth / 2)

    glEnd()

    glPopMatrix()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)

    glEnable(GL_DEPTH_TEST)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Definir a cor branca para as esferas e retângulos
        glColor3f(1.0, 1.0, 1.0)

        # Desenhar as esferas
        draw_half_sphere_upper(radius=2, slices=30, stacks=30, position=(-3, 0, 0))  # Metade superior à esquerda
        draw_half_sphere_lower(radius=2, slices=30, stacks=30, position=(3, 0, 0))  # Metade inferior à direita

        # Desenhar os retângulos
        draw_rectangle(width=1, height=4, depth=1, position=(0, 0, 0))  # Retângulo no meio

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
