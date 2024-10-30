import pygame
import time
import random
import sys
import customtkinter as ctk
import os

# Initialize pygame and fonts
pygame.font.init()
pygame.mixer.init()

# Window settings
WIDTH, HEIGHT = 1530, 780
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

# Background settings
BG = pygame.transform.scale(
    pygame.image.load("bg.jpeg"),
    (WIDTH, HEIGHT)
)
pygame.mixer.music.load("theme.mp3")
pygame.mixer.music.play(-1)

PLAYER_VEL = 5
BULLET_VEL = 10
FONT = pygame.font.SysFont("comicsans", 30)

# Load images
PLAYER_IMG = pygame.image.load("player.png")
PLAYER_IMG = pygame.transform.scale(PLAYER_IMG, (60, 60))

ENEMY_IMG = pygame.image.load("enemy.png")
ENEMY_IMG = pygame.transform.scale(ENEMY_IMG, (40, 40))

BULLET_IMG = pygame.image.load("bullet.png")
BULLET_IMG = pygame.transform.scale(BULLET_IMG, (20, 40))

SPECIAL_POWER_COST = 10

def draw(player, stars, bullets, elapsed_time, hits, level, coins):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    hits_text = FONT.render(f"Hits: {hits}", 1, "white")
    WIN.blit(hits_text, (10, 40))

    level_text = FONT.render(f"Level: {level}", 1, "white")
    WIN.blit(level_text, (10, 70))

    coins_text = FONT.render(f"Coins: {coins}", 1, "yellow")
    WIN.blit(coins_text, (10, 100))

    WIN.blit(PLAYER_IMG, (player.x, player.y))

    for star in stars:
        WIN.blit(ENEMY_IMG, (star.x, star.y))

    for bullet in bullets:
        WIN.blit(BULLET_IMG, (bullet.x, bullet.y))

    pygame.display.update()

def start_game(level):
    """Start the main game with the selected level."""
    main(level)

def create_level_selector():
    """Create a level selector window."""
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("Select Level")
    root.geometry("400x300")

    label = ctk.CTkLabel(root, text="Choose your starting level:", font=("Arial", 20))
    label.pack(pady=20)

    # Create buttons for levels
    for level in range(1, 6):  # Levels 1 to 5
        button = ctk.CTkButton(
            root, text=f"Level {level}",
            command=lambda lvl=level: [root.destroy(), start_game(lvl)]  # Close selector and start game
        )
        button.pack(pady=10)

    root.mainloop()

def main(level):
    star_vel = 2 + level  # Adjust enemy speed based on the level

    run = True
    player = pygame.Rect(200, HEIGHT - 60, 60, 60)
    clock = pygame.time.Clock()

    start_time = time.time()
    elapsed_time = 0
    hits = 0
    coins = 0
    star_add_increment = max(2000 - level * 300, 500)
    star_count = 0

    stars = []
    bullets = []

    last_shot_time = 0

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - 40)
                star = pygame.Rect(star_x, -40, 40, 40)
                stars.append(star)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        if keys[pygame.K_UP] and player.y - PLAYER_VEL >= 0:
            player.y -= PLAYER_VEL
        if keys[pygame.K_DOWN] and player.y + PLAYER_VEL + player.height <= HEIGHT:
            player.y += PLAYER_VEL

        if keys[pygame.K_SPACE] and time.time() - last_shot_time > 0.3:
            bullet = pygame.Rect(player.x + player.width // 2 - 10, player.y, 20, 40)
            bullets.append(bullet)
            last_shot_time = time.time()

        if keys[pygame.K_p] and coins >= SPECIAL_POWER_COST:
            coins -= SPECIAL_POWER_COST
            stars.clear()

        for bullet in bullets[:]:
            bullet.y -= BULLET_VEL
            if bullet.y < 0:
                bullets.remove(bullet)

        for star in stars[:]:
            star.y += star_vel
            if star.colliderect(player):
                run = False

            if star.y > HEIGHT:
                stars.remove(star)

        for star in stars[:]:
            for bullet in bullets[:]:
                if bullet.colliderect(star):
                    stars.remove(star)
                    bullets.remove(bullet)
                    hits += 1
                    coins += 1

        draw(player, stars, bullets, elapsed_time, hits, level, coins)

    pygame.quit()

if __name__ == "__main__":
    create_level_selector()
