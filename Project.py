import heapq

class CampusGraph:
    def __init__(self):
        self.graph = {}

    def add_location(self, location):
        if location not in self.graph:
            self.graph[location] = []

    def add_pathway(self, loc1, loc2, distance):
        self.graph[loc1].append((loc2, distance))
        self.graph[loc2].append((loc1, distance))

    def shortest_path(self, start, end):
        pq = [(0, start)]
        distances = {node: float('inf') for node in self.graph}
        previous = {node: None for node in self.graph}

        distances[start] = 0

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_node == end:
                break

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        path = []
        node = end
        while node:
            path.insert(0, node)
            node = previous[node]

        return path, distances[end]


campus = CampusGraph()

locations = ["Gate", "Library", "Cafeteria", "Lab", "Hostel", "Auditorium"]

for loc in locations:
    campus.add_location(loc)

campus.add_pathway("Gate", "Library", 4)
campus.add_pathway("Gate", "Cafeteria", 2)
campus.add_pathway("Library", "Lab", 3)
campus.add_pathway("Cafeteria", "Lab", 2)
campus.add_pathway("Lab", "Hostel", 5)
campus.add_pathway("Hostel", "Auditorium", 3)

start = input("Enter starting location: ")
end = input("Enter destination: ")

path, distance = campus.shortest_path(start, end)

print("Shortest Path:", " -> ".join(path))
print("Total Distance:", distance)