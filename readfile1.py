# Project 5
# Shivam Kundan
# skundan1@stu.parkland.edu
# CSC 220, Spring 2015

from shortest_paths import *
from graph import Graph
import sys
import string

class ReadFile1:

    def __init__(self, filename):
        self._filename = filename


    def save_to_graph(self):
            """Saves origin, destination, and travel time to graph"""

            inputstring = self.updated_file()

            length = len(inputstring.split())

            #My earlier attempt to use a python dictionary did not work out.
            #When calling dict[city], it would not return the Vertex object
            #and instead returned just the city name.
            #The index number for cities_list matches those for vertex_list

            cities_list = []

            vertex_list = []

            #adding cities to list without any repetition
            for i in range (0,length):
                
                if inputstring.split('\n')[i].split(',')[0] not in cities_list:
                    cities_list.append(inputstring.split('\n')[i].split(',')[0])
                
                if inputstring.split('\n')[i].split(',')[1] not in cities_list:
                    cities_list.append(inputstring.split('\n')[i].split(',')[1])

            g = Graph()

            #inserting vertices
            for city in cities_list:
                v = g.insert_vertex(str(city))
                vertex_list.append(v)

            
            #inserting edges
            for i in range (0, length):
                
                city1_index = cities_list.index\
                (str(inputstring.split('\n')[i].split(',')[0]))
                
                city2_index = cities_list.index\
                (str(inputstring.split('\n')[i].split(',')[1]))
                
                time = int(inputstring.split('\n')[i].split(',')[2])
                
                g.insert_edge(vertex_list[city1_index],\
                    vertex_list[city2_index],time)


            return g, vertex_list, cities_list, inputstring

    def updated_file(self):
        """Converts format from (city1,city2,hh:mm) 
           to (city1,city2,total_minutes)""" 
        
        #checking if input file exists
        try:                                    
            f = open(self._filename, 'r')
        except IOError:                        
            print ('error: input file does not exist')
        else:  
            
            #reading file
            inputstring = f.read()
            length = len(inputstring.split())
            f.close()

            outstring = ''
            for i in range (0,length):
                outstring = outstring + inputstring.split()[i].split(',')[0]+\
                ',' + inputstring.split()[i].split(',')[1] + ',' +\
                str(self.convert_to_mins(inputstring.split()[i].\
                    split(',')[2])) + '\n'

            return outstring.lower()

    def convert_to_mins(self, time):
        """Converts time in format hh:mm to minutes"""
        self._time = time
        hours = int(self._time.split(':')[0])
        mins = int(self._time.split(':')[1])
        totalmins = (hours * 60) + mins
        return totalmins







