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

- Logical rules: A database of logical relationships of concepts.
- Semantic network: A graph consisting of concepts as nodes and their relations as vertices. The semantic network can also represent the data in logical database, but has greater expressiveness.
- Frame representation: A frame is a record containing many attributes related to the real world objects. It would be an object in the object oriented language. The connections between frames can create a graph like structures.

The Greek philosopher Aristotle defined a framework of rational thinking by defining logical syllogisms, the patterns for arguments which always produces correct conclusions, provided that the premises are correct. Much later, it was proposed that an artificial machine could use these kinds of logical rules and the database of premises to draw conclusions. The premises and the rules creates a logical database and a program can use it to make queries to find out if some statements are true or false. Many AI systems are made using this approach. Practical problems are that it is a lot of work to encode the complete set of premises and logical rules of a practical case into the database, and solving complex queries may need too much computational resources to be efficient. In addition the traditional logic does not support the concept of uncertainty.



### Logics database

- Inference engine
- Resolution
- Backward chaining
- Forward chaining
- Belief network

## Classical AI:

Expert systems were supposed to be able to make decisions on behalf of a person. They consisted of a large number of logical rules stored in the knowledge database, which was used to resolve true statements based on the facts perceived and the rules stored. They are still used in certain applications, like in a bird recognition system [www.luontoportti.fi](Luontorportti).

The bird species can be recognized by searching true statements from the database of logical rules. Each observation rules out part of the possible species.


    If (color is white)                 (A)
        and (wings are dark)            (B)
        and (size equals to crow)       (C)
        and (circulates in the air)     (D)
        and (swims in water)            (E)
    then it is a seagull                (Q)

The above can be shown mathematically as

$$
    A \wedge B \wedge C \wedge D \wedge E \rightarrow Q
$$

The knowledge database or knowledge base (KB) of Luontoportti is build in the opposite diretion though using simple logical rules as follows:

$$
\begin{eqnarray}
    \mathrm{KB} = ( Q &\rightarrow& A, \\
        Q &\rightarrow& B, \\
        Q &\rightarrow& C, \\
        Q &\rightarrow& D, \\
        Q &\rightarrow& E )
\end{eqnarray}
$$

The inference shown above can be made from the KB using propositional logics, for example a method called resolution. Logical inference follows

The knowledge database above can be used in both directions.

- If we know the species, we can find out the properties, for examples it can be seen that seagulls are white. This kind of inference is called as *forward chaining*, or *prediction*, because it predicts the properties or perceptions based on the species. Example in the medical field would be to describe the symptoms when the diagnosis is known.
- If we on the other hand know the perceptions, we can use the database to find out the species where the observations fit. This kind of inference is called as *backward chaining* or *diagnostics'. In medical field this is used for diagnosing the cause, the disease, when the symptoms are known.

The inference using logics KB is carried out by searching. Exhaustive search by trying all possible solutions is the simplest method, but it uses plenty of resources and is unfeasible in most practical databases.

### Propability

Medical diagnosis, current care guidelines (käypähoitosuositukset)

The symptoms for having a stroke or TIA
- One sided face paralysis
- difficulties to speak (afasia)
- one eye vision problems
- nausea
- double images in vision
- difficulties to swallow

Each symptom increases the propability of the diagnosis. A different probability may be involved in each symptom and connection with a stroke

Some symptoms are very common in many conditions, like nausea. Therefore their specificity is low, and their power for predicting stroke is therefore low.

One sided face paralysis is on the other hand rare in other conditions, and therefore its specificity is high, and it is a good symptom for diagnosing stroke. If one does not have this symptom, it may be reduce the hypothesis that the stroke is the cause for other symptoms.

Properties
- Human knowledge is expressed as rules

Cons
- gathering the rules is awkward, difficult for real world cases and impossible for complex cases
- combinatorial explosion follows

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


- Markov model
- Neural network
- Deep learning


## Read more

> Programming is a superpower

- Harrison  [Python programming](https://pythonprogramming.net)

-  Daniele Paliotta, [Introduction to Reinforcement Learning with Python](https://stackabuse.com/introduction-to-reinforcement-learning-with-python/)

- Harrison  [Q-Learning introduction and Q Table - Reinforcement Learning w/ Python Tutorial p.1](https://pythonprogramming.net/q-learning-reinforcement-learning-python-tutorial/)

- Harrison [Introduction - Self-driving cars with Carla and Python part 1](https://pythonprogramming.net/introduction-self-driving-autonomous-cars-carla-python/)
