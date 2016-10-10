# Project 5
# Shivam Kundan
# skundan1@stu.parkland.edu
# CSC 220, Spring 2015

import math

class GraphViz:
    
    def __init__(self, filename, inputstring, route):
        self._output_file = filename
        self._inputstring = inputstring
        self._route = []
        for item in reversed(route):
            self._route.append(item)



    def draw_route_map(self):
        """Writes the map in .gv format"""
        f = open (self._output_file, 'w')

        f.write('graph {')

                
        for i in range (0,(len(self._route)-1)):
            j = i + 1
            for line in self._inputstring.split():
                if (str(line.split(',')[0]) == str(self._route[i]) and str(line.split(',')[1]) == str(self._route[j])) or (str(line.split(',')[1]) == str(self._route[i]) and str(line.split(',')[0]) == str(self._route[j])):
                    f.write (line.split(',')[0] + ' -- ' + line.split(',')[1] + ' [label = \"' + self.minutes_to_hhmm(int(line.split(',')[2])) + '\" color = "red" fontcolor = "blue" fontname = "times bold" penwidth = "1"]')
                else:
                    f.write (line.split(',')[0] + ' -- ' + line.split(',')[1] + ' [label = \"' + self.minutes_to_hhmm(int(line.split(',')[2])) + '\"]')



        #for line in self._inputstring.split():
         #   for i in range (0,len(self._route)-1):
          #      j = i + 1
           #     if (str(line.split(',')[0]) == str(self._route[i]) and str(line.split(',')[1]) == str(self._route[j])) or (str(line.split(',')[1]) == str(self._route[i]) and str(line.split(',')[0]) == str(self._route[j])):
            #        f.write (line.split(',')[0] + ' -- ' + line.split(',')[1] + ' [label = \"' + self.minutes_to_hhmm(int(line.split(',')[2])) + '\" color = "red" fontcolor = "blue" fontname = "times bold" penwidth = "1"]')
             #   else:
              #      f.write (line.split(',')[0] + ' -- ' + line.split(',')[1] + ' [label = \"' + self.minutes_to_hhmm(int(line.split(',')[2])) + '\"]')

        f.write('}')

        f.close()

        print('Route map saved as ' + str(self._output_file) + '\n')

    def minutes_to_hhmm(self, totalminutes):
        """Converts time format from minutes to hh:mm"""

        hours = totalminutes/60

        hh = int(hours)

        mm = "%02d" % (math.ceil((hours - hh)*60),)

        return (str(hh) + ':' + str(mm))

