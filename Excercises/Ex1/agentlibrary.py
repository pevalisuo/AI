import numpy as np
from numpy import sin, cos, pi
import matplotlib.pyplot as plt

from matplotlib import animation, rc
from IPython.display import HTML

import matplotlib.pyplot as plt
import networkx as nx

from numpy import log2

#%load_ext autoreload
#%autoreload 2

class autonomousCar:

    def __init__(self):
        # First set up the figure, the axis, and the plot element we want to animate
        fig, ax = plt.subplots(figsize=(10,4))

        Length=500

        ax.set_ylim(( -55,55))
        ax.set_xlim((0, Length))

        line, = ax.plot([], [], lw=2, linestyle=':', color='blue')
        left_border, = ax.plot([0,Length], [-50,-50], color='black')
        right_border, = ax.plot([0,Length],[50,50], color='black')
        center, = ax.plot([0,Length], [0,0], color='black', linestyle='--')
        
        self.fig=fig
        self.ax=ax
        self.Length=Length
        self.line=line
        self.reset()
        self.penalty=0

    def reset(self):
        self.speed=1
        self.direction=30
        self.x=0
        self.y=-25
        self.xdata=[]
        self.ydata=[]
        self.line.set_color('blue')
        self.line.set_data([], [])
        return (self.line,)
        
    def steer(self, left, right):
        """ Dummy always streight forward steering method """
        return(0)
        
    def getPenalty(self):
        """ Return the ratio of penalized steps / all steps in percents"""
        if self.penalty>self.Length:
            return(100)
        else:
            return(100*self.penalty/self.Length)

    # animation function. This is called sequentially
    def animate(self, i):
        global x,y,speed,direction,xdata,ydata

        self.x = self.x + self.speed * cos(self.direction/180*pi)
        self.y = self.y + self.speed * sin(self.direction/180*pi)
        
        left = (self.y>-5)
        right = (self.y<-45)
        if left or right:
            self.penalty=self.penalty+1
        steering = self.steer(left, right)
        if steering>40:
            steering=40
        if steering<-40:
            steering=-40
        self.direction += self.speed*0.1*steering
        
        self.xdata.append(self.x)
        self.ydata.append(self.y)
        
        self.line.set_data(self.xdata, self.ydata)
        if (self.y>0) or (self.y<-50):
            self.line.set_color('red')
            self.penalty=self.Length
        return (self.line,)

    def run(self):
        # call the animator. blit=True means only re-draw the parts that have changed.
        self.anim = animation.FuncAnimation(self.fig, self.animate, 
            init_func=self.reset, frames=self.Length, 
            interval=20, blit=False)
            
class UtilityGraph(object):
    
    def makeNodes(self, Nnodes):
        return([chr(x) for x in range(ord('A'), ord('A')+Nnodes)])

    def makeEdges(self, nodes):
        edges=[]
        k=1
        for i in range(len(nodes)):
            for j in range(2):
                if k<len(nodes):
                    edges.append((nodes[i], nodes[k]))
                    k+=1
            if k>=len(nodes):
                break     
        return edges
        
    def getWeights(self,nWeights):
        w=np.random.rand(nWeights)*0.8+0.1
        for i in range(0, len(w), 2):
            s=w[i]+w[i+1]
            w[i]=w[i]/s
            w[i+1]=w[i+1]/s
        return w.round(2)

    def getPositions(self, Nnodes):
        pos=[]
        for i in range(Nnodes): 
            if i==0:
                row=0
                col=0
                x,y=0,0
            else:
                row=int(log2(i+1)) 
                col=(i+1)-2**row 
                sep=40/(2**(row-1))
                width=((2**row)-1)*sep
                y=row*-10 
                x=0-width/2+col*sep
            pos.append((x,y))
        return pos
    
    def __init__(self, Nnodes=7):
        G=nx.DiGraph()
        
        N=Nnodes
        nodes=self.makeNodes(N)
        pos=self.getPositions(N)
        edges=self.makeEdges(nodes)
        weights=self.getWeights(len(edges))
        
        for i in range(len(nodes)):
            G.add_node(nodes[i], pos=pos[i])
        for i in range(len(edges)):
            G.add_edge(edges[i][0], edges[i][1], weight=weights[i])
        self.G=G
        self.clearBets()
        
    def plot(self):
        pos=nx.get_node_attributes(self.G,'pos') 
        nx.draw_networkx(self.G, with_label = True, pos=pos)
        labels = nx.get_edge_attributes(self.G,'weight')
        nx.draw_networkx_edge_labels(self.G,pos,edge_labels=labels)
        
    def getDistances(self):
        return dict(nx.all_pairs_dijkstra_path_length(self.G, 
                weight='weight'))['A']
    
    def getProbabilities(self):
        nodes=set(self.G.nodes)
        source='A'
        targets=nodes-set(source)
        d=dict()
        prob=nx.get_edge_attributes(self.G, 'weight')          
        for target in targets:
            path=nx.shortest_path(self.G, source, target)
            edges=list(zip(path, path[1:]))
            p=1
            for edge in edges:
               p*=prob[edge]
            d[target]=p
        return d
        
    def clearBets(self):
        for room in set(self.G.nodes):
            self.G.nodes[room]['value']=0
        
    def placeBet(self, rooms, values):
        self.clearBets()
        
        # Check the total sum
        if(sum(values)!=100):
            print("Error! The total sum must be 100€, now it is %d€" %
                sum(values))
            return
        
        nodes=set(self.G.nodes)
        
        # Check that the room names are correct
        for room in rooms:
            if room not in nodes:
                print("Error! Wrong room name: %s!" % room)
                return
        
        for i in range(len(rooms)):
            room=rooms[i]
            value=values[i]
            self.G.nodes[room]['value']=value
        
    def simulate(self):
        
        # Play two rounds
        N=10
        collectedMoney=np.zeros(N)
        for round in range(N):
            # Start from the root
            agentNode='A'
            depth=0
            path=agentNode

            # Get the money from starting node
            collectedMoney[round]+=self.G.nodes[agentNode]['value']
            
            # Go deeper
            while(len(list(self.G.successors(agentNode)))>0):
                depth+=1
                
                # Select next node
                successors=list(self.G.successors(agentNode))
                probs=[self.G.get_edge_data(agentNode, successors[i])['weight'] 
                    for i in range(len(successors))]
                r=np.random.rand(1)[0]
                cumprob=0
                for i in range(len(successors)):
                    cumprob += probs[i]
                    if cumprob >= r:
                        agentNode=successors[i]
                        # Get the money from the new node
                        collectedMoney[round]+=self.G.nodes[agentNode]['value']
                        path += "," + agentNode
                        break
            print("The path of the robot in round %d is:" % (round), path)
            
        #Return remaining funds
        return 100-collectedMoney.mean()

if __name__=='__main__':
    UG=UtilityGraph(7)
    UG.clearBets()
    UG.placeBet(['D', 'E', 'F', 'G'], [25, 0, 25, 50])
    UG.simulate()
    
            

            
