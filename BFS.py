def BFS(graph, start, goal, heuristic):
    path = []
    open_list = [(0, start)]
    closed_list = set()

    while open_list:
        open_list.sort(key = lambda x : heuristic[x[1]])
        cost, node = open_list.pop(0)
        path.append(node)

        if node == goal:
            return cost, path

        closed_list.add(node)
        for neighbour, neighbour_cost in graph[node]:
            if neighbour not in closed_list and (cost + neighbour_cost, neighbour) not in open_list:
                open_list.append((cost+neighbour_cost, neighbour))

    return None

graph = {
    'A': [('B', 11), ('C', 14), ('D',7)],
    'B': [('A', 11), ('E', 15)],
    'C': [('A', 14), ('E', 8), ('D',18), ('F',10)],
    'D': [('A', 7), ('F', 25), ('C',18)],
    'E': [('B', 15), ('C', 8), ('H',9)],
    'F': [('G', 20), ('C', 10), ('D',25)],
    'G': [],
    'H': [('E',9), ('G',10)]
}

start = 'A'
goal = 'G'

heuristic = {
    'A': 40,
    'B': 32,
    'C': 25,
    'D': 35,
    'E': 19,
    'F': 17,
    'G': 0,
    'H': 10
}

result = BFS(graph, start, goal, heuristic)

if result:
    print(f'Path exists from {start} to {goal}')
    print(f'Path : ', result[1])
    print(f'Cost is {result[0]}')
else:
    print("No Path")