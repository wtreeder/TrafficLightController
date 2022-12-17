import pygame

import src.controllers.constants as c


class Vehicle:
    def __init__(self, vehicle_type: c.VehicleType, direction: c.Direction, lane: c.Lane,
                 turn: c.Turn):
        self.vehicle_type = vehicle_type
        self.direction = direction
        self.lane = lane
        self.turn = turn

        self.x = c.x_vehicle[direction.value][lane.value]
        self.y = c.y_vehicle[direction.value][lane.value]
        self.angle = c.rotation[direction.value]
        self.speed = c.speeds[vehicle_type.value]
        self.stop = c.default_stop[direction.value]

        self.is_stopped = False
        self.is_through = False
        self.is_turned = False
        self.wait_time = 0

        path = '../images/' + str(vehicle_type.value) + '.png'
        image = pygame.image.load(path)
        self.image = pygame.transform.rotate(image, self.angle)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        if direction == c.Direction.EAST:
            self.x -= self.width + c.stoppingGap
        elif direction == c.Direction.SOUTH:
            self.y -= self.height + c.stoppingGap
        elif direction == c.Direction.WEST:
            self.x += c.stoppingGap
        elif direction == c.Direction.NORTH:
            self.y += c.stoppingGap





v = Vehicle(c.VehicleType.RED_CAR, c.Direction.WEST, c.Lane.RIGHT, c.Turn.RIGHT)
print(v.width)
print(v.height)
print(v.x)
print(v.y)
