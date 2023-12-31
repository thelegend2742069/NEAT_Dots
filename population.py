from dots import Dots, Goal, Bars
from neural_network import NeuralNetwork
class Population:
    def __init__(self, population:int, nodes_per_layer:list) -> None:
        self.population = population
        self.dots = [Dots() for _ in range(self.population)]
        self.NNs = [NeuralNetwork(nodes_per_layer) for _ in range(self.population)]


    def update(self, goal:Goal, bars:list[Bars]):
        
        for dot, nn in zip(self.dots, self.NNs):
            if not dot.alive: continue

            inputs = list(map(dot.distance_to, [goal]+bars))
            (up, right, left) = nn.calculate_output(inputs)
            
            if up > 0.150: dot.move_up()
            if right > 0.150: dot.move_right()
            if left > 0.150: dot.move_left()

            for bar in bars:
                if bar.collides(dot): 
                    dot.kill()
                    # print(dot)
                    # print(nn)
            
            if goal.collides(dot): dot.kill()
    

    def draw(self, window):
        for dot in self.dots:
            # if dot.alive: print("drawing: ", dot, dot.x, dot.y)
            dot.draw(window)