'''

jo : rouge et grosse taille (size=175)
al : vert et petite taille (size=40)
lio : bleu et taille moyenne (siez=60)
Liens en pointillés avec jo-al de couleur rouge
al-lio de couleur bleue
jo-lio de couleur noire


'''
import pdb
import networkx as nx
import matplotlib.pyplot as plt
g=nx.Graph()
print(type(g))

##on ajoute les 3 noeuds avec leurs attributs
# Possiblité de rentrer un noeud après l'autre
#Méthodes .add._node et .noce - cf example1.py

g.add_nodes_from([('A',{'color':'red','size':175 ,'label':'jo'})
    ,('B',{'color':'green','size':40 ,'label':'al'})
    ,('C',{'color':'blue','size':60 ,'label':'lio'})])

## On crée les liens avec leur attribut
# Possibilité de rentrer un lien après l'autre
# la méthode .add_edge - cf exemple1.py

g.add_edges_from([('A','B',{'color':'red'})
,('B','C',{'color':'blue'})
,('C','A',{'color':'black'})])


## Couleur des noeuds
# Méthode équivalente avec g.node.keys() - cf exemple1.py

Node_Color=[]
for n in g.nodes(data=True):
    Node_Color.append(n[1]['color'])

## Taille des noeuds
# Méthode équivalente avec g.node.keys() - cf exemple1.py

Node_Size=[]
for n in g.nodes(data=True):
    Node_Size.append(n[1]['size'])



## Label des noeuds (dictionnaire)
# Méthode équivalente avec g.node.keys() - cf exemple1.py

Node_Label={}
for n in g.nodes(data=True):
    Node_Label[n[0]]=n[1]['label']

    
## Couleur des liens
    
Edge_Color=[]
for e in g.edges(data=True):
    Edge_Color.append(e[2]['color'])


## Taille du graphe
plt.figure(figsize=(5,4))


## Caractéristiques du graphe
# style : definir le lien (trait plein, pointillé...)
# alpha : niveau de transparence des liens et n÷uds
nx.draw(g)

'''
node_color=Node_Color,node_size=Node_Size,
labels=Node_Label,edge_color=Edge_Color,alpha=0.30,style='dashed')


## Titre du graphe
plt.title('Mon premier graphe', size=10)


## Retirer les axes abscisse et ordonnée
plt.axis('off')


## Nom et format du fichier enregistré
plt.savefig('first_graph.pdf', format='pdf')

'''
