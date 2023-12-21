from collections import deque
class Vertex:
    def __init__(self,key,population=None):
        self.id = key
        self.connected_to = {}
        self.population = population


    def add_neighbor(self,nbr,weight = 0):
        self.connected_to[nbr] = weight

    def __str__(self):
         return str(self.id) + " connected to:" + str([x.id for x in self.connected_to]) + \
             " with population: " + str(self.population)

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self,nbr):
        return self.connected_to[nbr]

    def set_population(self, population):  # Method to set population
        self.population = population

    def get_population(self):
        return int(self.population)


class Graph:
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def sum_neighbor_populations(graph):
        # Retrieve the target city vertex from the graph
        target_vertex = graph.get_vertex("New York")

        # Initialize the sum of populations with the target city's population
        total_population = target_vertex.get_population()

        # Iterate over the neighbors of the target city
        for neighbor_vertex in target_vertex.get_connections():
            # Add the neighbor's population to the total
            total_population += neighbor_vertex.get_population()

        # Return the target city and the total population sum
        return total_population

    def add_vertex(self,key, population = None):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(key,population)  # class vertex
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self,n):
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vert_list

    def add_edge(self,f,t,cost = 0):
        self.vert_list[f].add_neighbor(self.vert_list[t],cost)  # weight set to default as 1

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())

    def bfs_population_traverse(self):    # BFS time complexity O(V+vt) Vertex + visited
        start_vertex = self.get_vertex("New York")
        # if start_vertex is None:
        #     print("Starting vertex not found.")
        #     return

        visited = set()  # A set to keep track of visited vertices
        queue = deque([start_vertex])  # Create a queue for BFS
        visited.add(start_vertex)  # Mark the start vertex as visited

        while queue:
            current_vertex = queue.popleft()  # Dequeue a vertex from the queue

            # print(current_vertex)  # For demonstration, print the current vertex

            for nbr in current_vertex.get_connections():
                total_population += current_vertex.get_population()     # Visit all the neighbors of the vertex
                if nbr not in visited:
                    visited.add(nbr)  # Mark neighbor as visited
                    queue.append(nbr)  # Enqueue the neighbor

    def bfs(self,start_vertex_id, visited):
        queue = deque([start_vertex_id])  # Initialize the queue with the start vertex id
        visited.add(start_vertex_id)  # Mark the start vertex id as visited

        while queue:
            current_vertex_id = queue.popleft()
            current_vertex = self.get_vertex(current_vertex_id)
            for nbr in current_vertex.get_connections():  # Go through all the connected vertices
                nbr_id = nbr.get_id()  # Get the unique id of the neighbor vertex
                if nbr_id not in visited:
                    visited.add(nbr_id)  # Mark neighbor id as visited
                    queue.append(nbr_id)  # Enqueue the neighbor id

    def find_connected_components(self):
        visited = set()  # This will store vertex ids
        connected_components = 0

        for current_vertex in self:  # Iterate through all vertex objects in the graph
            current_vertex_id = current_vertex.get_id()  # Get the unique id of the vertex
            if current_vertex_id not in visited:  # If the vertex id hasn't been visited
                connected_components += 1  # We've found a new connected component
                self.bfs(current_vertex_id, visited)  # Perform BFS using vertex ids

        return connected_components

    def find_min_steps(self, start_id, end_id):
        # Ensure both vertices exist in the graph
        if start_id not in self.vert_list or end_id not in self.vert_list:
            return None  # If either vertex does not exist, return None

        start_vertex = self.get_vertex(start_id)
        end_vertex = self.get_vertex(end_id)

        # If the start and end are the same, the path length is 0
        if start_id == end_id:
            return 0

        # Queue for BFS that stores tuples of (vertex_id, distance)
        queue = deque([(start_vertex, 0)])

        # Set to keep track of visited vertices
        visited = {start_vertex}

        # Start BFS traversal
        while queue:
            current_vertex, distance = queue.popleft()

            # Visit all the neighbors of the current vertex
            for nbr in current_vertex.get_connections():
                if nbr == end_vertex:
                    distance += 1
                    print(f"Minimum highway from {start_id} to {end_id} is {distance}")  # Return the distance if end vertex is reached
                    return
                if nbr not in visited:
                    visited.add(nbr)
                    queue.append((nbr, distance + 1))  # Enqueue with incremented distance

        return None  # If the end vertex is not reachable from the start vertex


cities = Graph()
# input key and make connections
with open("city_population.txt", "r") as file:
    for line in file:
        city, population = line.strip().split(':')
        cities.add_vertex(city.strip(),population.strip())

with open("road_network.txt", "r") as file:
    for line in file:
        city1, city2 = line.strip().split(':')
        cities.add_edge(city1.strip(),city2.strip())
        cities.add_edge(city2.strip(), city1.strip())

# test
vertex = cities.get_vertex("New York")
print(cities.get_vertex("New York"))
number_of_components = cities.find_connected_components()
print(number_of_components)

# cities.bfs_population_traverse("New York")

cities.find_min_steps("New York", "Hoover")

print(cities.get_vertex("Los Angeles"))
#### task 3 test
total_population = cities.sum_neighbor_populations()
print(f" total population is {total_population}.")




