# WRITE YOUR SOLUTION HERE:

# WRITE YOUR SOLUTION HERE:



# The exercises in this part of the course have no automated tests, as the results as visually verified.
# The tests grant points automatically as you submit your solution to the server, no matter what your implementation.
# Only submit your solution when you are ready, and your solution matches the exercise description.
# The exercises may not have automatic tests, but the course staff will still see your solution.
# If your solution clearly does not match the exercise description, you may lose the points granted for the exercises in this part.

# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
window = pygame.display.set_mode((740, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))

robot_width = robot.get_width()
robot_height = robot.get_height()

screen_width = window.get_width()
screen_height = window.get_height()

x_step = 0
y_step = -70
row = 10
col = 10
offset = 5

print(f'Robot size: ({robot_width}, {robot_height})')

start_x = (screen_width - ((robot_width + x_step) * row)) / 2
start_y = (screen_height - ((robot_height + y_step) * col)) / 2

positions = [
    (start_x + (offset * y) + (robot_width + x_step) * x, (start_y + (robot_height + y_step) * y))
     for x in range(row)
     for y in range(col)
    ]

print(positions)

for pos in positions:
    window.blit(robot, pos)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()