
import random # For random number generation
from fuzzywuzzy import fuzz # for string similarity
import string # to get access to some utility functions

# Ideally store these variables and such in a config file

population = 25
generations = 8000
target_str = None # input string that we target towards
target_len = None # length of that string
do_mutations = True
mutation_chance = 0.1
fitness_threshold = 89 # if reached you can stop



# Representation of an individual (A.K.A. agent)
class Individual:

    def __init__(self, length):

        self.string = ''.join(random.choice(string.ascii_letters) for _ in range(length)) # Each initialized with a random string
        self.fitness = -1 # No evaluation had been done on object yet

    def __str__(self): # like toString in java

        return 'String (Guess): ' + str(self.string) + ' Fitness Score: ' + str(self.fitness)


def init_Individuals(population, length):

    return [Individual(length) for _ in range(population)]


# If the problem can exhibit some form of partial correctness, then a genetic algorithm works just fine
def ga():

    Individuals = init_Individuals(population, target_len)

    for generation in range(generations):

        print()
        print('!!! Generation: ' + str(generation) + ' !!!')
        print()

        Individuals = fitness(Individuals)
        Individuals = selection(Individuals)
        Individuals = crossover(Individuals)
        if do_mutations:
            # I could actually define different mutation functions, or maybe I'd add a second 'type' parameter for the mutation function, and therefoer enable other mutation choices to be analysed (would've been better for the submission)
            Individuals = mutation(Individuals)

        if any(Individual.fitness >= fitness_threshold for Individual in Individuals): 

            print('Threshold had been met!')
            exit(0)




def fitness(Individuals):

    for Individual in Individuals:

        Individual.fitness = fuzz.ratio(Individual.string, target_str)

    return Individuals


def selection(Individuals):

    Individuals = sorted(Individuals, key=lambda Individual: Individual.fitness, reverse=True)

    print('\n'.join(map(str, Individuals)))
    
    Individuals = Individuals[:int(0.2 * len(Individuals))] # 0.2 -> percentage of Individuals that will be moving on for reproduction

    return Individuals


def crossover(Individuals):

    offspring = []

    for _ in range((population - len(Individuals)) // 2):

        parent1 = random.choice(Individuals)
        parent2 = random.choice(Individuals) # Here we may select the same parent twice, but it isn't that crucial for the purpose of this analyse

        child1 = Individual(target_len)
        child2 = Individual(target_len)
        
        split = random.randint(0, target_len)
        child1.string = parent1.string[0:split] + parent2.string[split:target_len]
        child2.string = parent2.string[0:split] + parent1.string[split:target_len]

        offspring.append(child1)
        offspring.append(child2)

    Individuals.extend(offspring)

    return Individuals


def mutation(Individuals):

    for Individual in Individuals:

        for idx, param in enumerate(Individual.string):

            if random.uniform(0.0, 1.0) <= mutation_chance:

                Individual.string = Individual.string[0:idx] + random.choice(string.ascii_letters) + Individual.string[idx+1:target_len] # Here we simply 'flip' a value, we could also use inversion (swap) etc...
                 

    return Individuals


if __name__ == '__main__':

    target_str = 'batikanor'
    target_len = len(target_str)
    ga()