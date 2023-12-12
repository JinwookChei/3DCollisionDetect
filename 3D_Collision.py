import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

verticsSize = 0.5

verticies_1 = (
    (verticsSize, -verticsSize, -verticsSize),
    (verticsSize, verticsSize, -verticsSize),
    (-verticsSize, verticsSize, -verticsSize),
    (-verticsSize, -verticsSize, -verticsSize),
    (verticsSize, -verticsSize, verticsSize),
    (verticsSize, verticsSize, verticsSize),
    (-verticsSize, -verticsSize, verticsSize),
    (-verticsSize, verticsSize, verticsSize)
    )

edges_1 = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

verticies_2 = (
    (verticsSize, -verticsSize, -verticsSize),
    (verticsSize, verticsSize, -verticsSize),
    (-verticsSize, verticsSize, -verticsSize),
    (-verticsSize, -verticsSize, -verticsSize),
    (verticsSize, -verticsSize, verticsSize),
    (verticsSize, verticsSize, verticsSize),
    (-verticsSize, -verticsSize, verticsSize),
    (-verticsSize, verticsSize, verticsSize)
    )

edges_2 = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

cube1_pos = [0.0, 0.0, 0.0]
cube2_pos = [0.0, 0.0, 0.0]

# Rotation angles for Cube_1 and Cube_2
rotation_angle_1_x = 0.0
rotation_angle_1_y = 0.0 
rotation_angle_2_x = 0.0
rotation_angle_2_y = 0.0

def Cube_1():
    glPushMatrix()
    glTranslatef(cube1_pos[0], cube1_pos[1], cube1_pos[2])
    glRotatef(rotation_angle_1_x, 0, 1, 0)
    glRotatef(rotation_angle_1_y, 1, 0, 0)
    glBegin(GL_LINES)
    for edge in edges_1:
        for vertex in edge:
            glVertex3fv(verticies_1[vertex])
    glEnd()
    glPopMatrix()

def Cube_2():
    glPushMatrix()
    glTranslatef(cube2_pos[0], cube2_pos[1], cube2_pos[2])
    glRotatef(rotation_angle_2_x, 0, 1, 0)
    glRotatef(rotation_angle_2_y, 1, 0, 0)
    glBegin(GL_LINES)
    for edge in edges_2:
        for vertex in edge:
            glVertex3fv(verticies_2[vertex])
    glEnd()
    glPopMatrix()

def CollisionDetect_3D(cube1_pos, cube2_pos):
    cube1_min = [cube1_pos[0] - verticsSize, cube1_pos[1] - verticsSize, cube1_pos[2] - verticsSize]
    cube1_max = [cube1_pos[0] + verticsSize, cube1_pos[1] + verticsSize, cube1_pos[2] + verticsSize]

    cube2_min = [cube2_pos[0] - verticsSize, cube2_pos[1] - verticsSize, cube2_pos[2] - verticsSize]
    cube2_max = [cube2_pos[0] + verticsSize, cube2_pos[1] + verticsSize, cube2_pos[2] + verticsSize]

    overlap_x = cube1_min[0] <= cube2_max[0] and cube1_max[0] >= cube2_min[0]
    overlap_y = cube1_min[1] <= cube2_max[1] and cube1_max[1] >= cube2_min[1]
    overlap_z = cube1_min[2] <= cube2_max[2] and cube1_max[2] >= cube2_min[2]

    return overlap_x and overlap_y and overlap_z

def main():

    SelectOBJ = 1

    global rotation_angle_1_x, rotation_angle_1_y, rotation_angle_2_x, rotation_angle_2_y
    global cube1_pos, cube2_pos

    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    dragging = False
    start_pos = (0, 0)

    while True:
        if SelectOBJ == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    dragging = True
                    start_pos = pygame.mouse.get_pos()
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    dragging = False
                elif event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_LEFT]:
                        rotation_angle_1_x -= 10
                    elif keys[pygame.K_RIGHT]:
                        rotation_angle_1_x += 10
                    elif keys[pygame.K_UP]:
                        rotation_angle_1_y -= 10
                    elif keys[pygame.K_DOWN]:
                        rotation_angle_1_y += 10
                    elif keys[pygame.K_2]:
                        SelectOBJ = 2

        elif SelectOBJ == 2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    dragging = True
                    start_pos = pygame.mouse.get_pos()
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    dragging = False
                elif event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_LEFT]:
                        rotation_angle_2_x -= 10
                    elif keys[pygame.K_RIGHT]:
                        rotation_angle_2_x += 10
                    elif keys[pygame.K_UP]:
                        rotation_angle_2_y -= 10
                    elif keys[pygame.K_DOWN]:
                        rotation_angle_2_y += 10
                    elif keys[pygame.K_1]:
                        SelectOBJ = 1

        if dragging:
            current_pos = pygame.mouse.get_pos()
            dx = current_pos[0] - start_pos[0]
            dy = current_pos[1] - start_pos[1]

            if SelectOBJ == 1:
                cube1_pos[0] += dx / 100
                cube1_pos[1] -= dy / 100
            elif SelectOBJ == 2:
                cube2_pos[0] += dx / 100
                cube2_pos[1] -= dy / 100

            start_pos = current_pos
        
        if CollisionDetect_3D(cube1_pos, cube2_pos):
            glColor3f(1.0, 0.0, 0.0)
        else:
            glColor3f(1.0, 1.0, 1.0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube_1()
        Cube_2()
        pygame.display.flip()
        pygame.time.wait(10)

main()