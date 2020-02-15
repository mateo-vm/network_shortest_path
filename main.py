#! python3
# -*- coding: utf-8 -*-
"""
@author: mateo
"""

import numpy as np
import random
from scipy import signal as sg
from matplotlib import pyplot as plt

import dijkstra
import bresenham

def create_newimage(width,height,nsize,num_nodes):
    F = np.zeros((height,width))
    
    nsize = nsize//2
    N = np.ones((2*nsize+1,2*nsize+1))
    random.seed()
    for i in range(0,num_nodes):
        x = random.randint(nsize+1,width-(nsize+1))
        y = random.randint(nsize+1,height-(nsize+1))
        F[y-nsize:y+nsize+1,x-nsize:x+nsize+1] = N
    return F

def find_node(fig,width,height,nsize):
    filt = np.ones(((nsize),(nsize)))/(nsize**2)
    
    f0 = sg.convolve(fig, filt, 'same')
    
    pos = np.empty((0,2))
    threshold = 0.9
    
    # The order of the loop was changed to get the coordinates already ordered
    for j in range(1,width-1):
        for i in range(1,height-1):
            if f0[i-1,j]<f0[i,j] and f0[i,j-1]<f0[i,j] and f0[i+1,j]<f0[i,j] and f0[i,j+1]<f0[i,j] and threshold<f0[i,j]:
                pos = np.append(pos,[[j,i]],axis=0)
    return pos

def calc_energy(coord):
    n = len(coord)
    e = np.zeros((n,n))
    
    for i in range(0,n):
        for j in range(0,n):
            if j >= i:
                # As energy is a fuction of the square of the distance
                # usage of the square root to calculate the actual distance
                # is skipped to save calculation time
                e[i,j] = (coord[i,0]-coord[j,0])**2+(coord[i,1]-coord[j,1])**2
            else:
                # Save calculation time, matrix will be always symmetric
                e[i,j] = e[j,i]
    return e

def main():
    # Initial parameters
    height    = int(720)
    width     = int(1280)
    nsize     = int(9)
    num_nodes = int(50)
    
    # Correct node size
    if (nsize%2) == 0:
        nsize = nsize + 1
    
    # Create figure
    fig = create_newimage(width,height,nsize,num_nodes)
    plt.figure(0)
    plt.imshow(fig, interpolation='nearest')
    plt.title('Base image')
    plt.show(block=False)
    
    # Find nodes
    pos_node = find_node(fig,width,height,nsize);
    print(pos_node)
    
    # Calculate energy = f(distance)
    energy = calc_energy(pos_node);
    
    # Calculate the shortest path
    dijkstra_res = dijkstra.shortest_path(energy,0,num_nodes-1,num_nodes)
    energy_req = dijkstra_res[0]
    path = dijkstra_res[1]
    length_path = dijkstra_res[2]
    
    # Plot the lines on the image
    final_fig = bresenham.line(path,length_path,pos_node,fig);
    plt.figure(1)
    plt.imshow(final_fig, interpolation='nearest')
    plt.title('Final image')
    plt.show()

if __name__== "__main__":
    main()
