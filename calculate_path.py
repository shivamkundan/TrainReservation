# Project 5
# Shivam Kundan
# skundan1@stu.parkland.edu
# CSC 220, Spring 2015

from shortest_paths import *
from graph import *
import copy
import string
import math

class CalculatePath:

    def __init__(self, graph, vertex_list, cities_list):
        self._g = graph
        self._vertex_list = vertex_list
        self._cities_list = cities_list

    
    def calculate_length(self):        

        origin_city = ''
        destination_city = ''

        #take user input for origin
        while origin_city not in self._cities_list:
            origin_city = str(input('Enter origin city name: ')).lower()

        #take user input for destination
        while destination_city not in self._cities_list:
            destination_city = str(input('Enter destination city name: ')).lower()

        #computing shortest path distances from origin
        dist_map = shortest_path_lengths(self._g, self._vertex_list[self._cities_list.index(origin_city)])

        #computing total journey time
        time_taken = dist_map[self._vertex_list[self._cities_list.index(destination_city)]]

        #Return tree as a map from each reachable vertex v (other than s)
        # to the edge e=(u,v) that is used to reach v from its parent u 
        #  in the tree.
        tree = shortest_path_tree(self._g, self._vertex_list\
            [self._cities_list.index(origin_city)], dist_map )

        return tree, origin_city, destination_city, time_taken


    def shortest_route(self):
        """Prints the actual shortest route"""
        tree, origin, destination, time = self.calculate_length()

        mylist = []

        vertex1 = self._vertex_list[self._cities_list.index(destination)] #starting vertex
        mylist.append(vertex1.element())

        vertex2_name = ''

        while str(vertex2_name) != str(origin):
            vertex2 = tree[vertex1].opposite(vertex1)
            vertex2_name = vertex2.element()
            mylist.append(vertex2_name)
            vertex1 = vertex2


        print('\nShortest route is: ')
        for item in reversed(mylist):
            print (str(item))
        print('\nTotal journey time: ' + str(self.minutes_to_hhmm(time)) + '\n')

        return (mylist)


    def minutes_to_hhmm(self, totalminutes):
        """Converts time format from minutes to hh:mm"""

        hours = totalminutes/60

        hh = int(hours)

        mm = "%02d" % (math.ceil((hours - hh)*60),)

        return (str(hh) + ':' + str(mm))
















