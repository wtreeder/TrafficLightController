# Import packages
import random
import sys
from threading import Thread
import time

import pygame

from controllers.traffic_light import TrafficLightController
from controllers.vehicle import Vehicle
import controllers.constants as c

vehicles = []


def generate_vehicles(tlc: TrafficLightController):
    i = 0
    while True:
        vehicle_type = random.choice(list(c.VehicleType))
        direction = random.choice(list(c.Direction))
        lane = random.choice(list(c.Lane))
        if lane == c.Lane.LEFT:
            turn = c.Turn.LEFT
        elif lane == c.Lane.MIDDLE:
            turn = c.Turn.STRAIGHT
        else:
            turn = random.choice([c.Turn.STRAIGHT, c.Turn.RIGHT])
        tlc.add_vehicle(Vehicle(vehicle_type, direction, lane, turn))
        time.sleep(1)
        i += 1


def update_signals(tlc: TrafficLightController):
    while True:
        tlc.update_signals()


class Main:
    # Initialize pygame
    pygame.init()

    # Set window size and caption
    screen_size = (screen_width, screen_height) = 821, 821
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Traffic Light Simulation')

    # Clock
    clock = pygame.time.Clock()

    # Load background
    background = pygame.image.load('../images/intersection.png')

    # Instantiate traffic light controller and start thread to update signals
    tlc = TrafficLightController()
    update_signals = Thread(target=update_signals, args=(tlc,))
    update_signals.daemon = True
    update_signals.start()

    # Start thread to generate vehicles
    generate_vehicles = Thread(target=generate_vehicles, args=(tlc,))
    generate_vehicles.daemon = True
    generate_vehicles.start()

    while True:
        # Exits program if window is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Render background
        screen.blit(background, (0, 0))

        # Render vehicles
        for direction in tlc.vehicles:
            for turn in tlc.vehicles[direction]:
                for vehicle in tlc.vehicles[direction][turn]:
                    screen.blit(vehicle.image, (vehicle.x, vehicle.y))

        # Render traffic signals
        for direction in tlc.signals:
            for lane in tlc.signals[direction]:
                signal = tlc.signals[direction][lane]
                screen.blit(signal.image, (signal.x, signal.y))

        tlc.update_vehicles()

        pygame.display.update()


Main()
