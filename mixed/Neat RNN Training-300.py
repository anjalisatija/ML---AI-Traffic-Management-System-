import neat
import torch
import sys

def fitness_function(genome, config):
    net = neat.nn.FeedForwardNetwork.create(genome, config)

    traffic_data = [
        [10, 15, 20, 12],
        [12, 18, 17, 14],
        [10, 16, 14, 13],
        [13, 11, 15, 10]
    ]

    total_wait_time = 0
    for data in traffic_data:
        output = net.activate(data)
        green_time = [o * 60 for o in output]
        total_wait_time += sum(green_time)
    
    fitness = -total_wait_time
    return fitness

def run_neat():
    config_path = "D:\\KUSHAGRA\\DATA\\K_Works\\ML AI TMS\\mixed\\config-neat.txt"
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
    
    population = neat.Population(config)
    population.add_reporter(neat.reporting.StdOutReporter(True))
    population.add_reporter(neat.reporting.StatisticsReporter())

    population.run(fitness_function, 300)

if __name__ == "__main__":
    if torch.cuda.is_available():
        device = torch.device("cuda")
        print("CUDA is available. Training will use GPU.")
    else:
        device = torch.device("cpu")
        print("CUDA is not available. Training will use CPU.")
        i = input("Ya Wanna start with CPU Seriously...(y): ")
        if(i=="y" or "Y"):
            pass
        else:
            sys.exit()
    run_neat()
