import tkinter as tk
import neat
import random
import pygame
import time

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('4-Lane Traffic Management')

CARS = []
TRAFFIC_LIGHTS = {'NORTH_SOUTH': {'color': RED, 'pos': (300, 50)}, 'EAST_WEST': {'color': RED, 'pos': (450, 50)}}

class Car:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.width = 40
        self.height = 20
        self.speed = random.randint(3, 5)

    def move(self):
        if self.direction == 'NORTH_SOUTH':
            self.y -= self.speed
        elif self.direction == 'EAST_WEST':
            self.x += self.speed

    def draw(self):
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.width, self.height))

def generate_cars():
    direction = random.choice(['NORTH_SOUTH', 'EAST_WEST'])
    if direction == 'NORTH_SOUTH':
        car = Car(random.randint(200, 600), 600, 'NORTH_SOUTH')
    else:
        car = Car(0, random.randint(100, 500), 'EAST_WEST')
    CARS.append(car)

def change_traffic_light(light):
    if light == 'NORTH_SOUTH':
        if TRAFFIC_LIGHTS['NORTH_SOUTH']['color'] == RED:
            TRAFFIC_LIGHTS['NORTH_SOUTH']['color'] = GREEN
            TRAFFIC_LIGHTS['EAST_WEST']['color'] = RED
        else:
            TRAFFIC_LIGHTS['NORTH_SOUTH']['color'] = RED
            TRAFFIC_LIGHTS['EAST_WEST']['color'] = GREEN
    elif light == 'EAST_WEST':
        if TRAFFIC_LIGHTS['EAST_WEST']['color'] == RED:
            TRAFFIC_LIGHTS['EAST_WEST']['color'] = GREEN
            TRAFFIC_LIGHTS['NORTH_SOUTH']['color'] = RED
        else:
            TRAFFIC_LIGHTS['EAST_WEST']['color'] = RED
            TRAFFIC_LIGHTS['NORTH_SOUTH']['color'] = GREEN

def fitness_function(genome, config):
    net = neat.nn.FeedForwardNetwork.create(genome, config)

    traffic_data = [random.randint(0, 100) for _ in range(4)]
    output = net.activate(traffic_data)

    green_time = [o * 60 for o in output]
    total_wait_time = sum(green_time)
    return -total_wait_time

def run_neat():
    config_path = "D:\\KUSHAGRA\\DATA\\K_Works\\ML AI TMS\\mixed\\config-neat.txt"
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    population = neat.Population(config)
    population.add_reporter(neat.reporting.StdOutReporter(True))
    population.add_reporter(neat.reporting.StatisticsReporter())

    population.run(fitness_function, 300)

def main_gui():
    root = tk.Tk()
    root.title("Traffic Management System")
    
    def start_simulation():
        run_neat()
        for _ in range(50):
            generate_cars()
        root.after(100, update_simulation)

    def update_simulation():
        screen.fill(WHITE)

        for car in CARS:
            car.move()
            car.draw()

        for light in TRAFFIC_LIGHTS.values():
            pygame.draw.circle(screen, light['color'], light['pos'], 20)

        pygame.display.flip()
        time.sleep(0.1)

        root.after(100, update_simulation)

    start_button = tk.Button(root, text="Start Simulation", command=start_simulation)
    start_button.pack()

    quit_button = tk.Button(root, text="Quit", command=root.quit)
    quit_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main_gui()
