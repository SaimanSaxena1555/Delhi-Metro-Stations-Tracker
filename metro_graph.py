import networkx as nx
import matplotlib.pyplot as plt
import metro_data as md

graph = md.graph
lines = md.lines

def shortest_path_function(graph):
    number_of_stations = 0
    input_start = input("Enter the starting station: ").lower()
    input_end = input("Enter the destination station: ").lower()

    if input_start not in graph.nodes:
        print(f"{input_start} is not a valid station.")
        return
    if input_end not in graph.nodes:
        print(f"{input_end} is not a valid station.")
        return
    
    shortest_path = nx.dijkstra_path(graph,input_start,input_end)
    for i in shortest_path:
        number_of_stations += 1
    print(f"The shortest path between {input_start} and {input_end} is: {shortest_path}")
    for stations in shortest_path:
        print(stations)
    print(f"The number of stations between {input_start} and {input_end} is: {number_of_stations}")
    time_of_travel(shortest_path)

def time_of_travel(shortest_path):
        time = 0
        for i in shortest_path:
             time = shortest_path[i].weight 
        print(f"The time is :{time}")


shortest_path_function(graph)
