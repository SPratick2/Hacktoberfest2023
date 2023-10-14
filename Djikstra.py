def dijkstra(graph, source):

  distances = {vertex: float("inf") for vertex in graph}
  previous_nodes = {vertex: None for vertex in graph}


  queue = [(0, source)]


  while queue:
    _, current_vertex = queue.pop(0)
    if current_vertex == destination:
      break


    for neighbor in graph[current_vertex]:
      if distances[neighbor] > distances[current_vertex] + graph[current_vertex][neighbor]:
        distances[neighbor] = distances[current_vertex] + graph[current_vertex][neighbor]
        previous_nodes[neighbor] = current_vertex
  return distances, previous_nodes