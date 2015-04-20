from numpy import *
def build_adjacencymatrix(final_rows):
    length_players = final_rows.length
    adjacency_matrix= zeros(shape(length_players,length_players),dtype= numpy.int)
    for x in final_rows:
        for y in final_rows:
            adjacency_matrix[final_rows.index(x[0]),final_rows.index(y[0])]=communication_cost[x[1],y[1]]
            
    return adjacency_matrix
        
    