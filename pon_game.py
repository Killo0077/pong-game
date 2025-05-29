import pygame, sys

pygame.init()

# Set Up the Game Window
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLUE = (0,0,255)
RED = (255,0,0)
BLACK = (0, 0, 0)

# Add Variables to Track Score
left_score = 0
right_score = 0

font = pygame.font.Font(None, 74)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Setup the Game Clock
clock = pygame.time.Clock()
FPS = 60

# Create the Game Objects (Paddles and Ball)
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
paddle_speed = 5

left_paddle = pygame.Rect(10, HEIGHT // 2 - 50, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 50, PADDLE_WIDTH, PADDLE_HEIGHT)

BALL_SIZE = 15
ball = pygame.Rect(
    WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE
)
ball_speed_x = 4
ball_speed_y = 4

# Main Game Loop & Input Handling
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Paddle Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= paddle_speed
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += paddle_speed
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += paddle_speed

    # Move the Ball and Handle Collisions
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x *= -1

    
    if ball.left <= 0:
        right_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= -1

    if ball.right >= WIDTH:
        left_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= -1

    # Draw Everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, left_paddle)
    pygame.draw.rect(screen, BLUE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)

    screen.blit(left_text, (WIDTH // 4, 20))
    screen.blit(right_text, (WIDTH * 3 // 4, 20))

    pygame.display.flip()
    clock.tick(FPS)
