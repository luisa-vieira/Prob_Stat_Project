import numpy as np
import matplotlib.pyplot as plt

def birth_death_migration_process(X1_0, X2_0, X3_0, Y1_0, Y2_0, Y3_0, a10, a11, a12, a20, a21, u, v, total_time):
    
    population_X1 = X1_0
    population_Y1 = Y1_0
    population_X2 = X2_0
    population_Y2 = Y2_0
    population_X3 = X3_0
    population_Y3 = Y3_0
    
    time = 0
    
    time_points = [time]
    population_X1_sizes = [population_X1]
    population_Y1_sizes = [population_Y1]
    population_X2_sizes = [population_X2]
    population_Y2_sizes = [population_Y2]
    population_X3_sizes = [population_X3]
    population_Y3_sizes = [population_Y3]
    
    while time < total_time:

        # Step 1: Draw time of the next event from exponential distribution
        
        rate_X1_birth = a10 * population_X1
        rate_X1_death = a11 * population_X1 * population_X1 + a12 * population_X1 * population_Y1
        rate_Y1_birth = a21 * population_X1 * population_Y1
        rate_Y1_death = a20 * population_Y1
        rate_X2_birth = a10 * population_X2
        rate_X2_death = a11 * population_X2 * population_X2 + a12 * population_X2 * population_Y2
        rate_Y2_birth = a21 * population_X2 * population_Y2
        rate_Y2_death = a20 * population_Y2
        rate_X3_birth = a10 * population_X3
        rate_X3_death = a11 * population_X3 * population_X3 + a12 * population_X3 * population_Y3
        rate_Y3_birth = a21 * population_X3 * population_Y3
        rate_Y3_death = a20 * population_Y3
        rate_migration_X1_to_X2 = u * population_X1
        rate_migration_X1_to_X3 = u * population_X1 # ?
        rate_migration_X2_to_X1 = u * population_X2
        rate_migration_X2_to_X3 = u * population_X2 # ?
        rate_migration_Y1_to_Y2 = v * population_Y1
        rate_migration_Y1_to_Y3 = v * population_Y1 # ?
        rate_migration_Y2_to_Y1 = v * population_Y2
        rate_migration_Y2_to_Y3 = v * population_Y2 # ?
        rate_migration_X3_to_X1 = u * population_X3 # ?
        rate_migration_X3_to_X2 = u * population_X3 # ?
        rate_migration_Y3_to_Y1 = v * population_Y3 # ?
        rate_migration_Y3_to_Y2 = v * population_Y3 # ?
        
        total_rate = (
            rate_X1_birth + rate_X1_death + rate_Y1_birth + rate_Y1_death + 
            rate_X2_birth + rate_X2_death + rate_Y2_birth + rate_Y2_death +
            rate_X3_birth + rate_X3_death + rate_Y3_birth + rate_Y3_death +
            rate_migration_X1_to_X2 + rate_migration_X2_to_X1 +
            rate_migration_Y1_to_Y2 + rate_migration_Y2_to_Y1 +
            rate_migration_X1_to_X3 + rate_migration_X2_to_X3 +
            rate_migration_Y1_to_Y3 + rate_migration_Y2_to_Y3 +
            rate_migration_X3_to_X1 + rate_migration_X3_to_X2 +
            rate_migration_Y3_to_Y1 + rate_migration_Y3_to_Y2
        )
        
        # Ensure total_rate is non-negative
        
        if total_rate <= 0:
            break
        
        next_event_time = np.random.exponential(1 / total_rate)
        time += next_event_time
        
        # Step 2: Determine type of event
        
        probabilities = [
            rate_X1_birth / total_rate,
            rate_X1_death / total_rate,
            rate_Y1_birth / total_rate,
            rate_Y1_death / total_rate,
            rate_X2_birth / total_rate,
            rate_X2_death / total_rate,
            rate_Y2_birth / total_rate,
            rate_Y2_death / total_rate,
            rate_X3_birth / total_rate,
            rate_X3_death / total_rate,
            rate_Y3_birth / total_rate,
            rate_Y3_death / total_rate,
            rate_migration_X1_to_X2 / total_rate,
            rate_migration_X2_to_X1 / total_rate,
            rate_migration_Y1_to_Y2 / total_rate,
            rate_migration_Y2_to_Y1 / total_rate,
            rate_migration_X1_to_X3 / total_rate,
            rate_migration_X2_to_X3 / total_rate,
            rate_migration_Y1_to_Y3 / total_rate,
            rate_migration_Y2_to_Y3 / total_rate,
            rate_migration_X3_to_X1 / total_rate,
            rate_migration_X3_to_X2 / total_rate,
            rate_migration_Y3_to_Y1 / total_rate,
            rate_migration_Y3_to_Y2 / total_rate
        ]
        
        event = np.random.choice(
            ['X1_birth', 'X1_death', 'Y1_birth', 'Y1_death', 'X2_birth', 'X2_death', 'Y2_birth', 'Y2_death', 'X3_birth', 'X3_death', 'Y3_birth', 'Y3_death',
             'X1_to_X2', 'X2_to_X1', 'Y1_to_Y2', 'Y2_to_Y1', 'X1_to_X3', 'X2_to_X3', 'Y1_to_Y3', 'Y2_to_Y3', 'X3_to_X1', 'X3_to_X2', 'Y3_to_Y1', 'Y3_to_Y2'],
            p=probabilities
        )


        if event == 'X1_birth':
            population_X1 += 1
        elif event == 'X1_death':
            population_X1 -= 1
        elif event == 'Y1_birth':
            population_Y1 += 1
        elif event == 'Y1_death':
            population_Y1 -= 1
        elif event == 'X2_birth':
            population_X2 += 1
        elif event == 'X2_death':
            population_X2 -= 1
        elif event == 'Y2_birth':
            population_Y2 += 1
        elif event == 'Y2_death':
            population_Y2 -= 1
        elif event == 'X3_birth':
            population_X3 += 1
        elif event == 'X3_death':
            population_X3 -= 1
        elif event == 'Y3_birth':
            population_Y3 += 1
        elif event == 'Y3_death':
            population_Y3 -= 1
        elif event == 'X1_to_X2':
            population_X1 -= 1
            population_X2 += 1
        elif event == 'X2_to_X1':
            population_X1 += 1
            population_X2 -= 1
        elif event == 'Y1_to_Y2':
            population_Y1 -= 1
            population_Y2 += 1
        elif event == 'Y2_to_Y1':
            population_Y1 += 1
            population_Y2 -= 1
        elif event == 'X1_to_X3':
            population_X1 -= 1
            population_X3 += 1
        elif event == 'X2_to_X3':
            population_X2 -= 1
            population_X3 += 1
        elif event == 'Y1_to_Y3':
            population_Y1 -= 1
            population_Y3 += 1
        elif event == 'Y2_to_Y3':
            population_Y2 -= 1
            population_Y3 += 1
        elif event == 'X3_to_X1':
            population_X3 -= 1
            population_X1 += 1
        elif event == 'X3_to_X2':
            population_X3 -= 1
            population_X2 += 1
        elif event == 'Y3_to_Y1':
            population_Y3 -= 1
            population_Y1 += 1
        elif event == 'Y3_to_Y2':
            population_Y3 -= 1
            population_Y2 += 1
        
        # Ensure populations never go negative
        
        population_X1 = max(population_X1, 0)
        population_Y1 = max(population_Y1, 0)
        population_X2 = max(population_X2, 0)
        population_Y2 = max(population_Y2, 0)
        population_X3 = max(population_X3, 0)
        population_Y3 = max(population_Y3, 0)
        
        time_points.append(time)
        population_X1_sizes.append(population_X1)
        population_Y1_sizes.append(population_Y1)
        population_X2_sizes.append(population_X2)
        population_Y2_sizes.append(population_Y2)
        population_X3_sizes.append(population_X3)
        population_Y3_sizes.append(population_Y3)
    
    return time_points, population_X1_sizes, population_Y1_sizes, population_X2_sizes, population_Y2_sizes, population_X3_sizes, population_Y3_sizes


def run_multiple_simulations(num_simulations, X1_0, X2_0, X3_0, Y1_0, Y2_0, Y3_0, a10, a11, a12, a20, a21, u, v, total_time):
    prey_extinct_count = 0
    predators_extinct_count = 0
    coexist_count = 0
    
    for _ in range(num_simulations):
        _, population_X1_sizes, population_Y1_sizes, population_X2_sizes, population_Y2_sizes, population_X3_sizes, population_Y3_sizes  = birth_death_migration_process(
            X1_0, X2_0, X3_0, Y1_0, Y2_0, Y3_0, a10, a11, a12, a20, a21, u, v, total_time)
        
        final_population_X1 = population_X1_sizes[-1]
        final_population_Y1 = population_Y1_sizes[-1]
        final_population_X2 = population_X2_sizes[-1]
        final_population_Y2 = population_Y2_sizes[-1]
        final_population_X3 = population_X3_sizes[-1]
        final_population_Y3 = population_Y3_sizes[-1]
        
        if final_population_X1 == 0 and final_population_X2 == 0 and final_population_X3 == 0:
            prey_extinct_count += 1
        elif final_population_Y1 == 0 and final_population_Y2 and final_population_Y3 == 0:
            predators_extinct_count += 1
        else:
            coexist_count += 1
    
    prey_extinct_proportion = prey_extinct_count / num_simulations
    predators_extinct_proportion = predators_extinct_count / num_simulations
    coexist_proportion = coexist_count / num_simulations
    
    return prey_extinct_proportion, predators_extinct_proportion, coexist_proportion

num_simulations = 50
X1_0 = 15
Y1_0 = 7
X2_0 = 0
Y2_0 = 0
X3_0 = 0
Y3_0 = 0
total_time = 200
a10 = 1
a11 = 0.02
a12 = 0.1
a20 = 0.15
a21 = 0.01

u_values = [0, 0.001, 0.001, 0.01]
v_values = [0, 0.001, 0.01, 0.001]

for u, v in zip(u_values, v_values):
    print(f"Running simulation for u={u}, v={v}")
    time_points, population_X_sizes, population_Y_sizes, population_X2_sizes, population_Y2_sizes, population_X3_sizes, population_Y3_sizes = birth_death_migration_process(
        X1_0, X2_0, X3_0, Y1_0, Y2_0, Y3_0, a10, a11, a12, a20, a21, u, v, total_time)

    plt.plot(time_points, population_X_sizes, label='Prey 1')
    plt.plot(time_points, population_Y_sizes, label='Predator 1')
    plt.plot(time_points, population_X2_sizes, label='Prey 2')
    plt.plot(time_points, population_Y2_sizes, label='Predator 2')
    plt.plot(time_points, population_X3_sizes, label='Prey 3')
    plt.plot(time_points, population_Y3_sizes, label='Predator 3')
    plt.xlabel('Time')
    plt.ylabel('Population Size')
    plt.title(f'Population Dynamics over Time with Migration (u={u}, v={v})')
    plt.legend()
    plt.grid(True)
    plt.show()

    prey_extinct_proportion, predators_extinct_proportion, coexist_proportion = run_multiple_simulations(
        num_simulations, X1_0, X2_0, X3_0, Y1_0, Y2_0, Y3_0,
        a10, a11, a12, a20, a21, u, v, total_time)

    print(f"Proportion of sample paths where:")
    print("Prey are extinct:", prey_extinct_proportion)
    print("Predators are extinct:", predators_extinct_proportion)
    print("Both coexist:", coexist_proportion)
    print()