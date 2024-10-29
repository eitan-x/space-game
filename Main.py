import pygame
import time
import random

pygame.font.init()
pygame.mixer.init()  # Initialize the mixer

# Window settings
WIDTH, HEIGHT = 1530, 780
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

# Background settings
BG = pygame.transform.scale(pygame.image.load(r"C:\Users\איתן לפאיר\Downloads\Designer (1).jpeg"), (WIDTH, HEIGHT))
pygame.mixer.music.load(r"C:\Users\איתן לפאיר\AppData\Local\Google\Chrome\User Data\Default\Extensions\mjjgmlmpeaikcaajghilhnioimmaibon\2.2.7_0\mp3\theme.mp3")
pygame.mixer.music.play(-1)  # Loop the background music

# Size and speed settings
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5

STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

BULLET_WIDTH = 5
BULLET_HEIGHT = 10
BULLET_VEL = 10

FONT = pygame.font.SysFont("comicsans", 30)

# Initialize game variables
level = 1
power_up_active = False
power_up_time = 0

def draw(player, stars, bullets, elapsed_time, hits, level):
    WIN.blit(BG, (0, 0))

    # Display time
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    # Display hits
    hits_text = FONT.render(f"Hits: {hits}", 1, "white")
    WIN.blit(hits_text, (10, 40))

    # Display level
    level_text = FONT.render(f"Level: {level}", 1, "white")
    WIN.blit(level_text, (10, 70))

    # Draw player
    pygame.draw.rect(WIN, "red", player)

    # Draw stars (enemies)
    for star in stars:
        pygame.draw.rect(WIN, "white", star)
    for bullet in bullets:
        pygame.draw.rect(WIN, "blue", bullet)

    pygame.display.update()

def move_towards_player(star, player):
    if star.x < player.x:
        star.x += 1
    elif star.x > player.x:
        star.x -= 1

def dodge_bullet(star, bullets):
    for bullet in bullets:
        if bullet.colliderect(star):
            if bullet.y < star.y:  # If the bullet is above the enemy
                star.y += 5  # Move the enemy down to avoid the bullet

def enemy_shoot(star, player, enemy_bullets):
    if random.randint(1, 100) < 5:  # 5% chance to shoot
        bullet = pygame.Rect(star.x + STAR_WIDTH // 2 - BULLET_WIDTH // 2, star.y + STAR_HEIGHT, BULLET_WIDTH, BULLET_HEIGHT)
        enemy_bullets.append(bullet)

def main():
    global level, power_up_active, power_up_time
    run = True
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()

    start_time = time.time()
    elapsed_time = 0
    hits = 0

    stars = []  # List of enemies
    bullets = []  # List of player bullets
    enemy_bullets = []  # List of enemy bullets

    star_add_increment = 2000  # Time interval to add new stars
    star_count = 0

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        # Add new enemies at intervals
        if star_count > star_add_increment:
            for _ in range(level + 2):  # Increase number of enemies with level
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
            star_add_increment = max(500, star_add_increment - 50)  # Decrease time interval as the game progresses
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH:
            player.x += PLAYER_VEL
        if keys[pygame.K_UP] and player.y - PLAYER_VEL >= 0:
            player.y -= PLAYER_VEL
        if keys[pygame.K_DOWN] and player.y + PLAYER_VEL + PLAYER_HEIGHT <= HEIGHT:
            player.y += PLAYER_VEL

        # Shooting bullets
        if keys[pygame.K_SPACE]:
            bullet = pygame.Rect(player.x + PLAYER_WIDTH // 2 - BULLET_WIDTH // 2, player.y, BULLET_WIDTH, BULLET_HEIGHT)
            bullets.append(bullet)

        # Power-up activation
        if keys[pygame.K_p] and time.time() - power_up_time > 30:
            power_up_active = True
            power_up_time = time.time()

        # Manage bullets
        for bullet in bullets[:]:
            bullet.y -= BULLET_VEL
            if bullet.y < 0:
                bullets.remove(bullet)

        # AI behavior: move, dodge, and shoot
        stars_to_remove = []  # Temporary list to remove enemies
        bullets_to_remove = []  # Temporary list to remove bullets

        for star in stars[:]:
            move_towards_player(star, player)
            dodge_bullet(star, bullets)
            enemy_shoot(star, player, enemy_bullets)

            star.y += STAR_VEL
            if star.colliderect(player):
                run = False  # Player got hit
            if star.y > HEIGHT:  # If the enemy goes off screen
                stars_to_remove.append(star)  # Add to temporary list

        # Remove enemies from the screen
        for star in stars_to_remove:
            if star in stars:  # Ensure the star is still in the list before removal
                stars.remove(star)

        # Bullet collisions with enemies
        for star in stars[:]:
            for bullet in bullets[:]:
                if bullet.colliderect(star):
                    if star in stars:  # Ensure the star is still in the list before removal
                        stars_to_remove.append(star)  # Add to temporary list
                    if bullet in bullets:  # Ensure the bullet is still in the list before removal
                        bullets_to_remove.append(bullet)  # Add to temporary list

        # Remove bullets and enemies
        for bullet in bullets_to_remove:
            if bullet in bullets:  # Ensure the bullet is still in the list before removal
                bullets.remove(bullet)

        for star in stars_to_remove:
            if star in stars:  # Ensure the star is still in the list before removal
                stars.remove(star)

        # Level up condition
        if hits >= level * 5:  # Increase level every 5 hits
            level += 1

        draw(player, stars, bullets, elapsed_time, hits, level)  # Draw everything on the screen

    pygame.quit()

if __name__ == "__main__":
    main()
