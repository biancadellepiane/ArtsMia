
import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._idMap = {}

    def buildGraph(self):
        nodes=DAO.getAllNodes()
        self._idMap = {}
        for n in nodes:
            self._idMap[n.object_id] = n

        self._graph.clear()
        self._graph.add_nodes_from(nodes)

        archi = DAO.getAllEdges(self._idMap)
        for a in archi:
            self._graph.add_edge(a.o1, a.o2, weight=a.peso)

    def getGraphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def getComponenteConnessa(self, idOggetto):
        nodoP = self._idMap[idOggetto]

        #componente connessa ci sono vari metodi, il più corretto è:
        componenteConnessa = nx.node_connected_component(self._graph, nodoP) #dato il grafo, prendendo il nodoP
        #prendo il numero di valori
        return len(componenteConnessa)

        #prendo i valori:
        #return componenteConnessa --> lista

        #ciao