import heapq
def heuristic(node):
    h={
        'A':6,
        'B':4,
        'C':4,
        'D':3,
        'E':1,
        'G':0,
    }
    return h[node]
graph={
    'A':[('B',2),('C',3)],
    'B':[('D',3),('E',1)],
    'C':[('D',1)],
    'D':[('G',2)],
    'E':[('G',3)],
    'G':[]
}
start_node = 'A'

def a_star(start,goal,graph):
    open_list = []
    heapq.heappush(open_list,(0,start,[start],0))
    
    closed_list= set()
    
    while open_list:
        f,current,path,g = heapq.heappop(open_list)
        if current == goal:
            return path,g
        closed_list.add(current)
        
        for neighbour,cost in graph[current]:
            if neighbour not in closed_list:
                new_g = g+cost
                new_f = new_g + heuristic(neighbour)
                
                heapq.heappush(
                    open_list,
                    (new_f,neighbour,path + [neighbour],new_g)
                    )

goal_node = 'G'
path,cost = a_star(start_node,goal_node,graph)

print("Path: ",path)
print("Total cost: ",cost)
