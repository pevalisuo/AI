---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: 1.4.1+dev
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

Block diagram of AI
====================


## Knowledge representation

### Logics database

Logical inference
Resolution

### Graphs

```{code-cell} ipython3
:tags: ["hide-input"]
:caption: A random graph

import matplotlib.pyplot as plt
import networkx as nx

G = nx.random_geometric_graph(200, 0.125)
# position is stored as node attribute data for random_geometric_graph
pos = nx.get_node_attributes(G, 'pos')

# find node near center (0.5,0.5)
dmin = 1
ncenter = 0
for n in pos:
    x, y = pos[n]
    d = (x - 0.5)**2 + (y - 0.5)**2
    if d < dmin:
        ncenter = n
        dmin = d

# color by path length from node near center
p = dict(nx.single_source_shortest_path_length(G, ncenter))

plt.figure(figsize=(8, 8))
nx.draw_networkx_edges(G, pos, nodelist=[ncenter], alpha=0.4)
nx.draw_networkx_nodes(G, pos, nodelist=list(p.keys()),
                       node_size=80,
                       node_color=list(p.values()),
                       cmap=plt.cm.Reds_r)

plt.xlim(-0.05, 1.05)
plt.ylim(-0.05, 1.05)
plt.axis('off')
plt.show()

```

A graph is simply a structure which has nodes (also called as vertices) which are connected to each other with edges (lines). The edges can be unidirectional (arrows) or bi-directional (lines). A graph with unidirectional edges is called as directed graph, whereas a graph containing only bi-directional edges is called undirected graph. If the graph contains cycles (or loops), it is said to be a cyclic graph. If it has no cycles, the graph is acyclic graph. If the graph contains a path between each nodes, the graph is said to be connected, otherwise it contains isolated sections and it is called disconnected.
Acyclic connected graph is called as tree and acyclic disconnected graph as forest.

Examples of different graphs are shown in Figures {numref}`fig:nondiag_graph` - {numref}`fig:treegraph`.

Mathematically, a graph $G$ is expressed as a set of Edges $E$ and vertices $V$:

$$
  G=(V,E)
$$ (eq:graph)

```{figure} figures/graafi_nondirectional.svg
---
width: 600px
align: center
name: fig:nondiag_graph
---

An example of cyclic undirected graph.
```


```{figure} figures/graafi_cyclic.svg
---
width: 300px
align: center
name: fig:cyclicraph
---

An example of a directed cyclic graph.
```


```{figure} figures/graafi_DAG.svg
---
width: 300px
align: center
name: fig:treegraph
---

An example of a directed a-cyclic graph (DAG), a directed tree.
```



```{code-cell} ipython3
:tags: ["hide-input"]
:caption: A random graph

rg=nx.random_tree(15)
nx.draw(rg, with_labels=True, font_weight='normal', node_color='orange', node_size=500)
```


#### Graph Search methods

When planning actions using a graph, a graph search algorithm is often used.

- Breadth First
- Depth First
- Heuristic function
- Greedy algorithms
- Hill climbing
- Optimisation

## Learning

- On-line learning
- Machine learning
- Deep learning
