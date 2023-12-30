## To Do List:
- Layer Class
    - stores no. of incoming nodes, no. of outgoing nodes, weights, and biases
    - Calculate Output Function: 
        - takes list of inputs (outputs of previous layer)
        - applies weight and bias associated with it
        - return list of values as output of layer (output of each node)

- Neural Network Class
    - creates and stores all the layers
    - Calculate Output Function: 
        - initial input will be game parameters (dist from bars, goal)
        - passed to layer to calculate its output, which will act as input to next layer
        - output of final layer will the output of our NN

- Activation Function
    - apply ReLU or Sigmoid function on input

- Mutation Function
    - 90% chance for any parameter to mutate
    - start of generation should have more drastic mutations, while later on mutations should be gentler
    - maybe set an initial rate which decreases as the generations go on
    - rate of decrement could be fraction of generations over max generations

- Population Function
    - creates a population of n dots initialising their nodes and weights with random values

- New Generation Function
    - saves 5 best dots from previous generation and uses them to create new population of 45 new dots while applying mutations
    - best 5 bots are added to this population
    - each parameter can come from any old dot probability of using old dots based on score