import networkx as nx
import matplotlib.pyplot as plt
import metro_data as md

num = 1
graph = md.graph 

for stations in graph:
    num += 1
    print(stations , num )  