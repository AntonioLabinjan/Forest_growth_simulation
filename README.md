# Forest_growth_simulation
This Python project simulates the growth of a forest over a specified number of years. The simulation starts with an initial set of trees in a forest, and each year, the trees have a chance to produce offspring, resulting in the growth of the forest.

## Simulation Parameters
You can adjust the following parameters in the simulation:

broj_godina: The number of years for which you want to simulate the forest growth.
velicina_sume: The size of the forest, represented by the number of squares or grid cells.
Initialization
The simulation begins by initializing the forest with a random distribution of trees. You can control the initial density of trees by modifying the loop that populates the forest. In this example, approximately 10% of the grid cells are initially populated with trees.

for _ in range(velicina_sume * velicina_sume // 10):
    x, y = random.randint(0, velicina_sume - 1), random.randint(0, velicina_sume - 1)
    suma[x][y] = 1

## Forest Growth
The rast_stabala function models the growth of trees in the forest. Each existing tree has a chance to produce offspring, leading to new trees in neighboring grid cells. The growth rate is controlled by the probability defined in the following line:

if random.random() < 0.2:
In this example, there is a 20% chance for each existing tree to produce offspring. You can adjust this probability to control the rate of forest growth.

## Visualization
The simulation includes visualization of the forest's growth over the specified number of years. It uses Matplotlib to display the forest grid at the end of each year. The imshow function is used to create a visual representation of the forest, with different shades of green indicating the presence of trees.

## Running the Simulation
You can run the simulation by executing the provided Python script. Adjust the simulation parameters to explore different scenarios of forest growth. (You can change number of years and forest area)
