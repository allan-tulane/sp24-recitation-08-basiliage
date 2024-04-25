from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
  dist = {vertex: float('infinity') for vertex in graph}
  num_e = {vertex: float('infinity') for vertex in graph}

  dist[source] = 0
  num_e[source] = 0

  visited = set()

  while len(visited) < len(graph):
      min_vertex = min((v for v in graph if v not in visited), key=lambda x: dist[x])
      visited.add(min_vertex)
      for neighbor, weight in graph[min_vertex]:
          new_d = dist[min_vertex] + weight
          new_e = num_e[min_vertex] + 1

          if new_d < dist[neighbor] or (new_d == dist[neighbor] and new_e < num_e[neighbor]):
              dist[neighbor] = new_d
              num_e[neighbor] = new_e

  return {vertex: (dist[vertex], num_e[vertex]) for vertex in graph}


    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    ### TODO



    

    
    
def bfs_path(graph, source):
  parent = {}  
  visited = {source: None} 
  queue = deque([source])
  while queue:
      node = queue.popleft()
      for neighbor in graph[node]:
          if neighbor not in visited:
              visited[neighbor] = node  
              parent[neighbor] = node
              queue.append(neighbor)

  return parent
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    ###TODO


def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
  if destination not in parents:
    return ''
  else:
    main = parents[destination]
    return get_path(parents, main) + main
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO

