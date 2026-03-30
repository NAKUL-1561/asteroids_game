import sys, pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot
from constants import *
from logger import log_state, log_event



def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 30)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    lives = STARTING_LIVES
    score = 0
    player_alive = True
    respawn_timer = 0.0

    dt = 0

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        if player_alive:
            player.update(dt)
        else:
            respawn_timer -= dt
            if respawn_timer <= 0:
                player.respawn(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                player_alive = True

        asteroid_field.update(dt)
        asteroids.update(dt)
        shots.update(dt)

        screen.fill("black")

        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
                    score += SCORE_PER_ASTEROID

            if player_alive and player.collides_with(asteroid):
                log_event("player_hit")
                lives -= 1
                player_alive = False
                respawn_timer = RESPAWN_SECONDS
                if lives <= 0:
                    print("Game Over! Final score:", score)
                    sys.exit()

        for obj in drawable:
            if obj is player and not player_alive:
                continue
            obj.draw(screen)

        # HUD
        score_text = font.render(f"Score: {score}", True, "white")
        lives_text = font.render(f"Lives: {lives}", True, "white")
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 40))

        if not player_alive:
            countdown_text = font.render(f"Respawning in {respawn_timer:.1f}s", True, "yellow")
            screen.blit(countdown_text, (10, 70))

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
