# Implementation of a Priority Queue
# Each element is a list of two elements (priority, element)
PRIORITY = 0
ID = 1

# data structure. Start by describing the priority queue as storing
# identifiers (drawn from set [0, n-1]) and an associated integer priority
# where lower values imply greater importance

# minHeap
# single shortest path using a priority queue
class BHeap:
    def __init__(self, size):
        """initialize Binary Heap to given number of elements"""
        self.size = size
        self.n = 0
        self.elements = [[0, None] for i in range(size+1)]
        self.positions = [0 for i in range(size+1)]
        
    def isEmpty(self):
        """Determine whether Binary Heap is empty"""
        return self.n == 0
    
    def smallest(self):
        id = self.elements[1][ID]
        
        # heap will have one less entry, so place final one appropiately
        last = self.elements[self.n]
        self.n -= 1
        
        self.elements[1] = last
        pIdx = 1
        child = pIdx *2
        while child <= self.n:
            # select smaller of two children 
            sm = self.elements[child]
            if child < self.n:
                if sm[PRIORITY] > self.elements[child+1][PRIORITY]:
                    sm = self.elements[child]
            if last[PRIORITY] <= sm[PRIORITY]:
                break
            self.elements[pIdx] = sm
            self.positions[sm[ID]] = pIdx
            
            pIdx = child
            child = 2*pIdx
        self.elements[pIdx] = last
        self.positions[last[ID]] = pIdx
        return id
            


    def insert(self, id, priority):
        """Insert item into heap with given priority"""
        self.n += 1
        i = self.n
        while i > 1:
            pIdx = int(i/2)
            p = self.elements[pIdx]

            if priority > p[PRIORITY]:
                break
            self.elements[i] = list(p)
            self.positions[p[ID]] = 1
            i = pIdx

        self.elements[i][ID] = id
        self.elements[i][PRIORITY] = priority
        self.positions[id] = i

    # O(log k) time find current location, 
    # change priority to be smaller then heapify
    def decreaseKey(self, id, newPriority):
        """Reduce the priority of the given item"""

        size = self.n
        self.n = self.positions[id] - 1
        self.insert(id, newPriority)
        self.n = size

import pytest as pyt
# single-source shortest path
# import BHeap

import sys

# sample graph with edge weights

graph = {   0:{1:6, 3:18, 2:8},
            1:{4:11},
            2:{3:9},
            3:{},
            4:{5:3},
            5:{3:4, 2:7}
        }

def singleShortestPath(graph, s):
    """Compute and return(dist, pred) matrices of computation"""
    
    pq = BHeap(len(graph))
    dist = {}
    pred = {}
    
    for v in graph:
#         dist[v] = sys.maxint
        dist[v] = sys.maxsize
        pred[v] = None
    dist[s] = 0
    
    for v in graph:
        pq.insert(v, dist[v])
    
    while not pq.isEmpty():
        u = pq.smallest()
        for v in graph[u]:
            wt = graph[u][v]
            newLen = dist[u] + wt
            
            if newLen < dist[v]:
                pq.decreaseKey(v, newLen)
                dist[v] = newLen
                pred[v] = u
    return (dist, pred)

def solution(s, v, dist, pred): 
    """Return path and total information for shortest path from s to v"""
    path = [v]
    total = dist[v]
    while v != s:
        v = pred[v]
        path.insert(0, v)
    return "length=" + str(total) + " " + str(path)

s = singleShortestPath(graph, 0)
# dist, pred = singleShortestPath(graph, 0)
# print(s)
# solution(0, 3, dist, pred)
s