# WRITE YOUR SOLUTION HERE:


# The exercises in this part of the course have no automated tests, as the results as visually verified.
# The tests grant points automatically as you submit your solution to the server, no matter what your implementation.
# Only submit your solution when you are ready, and your solution matches the exercise description.
# The exercises may not have automatic tests, but the course staff will still see your solution.
# If your solution clearly does not match the exercise description, you may lose the points granted for the exercises in this part.

# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))

robot_width = robot.get_width()
robot_height = robot.get_height()

screen_width = window.get_width()
screen_height = window.get_height()

#center of screen
center_x = (screen_width - robot_width) / 2
center_y = (screen_height - robot_height) / 2

#center of the screen
# window.blit(robot, (center_x, center_y))

#top right
window.blit(robot, (0, 0))
#top left
window.blit(robot, (screen_width - robot_width, 0))
#bottom left
window.blit(robot, (0, screen_height - robot_height))
#bootom right
window.blit(robot, (screen_width - robot_width, screen_height - robot_height))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()