def all_nodes(size):
    a, b = size
    nodes = set()
    for i in range(a*b):
        nodes.add(str(i))
    return nodes
        
def create_maze(size):
    a, b = size
    start = 0
    maze = []
    for i in range(a):
        for j in range(b):
            if j != b - 1:
                maze.append([str(start), str(start+1)])
            if i != a - 1: 
                maze.append([str(start), str(start + b)])
            start += 1  
    return maze   

def create_adj_list(edge_list):
    graph = {}
    for edge in edge_list:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph
    

def maze_game(graph, nodes):
    player1 = set()
    while True:
        x = str(input("Click on Node: "))
        if x == "-1":
            print("exit...")
            break
        if str(x) in player1:
            print(f"node is already clicked {x}")
            continue
        if x not in nodes:
            print("please enter correcte node")
            continue
        if player1 == nodes:
            print("congo you win")
            break
        player1.add(x)
        for i in graph[x]:
            player1.add(str(i))
        p = "-".join(player1)
        print(f"you: {p}")
        


if __name__ == "__main__":
    size = [6, 6]
    maze = create_maze(size)
    nodes = all_nodes(size)
    graph = create_adj_list(maze)
    maze_game(graph, nodes)