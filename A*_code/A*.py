import math

import numpy as np
import math
import copy

def shortest_path(M,start,goal):
    dictionary_up_to_date_distance = {node: math.inf for node in range(len(M.intersections))}
    shortest_path_to_node = {node: [0, []] for node in range(len(M.intersections))} # This is maybe irrelevant
    
    dictionary_up_to_date_distance[start] = np.linalg.norm(np.asarray(M.intersections[start]) - np.asarray(M.intersections[goal]))

    shortest_path_to_node[start][1].append(start)
    #print(shortest_path_to_node[start][1])
    
    visited = []
    
    while True:
        current_node, distance = sorted(dictionary_up_to_date_distance.items(), key = lambda x: x[1])[0]
        dictionary_up_to_date_distance.pop(current_node)
        visited.append(current_node)
        distance = distance - np.linalg.norm(np.asarray(M.intersections[current_node]) - np.asarray(M.intersections[goal]))
        #print('current_node ', current_node)
        if current_node == goal:
            return shortest_path_to_node[current_node][1]
        else:
            roads = M.roads[current_node]
            #print(roads)
            for road in roads:
                #print('road',road)
                temp_distance = np.linalg.norm(np.asarray(M.intersections[current_node]) - np.asarray(M.intersections[road]))
                heuristic = np.linalg.norm(np.asarray(M.intersections[road]) - np.asarray(M.intersections[goal]))
                final_distance = temp_distance + heuristic + distance
                #print('final distance', final_distance)
                
                if road in visited:
                    #print('visited')
                    continue
                
                if dictionary_up_to_date_distance[road] >= final_distance:
                    shortest_path_to_node[road][0] = final_distance
                    temp_list = []
                    #print(temp_list)
                    temp_list = shortest_path_to_node[current_node][1].copy()
                    #print(' Current_node {}, temp_list {}'.format(current_node, temp_list))
                    temp_list.append(road)
                    #print('temp list ', temp_list)
                    #print(road)
                    shortest_path_to_node[road][1] = temp_list
                    #print('temp list ', shortest_path_to_node[road][1])
                    dictionary_up_to_date_distance[road] = final_distance
        