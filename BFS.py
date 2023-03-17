import networkx as nx
import matplotlib.pyplot as plt

#Grafo  
graph = {'A': ['B', 'F','C','G','E'],
        'B': ['A','F'],
        'C': ['A','E','D','H'],
        'D': ['F','C','H'],
        'E': ['G','A','C','I'],
        'F': ['B','A','D'],
        'G': ['A','E'],
        'H': ['D','C','I'],
        'I': ['E','H']}

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
def BFS(graph, start):
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
    #Crear una lista que contendrá el orden recorrido con BFS.
    orden_grafo_bfs = []

    
    while not path_queue.IsEmpty():
        #Extraemos el primer camino de la cola 
        tmp_path = path_queue.dequeue()
        last_node = tmp_path[-1]
        #Se toma el ultimo nodo de ese camino
        orden_grafo_bfs.append(last_node)

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
    return orden_grafo_bfs, distancias

#Mostramos resultado en consola
orden_grafo_bfs, distancias = BFS(graph, 'A')
print("Distancias: ", distancias)

def printGraph(G, pos, distancias,title):
    # Imprimimos el recorrido en pantalla
    plt.title(title)

    # Dibujar los nodos y las aristas del grafo
    nx.draw_networkx_nodes(G, pos, node_size=1000,node_color='#A469BD')
    # edges
    nx.draw_networkx_edges(G, pos, width=1,arrows=True,arrowsize=10,arrowstyle='-')

    # Añadir etiquetas a los nodos con sus nombres y distancias
    labels = {node: f"{node},{distancias[node]}" for node in G.nodes}
    nx.draw_networkx_labels(G, pos,labels,font_size=15, font_family="sans-serif")
    
    #Ahora dibujamos el recorrido del grafo
    #COn un ciclo iteramos el orden en que se fueron visitando los nodos en BFS
    for i in range(len(orden_grafo_bfs)-1):  
        #edgelist contiene el par de nodos, representadndo los bordes que se dibujaran
        nx.draw_networkx_edges(G, pos, edgelist=[(orden_grafo_bfs[i], orden_grafo_bfs[i+1])], width=2,arrows=True ,edge_color='#F1C40F',arrowsize=30)


# Crear el gráfico con NetworkX
G = nx.DiGraph(graph)
# Crear un diccionario con las posiciones de cada nodo
pos = nx.spring_layout(G)
#Creamos el titulo en pantalla que moostrara el recorrido
title = 'Recorrido a lo Ancho: ' + ' -> '.join(orden_grafo_bfs)
printGraph(G, pos,distancias,title)

# Mostrar el grafo
plt.axis("off")
plt.show()