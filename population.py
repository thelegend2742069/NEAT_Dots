from dots import Dots, Goal, Bars
from neural_network import NeuralNetwork
import itertools
class Population:
    def __init__(self, population:int, nodes_per_layer:list) -> None:
        self.population = population
        self.dots = [Dots() for _ in range(self.population)]
        self.NNs = [NeuralNetwork(nodes_per_layer) for _ in range(self.population)]
        self.fittest = 0

    def update(self, goal:Goal, bars:list[Bars]):
        self.fittest = 0

        for dot, nn in zip(self.dots, self.NNs):
            if not dot.alive: 
                continue

            old = (dot.x, dot.y)

            inputs = list(map(dot.distance_to, [goal]+bars))
            inputs = list(itertools.chain.from_iterable(inputs))
            # print(inputs)
            (up, right, left) = nn.calculate_output(inputs)
            
            if up > 0.100: dot.move_up()
            # if down > 0.100: dot.move_down()
            if right > 0.100: dot.move_right()
            if left > 0.100: dot.move_left()

            for bar in bars:
                if bar.collides(dot): 
                    dot.kill()
                    # print(dot)
                    # print(nn)
            
            if goal.collides(dot): dot.kill()
            
            if old == (dot.x, dot.y): dot.kill()

            fitness = dot.get_fitness(goal)
            if fitness > self.fittest: self.fittest = fitness
            # print(fitness)
    

    def draw(self, window):
        for dot in self.dots:
            # if dot.alive: print("drawing: ", dot, dot.x, dot.y)
            dot.draw(window)
    
    def get_fitness(self):
        l = []
        print('-----------------------------------------')
        for dot in self.dots:
            l.append(dot.fittness)
        print(l)
        print(max(l))