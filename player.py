import pygame
from constants import *
from circleshape import CircleShape
from shot import *

class Player(CircleShape):


    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.timer -= dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if not self.timer > 0:

            forward = pygame.Vector2(0, 1).rotate(self.rotation)  # Note: changed to (0, -1) to match your triangle method
            front_point = self.position + forward * self.radius

            new_shot = Shot(front_point.x, front_point.y, SHOT_RADIUS)
            
            
            vector = pygame.Vector2(0, 1)
            rotated_vector = vector.rotate(self.rotation)

            
            new_shot.velocity = rotated_vector * PLAYER_SHOOT_SPEED

            self.timer = PLAYER_SHOOT_COOLDOWN

    

