def all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = all_paths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

def shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            new_path = shortest_path(graph, node, end, path)
            if new_path:
                if not shortest or len(new_path) < len(shortest):
                    shortest = new_path
    return shortest

def find_shortest_paths(all_paths, shortest_path):
    shortest_paths = []
    for path in all_paths:
        if len(path) == len(shortest_path):
            shortest_paths.append(path)
    return shortest_paths

def display_paths(paths):
    for i in range(len(paths)):
        print('Path', i+1, '=', paths[i])

def find_all_edges(graph):
    edges = []
    for key in graph.keys():
        if graph[key]:
            for value in graph[key]:
                temp = key + ' => ' + value
                edges.append(temp)
    return edges

graphSembarang = {
    'A': ['B', 'C', 'D'],
    'B': ['C', 'E', 'F'],
    'C': ['F'],
    'D': ['C', 'G', 'T'],
    'E': ['T'],
    'F': ['T'],
    'G': ['T'],
    'T': []
}

print('a. Banyaknya Edge:')
SemuaEdge = find_all_edges(graphSembarang)
display_paths(SemuaEdge)

print('\nb. Banyaknya Path:')
ListAllPaths = all_paths(graphSembarang, 'A', 'T')
display_paths(ListAllPaths)

print('\nc. Path terpendek:')
ShortPath = shortest_path(graphSembarang, 'A', 'T')
ListShortestPaths = find_shortest_paths(ListAllPaths, ShortPath)
display_paths(ListShortestPaths)
