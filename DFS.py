#Importamos las librerías necesarias para visualizar el grafo nos será útil para implementar el algoritmo DFS.
import matplotlib.pyplot as plt
import networkx as nx

#Creamos un diccionario que representa el grafo.
graph = {'A': ['B', 'F','C','G','E'],
        'B': ['A','F'],
        'C': ['A','E','D','H'],
        'D': ['F','C','H'],
        'E': ['G','A','C','I'],
        'F': ['B','A','D'],
        'G': ['A','E'],
        'H': ['D','C','I'],
        'I': ['E','H']
        }
# just an implementation of a queue
class MyQUEUE:
    
    def __init__(self):
        self.holder = []
        
    def enqueue(self,val):
        self.holder.append(val)
        
    def dequeue(self):
        val = None
        try:
            val = self.holder[0]
            if len(self.holder) == 1:
                self.holder = []
            else:
                self.holder = self.holder[1:]
        except:
            pass
            
        return val
    
    def IsEmpty(self):
        result = False
        if len(self.holder) == 0:
            result = True
        return result

#Recibimos el grafo y el nodo inicial
def Distancias(graph, start):
    #Diccionario para visitados
    visitados = {}
    #Diccionario para las distancias del nodo
    distancias = {}
    #Para cada nodo del grafo inicializamos estos dos diccionarios
    for node in graph.keys():
    #Esto indica que no han sido visitados
        visitados[node] = False
    #No tiene distancia asignada    
        distancias[node] = -1

    #Despues el nodo de inicio se marca como visitado
    visitados[start] = True
    #Y ahora su distancia sera 0
    distancias[start] = 0

    #Creamos una lista temporal con el nodo de inicio
    temp_path = [start]
    #Esto es para la cola de caminos
    path_queue = MyQUEUE()
    #Inicialmente contiene solo a el nodo inicial
    path_queue.enqueue(temp_path)
    
    while not path_queue.IsEmpty():
        #Extraemos el primer camino de la cola 
        tmp_path = path_queue.dequeue()
        last_node = tmp_path[-1]

        #Para cada nodo conectado al último nodo
        for link_node in graph[last_node]:
            #Si no ha sido visitado
            if not visitados[link_node]:
                #Creamos un nuevo camino 
                new_path = list(tmp_path)
                #Lo añadimos el nodo al nuevo camino
                new_path.append(link_node)
                # Se agrega a la cola de caminos
                path_queue.enqueue(new_path)
                #Se marca como visitado el nodo
                visitados[link_node] = True
                #Actualizamos la distancia del nodo conectado +1
                distancias[link_node] = distancias[last_node] + 1
    # Devolvemos los valor de orden y distancias
    return  distancias

#Mostramos resultado en consola
distancias = Distancias(graph, 'A')
print("Distancias: ", distancias)

# Aqui inicia el dfs recursivo
def recursive_dfs(graph, source, path=[]):
    if source not in path:
        path.append(source)
        if source not in graph:
            # Nodo hoja, retroceder
            return path
        for neighbour in graph[source]:
            path = recursive_dfs(graph, neighbour, path)
    return path


#Llamar a la funcion para el calculo de la distancia y el recorrido
path = recursive_dfs(graph, "A", [])


#Funcion para dibujar el grafo
def printGraph(G, pos, distances, title):
     # Imprimimos el recorrido en pantalla
    plt.title(title)
    # positions for all nodes
    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=1000,node_color='#A469BD')
    #Este es el recorrido
    nx.draw_networkx_edges(G, pos, edgelist=dfs_edges, width=3, arrowsize=30, edge_color='#F1C40F', arrows=True)
    # edges
    nx.draw_networkx_edges(G, pos, width=1,arrows=True,arrowsize=10,arrowstyle='->')  
    # Mostrar las distancias en los nodos
    labels = {node: f"{node},{distances[node]}" for node in G.nodes}
    nx.draw_networkx_labels(G, pos, labels, font_size=10, font_family='cursive') 

# Crear el gráfico con NetworkX
G = nx.DiGraph(graph) 
# Crear un diccionario con las posiciones de cada nodo
pos = nx.spring_layout(G)

dfs_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]

#Titulo del grafo
#Creamos el titulo en pantalla que moostrara el recorrido
title = 'Recorrido a lo DFS: ' + ' -> '.join(path)
printGraph(G, pos,distancias,title)

plt.axis('off')

# Mostrar el grafo
plt.show()