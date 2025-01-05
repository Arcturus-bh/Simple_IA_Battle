import pygame
import math


class Entity:
    def __init__(self, entity_type, color, width, height):
        self.type = entity_type
        self.entity_color = color
        self.rect = pygame.Rect(self.load_entity_rectangle(width, height))
        self.base_speed = 10
        self.max_speed = self.base_speed * 5
        self.current_speed = self.base_speed
        self.acceleration = (50/100) * self.base_speed
        self.previous_angle = None

    def load_entity_rectangle(self, width, height):
        new_width = width * 0.05
        new_height = height * 0.05
        x_offset = (width - new_width) / 2
        y_offset = (height - new_height) / 2
        return int(x_offset), int(y_offset), int(new_width), int(new_height)

    def convert_to_degrees(self, radiant):
        print(f"previous angle: {int(radiant * (180 / math.pi))}°")

    def move(self, limits, new_angle, delta_time):
        move_x = math.cos(new_angle) * self.current_speed * delta_time
        move_y = math.sin(new_angle) * self.current_speed * delta_time

        new_x = self.rect.x + move_x
        new_y = self.rect.y + move_y
        self.rect.x = int(
            max(limits['x_offset'], min(limits['x_offset'] + limits['width'] - self.rect.width, new_x)))
        self.rect.y = int(
            max(limits['y_offset'], min(limits['y_offset'] + limits['height'] - self.rect.height, new_y)))
        self.previous_angle = new_angle
        self.convert_to_degrees(new_angle)   # debug

    def check_move(self, keys, delta_time, limits):
        dx, dy = 0, 0
        if keys[pygame.K_UP] or keys[pygame.K_z]: dy -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]: dy += 1
        if keys[pygame.K_LEFT] or keys[pygame.K_q]: dx -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: dx += 1

        # Si une direction est valide
        if dx != 0 or dy != 0:
            new_angle = math.atan2(dy, dx)  # Trouve l'angle de direction
            if self.previous_angle is None or abs(new_angle - self.previous_angle) < float(0.01):
                self.current_speed += self.acceleration * delta_time
                self.current_speed = min(self.current_speed, self.max_speed)
            else:
                self.current_speed -= self.acceleration * delta_time
                self.current_speed = max(self.current_speed, self.base_speed)
            self.move(limits, new_angle, delta_time)

