import networkx as nx
import matplotlib.pyplot as plt
import openpyxl
from pyvis.network import Network

file = "Book1.xlsx"
names = []
total_names=[]
G = nx.Graph()

livre=openpyxl.load_workbook(file)
feuille=livre.active


for element in feuille.iter_rows(values_only=True):
    person1 = element[0]
    person2 = element[1]
    names.append((person1, person2))
    total_names.append(person1)
    total_names.append(person2)

G.add_edges_from(names)
G1=Network('500px','500px')
G1.from_nx(G)
G1.toggle_physics(True)
G1.show('mygraph.html')
#nx.draw(G,with_labels=True)
#plt.show()
