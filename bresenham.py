#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mateo

Implementation of Bresenham's line algorithm
"""

def line(path,length,coord,fig):
    line = 1
    
    for i in range(length,0,-1):
        # Last position corresponds to source node
        x0 = coord[int(path[i]),0]
        y0 = coord[int(path[i]),1]
        x1 = coord[int(path[i-1]),0]
        y1 = coord[int(path[i-1]),1]
        
        dx = x1 - x0
        dy = y1 - y0
        # Increments for the inclined sections
        if dx >= 0:
            incr_x_i = 1
        else:
            incr_x_i = -1
            dx = -dx
        if dy >= 0:
            incr_y_i = 1
        else:
            incr_y_i = -1
            dy = -dy
        # Increments for straight sections
        if dx >= dy:
            incr_x_str = incr_x_i
            incr_y_str = 0
        else:
            incr_x_str = 0
            incr_y_str = incr_y_i
            # Swap dx and dy
            aux = dx
            dx = dy
            dy = aux
        # Inicialization of parameters
        x = x0
        y = y0
        str_mov = 2 * dy
        mov = str_mov - dx
        inc_mov = mov - dx
        # Line plot
        while True:
            fig[int(y),int(x)] = line
            if mov >= 0:
                x = x + incr_x_i
                y = y + incr_y_i
                mov = mov + inc_mov
            else:
                x = x + incr_x_str
                y = y + incr_y_str
                mov = mov + str_mov
            if x == x1 and y == y1:
                break
    return fig