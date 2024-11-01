import sys, pygame
pygame.init()

# Window Size
size = width, height = 1600, 800

# This actually indicates where the ball should move in one iteration
speed = [1, 1]
background = 25, 25, 25
# Set size
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bouncing Ball")
ball = pygame.image.load("redball.png")
# Turn the image into a rectangle in PyGame
ball_rect = ball.get_rect()
# Set up the clock
clock = pygame.time.Clock()  # Create a clock object
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    # Each time, the ball will move according to speed [x, y]
    ball_rect = ball_rect.move(speed)
    # Bounce Effect
    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = -speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > height:
        speed[1] = -speed[1]
    # Fill screen with white background
    screen.fill(background)
    screen.blit(ball, ball_rect)
    #Update display
    pygame.display.flip()

    # Slow down the game to 60 frames per second
    clock.tick(120)  # Set the frame rate to 60 FPS