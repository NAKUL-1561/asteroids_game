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
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots,updatable,drawable)
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable,)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    score = 0
    lives = PLAYER_LIVES
    font = pygame.font.Font(None, 32)

    dt = 0

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        screen.fill("black")

        for asteroid in list(asteroids):
            for shot in list(shots):
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    points = int(ASTEROID_BASE_SCORE * (ASTEROID_MAX_RADIUS / asteroid.radius))
                    score += points
                    asteroid.split()

            if player.collides_with(asteroid) and player.invulnerable_timer <= 0:
                log_event("player_hit")
                lives -= 1
                asteroid.kill()
                if lives <= 0:
                    print(f"Game Over! Final score: {score}")
                    sys.exit()
                player.reset(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                break

        for obj in drawable:
            obj.draw(screen)

        score_surface = font.render(f"Score: {score}", True, "white")
        lives_surface = font.render(f"Lives: {lives}", True, "white")
        screen.blit(score_surface, (16, 16))
        screen.blit(lives_surface, (16, 48))

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
