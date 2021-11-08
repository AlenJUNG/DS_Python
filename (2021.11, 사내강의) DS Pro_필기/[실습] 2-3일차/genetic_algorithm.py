# basic Genetic Algorithm operators

def init_population(n,c):
    import numpy as np 
    import math
    return np.array([[math.ceil(e) for e in pop] for pop in (np.random.rand(n,c)-0.5)]), np.zeros((2,c))-1

def single_point_crossover(population):
    import numpy as np 
    r,c, n = population.shape[0], population.shape[1], np.random.randint(1,population.shape[1])         
    for i in range(0,r,2):                
        population[i], population[i+1] = np.append(population[i][0:n],population[i+1][n:c]),np.append(population[i+1][0:n],population[i][n:c])        
    return population

def flip_mutation(population):
    return population.max() - population

def random_selection(population):
    import numpy as np 
    r = population.shape[0]
    new_population = population.copy()    
    for i in range(r):        
        new_population[i] = population[np.random.randint(0,r)]
    return new_population

def memorize(pop, memory):
    import numpy as np 
    return np.append(memory, pop.reshape(1,memory.shape[1]), axis=0)

def replace_duplicate(population, memory):
    import numpy as np 
    import math
    for i in range(population.shape[0]):         
        counter = 0                
        while population.shape[1] in sum((memory==population[i]).astype(int).T) and counter<100:                                
            population[i] = np.array([math.ceil(k) for k in (np.random.rand(population.shape[1])-0.5)])                    
            counter += 1                    
        memory = memorize(population[i], memory)        
    return population, memory

# 로지스틱의 예측 정확도를 fitness로 정의

def get_fitness(data, feature_list, target, population):    
    fitness = []
    for i in range(population.shape[0]):        
        columns = [feature_list[j] for j in range(population.shape[1]) if population[i,j]==1]                    
        fitness.append(predictive_model(data[columns], data[target]))                
    return fitness


def predictive_model(X,y):
    import statsmodels.api as sm
    lr = sm.Logit(y, sm.add_constant(X))
    lrmodel = lr.fit() 
    score = 1/lrmodel.aic
    return score

# Genetic Algorithm

def ga(data, feature_list, target, n, max_iter):
    import numpy as np 
    np.random.seed(0)
    c = len(feature_list)
    
    population, memory = init_population(n,c)
    population, memory = replace_duplicate(population, memory)    
    
    fitness    = get_fitness(data, feature_list, target, population)    
    
    optimal_value    = max(fitness)
    optimal_solution = population[np.where(fitness==optimal_value)][0]    
    
    for i in range(max_iter):                
        population = random_selection(population)
        population = single_point_crossover(population)                        
        if np.random.rand() < 0.3:
            population = flip_mutation(population)   
        
        population, memory = replace_duplicate(population, memory)
                
        fitness = get_fitness(data, feature_list, target, population)
                
        if max(fitness) > optimal_value:
            optimal_value    = max(fitness)
            optimal_solution = population[np.where(fitness==optimal_value)][0]                               
        
    return optimal_solution, optimal_value