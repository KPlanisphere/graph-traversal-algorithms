#Importamos las librerías necesarias para visualizar el recorrido minimo del grafo
import networkx as nx
import matplotlib.pyplot as plt

#Grafo para calcular distancias
grafo2 = {'A': ['B', 'F','C','G','E'],
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
distancias = Distancias(grafo2, 'A')

# Crear el grafo de NetworkX
G = nx.Graph()

#Creamos un diccionario que representa el grafo e añadimos los pesos correspondientes.
grafo = {
    'G': {'A': 4, 'E': 3},
    'B': {'A': 5, 'F': 1},
    'A': {'G': 4, 'C': 7, 'F': 8, 'B':5},
    'E': {'I': 3, 'C': 3, 'A': 2, 'G':3},
    'F': {'D': 6, 'A': 8, 'B': 1},
    'D': {'C': 8, 'F': 6, 'H': 6},
    'C': {'D': 8, 'H': 3, 'E': 3, 'A':7},
    'H': {'C': 3, 'D': 6, 'I': 2},
    'I': {'H': 2, 'E': 3}
}


for node in grafo:
    for neighbour, weight in grafo[node].items():
        
        G.add_edge(node, neighbour, weight=weight)


# Dibujar el grafo
pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True)
nx.draw_networkx_nodes(G, pos, node_size=1000, node_color='#A469BD')

#Poner la distancia en los nodos
node_labels = {node: f"\n\n{distancias[node]}" for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=12, font_color='white')

#Pesos
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_family="sans-serif", font_size=15)


# Indicamos cual es el Nodo Inicial
start = 'A'

# Calculamos la ruta más corta hacia todos los demás nodos
for goal in set(G.nodes):
    path = nx.shortest_path(G, start, goal, weight='weight')
    # Calculamos la suma de distancias
    dist_sum = sum([distancias[node] for node in path])
    # Calculamos el peso total de la ruta
    weight_sum = sum([G[path[i]][path[i+1]]['weight'] for i in range(len(path)-1)])
    print(f'Ruta de {start} a {goal}: {path}')
    print(f'Suma de distancias g(n): {dist_sum}')
    print(f'Heurisitica de la ruta h(n): {weight_sum}')
    print(f'f(n)=g(n)+h(n): {dist_sum+weight_sum}\n')

plt.show()