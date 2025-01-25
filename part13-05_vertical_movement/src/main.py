import pygame
from random import randint

# Constants
WINDOW_WIDTH = 740
WINDOW_HEIGHT = 480
BG_COLOR = (0, 0, 0)
NUM_ROBOTS = 1000

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Random Robots")

# Load robot image
try:
    robot = pygame.image.load("robot.png")
except pygame.error as e:
    print(f"Unable to load image: {e}")
    pygame.quit()
    exit()

# Generate positions
def generate_positions(num, width, height, image):
    img_width, img_height = image.get_size()
    return [(randint(0, width - img_width), randint(0, height - img_height)) for _ in range(num)]

positions = generate_positions(NUM_ROBOTS, WINDOW_WIDTH, WINDOW_HEIGHT, robot)

# Draw everything
window.fill(BG_COLOR)
for pos in positions:
    window.blit(robot, pos)

pygame.display.flip()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    positions = generate_positions(NUM_ROBOTS, WINDOW_WIDTH, WINDOW_HEIGHT, robot)
    for pos in positions:
        window.blit(robot, pos)
    window.fill(BG_COLOR)