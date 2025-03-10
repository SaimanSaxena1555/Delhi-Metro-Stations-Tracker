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
    distance = nx.dijkstra_path_length(graph,input_start,input_end)
    for i in shortest_path:
        number_of_stations += 1
    print(f"The shortest path between {input_start} and {input_end} is: {shortest_path}")
    for stations in shortest_path:
        print(stations)
    print(f"The number of stations between {input_start} and {input_end} is: {number_of_stations}")
    time_of_travel(distance)

def time_of_travel(distance):
    metro_speed_mps = 11.11  # Speed in meters per second (converted from 40 km/h)
    travel_time_seconds = distance / metro_speed_mps  # Time in seconds
    travel_time_minutes = travel_time_seconds / 60  # Convert to minutes

    print(f"Estimated travel time: {travel_time_minutes:.2f} minutes")



shortest_path_function(graph)
