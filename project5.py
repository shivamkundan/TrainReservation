# Project 5
# Shivam Kundan
# skundan1@stu.parkland.edu
# CSC 220, Spring 2015

import sys
from readfile1 import *
from shortest_paths import *
from calculate_path import *
from graph import Graph
from graphviz import *

if __name__ == "__main__":
    
    #take file name from user
    r = ReadFile1(str(sys.argv[1]))

    #saving cities and travel times to a graph
    graph, vertex_list, cities_list, inputstring = r.save_to_graph()

    #to find shortest path between two cities
    c = CalculatePath(graph, vertex_list, cities_list)
    route = c.shortest_route()

    #print (route)

    #drawing system route map with highlighted itinerary
    g = GraphViz('map.' + str(sys.argv[1]).replace('.txt','') + '.gv', inputstring, route)
    g.draw_route_map()


    print('done')
        