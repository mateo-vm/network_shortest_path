#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mateo

Implementation of Dijkstra's shortes path algorithm
"""

import numpy as np

def shortest_path(graph,src,dst,n):
    path = np.empty((0))
    length = int(0)
    
    dist = np.zeros((n))
    for i in range(0,n):
        dist[i] = float('Inf')
    parent = np.zeros((n))
    visited = np.zeros((n))
    
    visited[src] = 1
    dist[src] = 0
    node = src
    
    while node != dst:
        # Look for the min distance to each non-visited node
        for i in range(0,n):
            if visited[i] == 0 and (dist[node] + graph[node,i]) < dist[i]:
                parent[i] = node
                dist[i] = dist[node] + graph[node,i]
        # Look for the next node
        min_dist = float('Inf')
        for i in range(0,n):
            if visited[i] == 0 and dist[i] < min_dist:
                min_dist = dist[i]
                node = i
        visited[node] = 1
    
    # Prepare the results
    while node != src:
        path = np.append(path,node)
        node = parent[int(node)]
        length = length + 1
    path = np.append(path,node) # Add the source node to path
    distance = dist[dst]
    return(distance, path, length)