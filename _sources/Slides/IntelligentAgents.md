---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

+++ {"slideshow": {"slide_type": "slide"}}

 <img src="kuvat/Clarke.png" height="200" align="right"/>

> Any sufficiently advanced technology is indistinguishable from magic.

  / Arthur C. Clarke
 

```{code-cell} ipython3

```

+++ {"slideshow": {"slide_type": "fragment"}}

The explanations like:
 - This image recognition is based on Deep Neural Networks, or
 - This prediction is based on Support Vector Regresssion 
 
Are equal to "it is magic", if one does not understand AI. 

+++ {"slideshow": {"slide_type": "fragment"}}

On the contrary to traditional magic, this course is going to reveal the tricks of the magicians who use AI tools.

+++ {"slideshow": {"slide_type": "slide"}}

 <img src="kuvat/robot.png" height="200" align="right"/>

# Intelligent agents

One convenient abstraction for discussing AI is so called intelligent agent.

+++ {"slideshow": {"slide_type": "subslide"}}

## Intelligent agents

An intelligent agent is something which acts and tries to pursue goals. An artificial intelligent agent is a machine or software. It has often sensors, to perceive the world and it may make actions to interact with the world

![image.png](kuvat/intelligent_agents.png)


The basic concept of an intelligent agent. It has sensors to measure information about the world (perception), it uses the information and it's internal state to make intelligent decisions and performs actions using its actuators to affect to the world.

+++ {"slideshow": {"slide_type": "subslide"}}

**Definition**:
A rational agent is an agent which always selects an action that is expected to maximize its performance measure based on its perceptions and build in information about the world.

+++ {"slideshow": {"slide_type": "fragment"}}

**Discussion topic:**
Can an intelligent agent be meaningful without perception or actuator or neither?

+++ {"slideshow": {"slide_type": "fragment"}}

**Discussion topic**:
If two rational agents both maximize their performance measure based on their perceptions and build in information, can one be better than another?

+++ {"slideshow": {"slide_type": "subslide"}}

Intelligent agents can be divided in four classes based on their cognitive abilities and level of sophistication:

1. Simple reflex agents
1. Model based agents
1. Goal based agents
1. Utility based agents

+++ {"slideshow": {"slide_type": "subslide"}}

### Simple reflex agents
 - These agents are reactive systems
 - perform simple actions based on their perception 
 
One example of really simple agent of this kind is a motion sensor based outdoor light controller:

$$
  \mbox{Light} = \begin{cases}
    1, & \mbox{if (dark AND movement_observed)} \\
    0, & \mbox{otherwise }
  \end{cases}
$$

- Operation is based on a simple logical rule to combine two input variables to make a decision for taking an action. 
- In general the decision system can be arbitrary complex and include also many other inference methods than logics.
- Because the agent acts based only on its perceptions it will run into troubles if the world is only partially observable.

+++ {"slideshow": {"slide_type": "subslide"}}

The simple reflex agent makes its decisions based only on the perceptions and decision rules.

![image.png](kuvat/reflex_agents.png)

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
from Agent import getSunlight, readMovementSensor, SwitchLighting

# Loop forewer
while True:
    # Perceptions
    Light = getSunlight()
    Movement = readMovementSensor()
    
    # Decision making
    if (Light < 0.25) and (Movement==True):
        LightState=1
    else:
        LightState=0
        
    # Action
    SwitchLighting(LightState)
    
    # Do it again :-)
```

+++ {"slideshow": {"slide_type": "subslide"}}

### Model based reflex agents
 - In addition to perception and actuators, the model based agent uses a model which describes some necessary behavior of the world. 
 - With the model, the agent "understands" something about how the world behaves, and can make predictions on how the actions changes the world. 
 - If the world is only partially observable, the agent can build a model which covers also the concealed information.

For example the collision avoidance system of an autonomous car can predict that even though the cars are still far away from each other, a collision is happening after a certain time, because the velocity of the car in front drives slower. The time to the collision can be estimated using physics:

$$
   t = \frac{\Delta s}{v_s - v_o}
$$ 

+++ {"slideshow": {"slide_type": "subslide"}}

 - In this case, the agent needs to perceive 
   - the distance between cars using a radar, for example 
   - its own speed by GPS. 
 - It uses it's own physical model to estimate the time for collision $ t = \frac{\Delta s}{v_s - v_o}$
 - it may decide to apply necessary breaking force by activating breaks.
 - The agent would probably need some model of Newton mechanics to estimate the effect of the breaking force to the car speed. $F=m\cdot a$

An automated vehicle could have a model of the roads in the city and it can therefore turn from the current road to the named street from the right crossing.

+++ {"slideshow": {"slide_type": "subslide"}}

![image.png](kuvat/modelbased_agents.png)

In addition to peceptions and decision rules, the model based agent has also a model and state of the world to allow it to make more complex decisions than the simple reflex agent.

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
from Agent import findObstacle, getDistanceToObstacle, Break

# State consist of current acceleration and speed. Lets initialize them
v=20  # Speed [m/s]
a=0   # Acceleration [m/s²]
m=1200 # The mass of the car [kg]

# Loop forewer
while True:
    # Perceptions
    obstacle = findObstacle()
    Delta_s = getDistanceToObstacle()
    
    # State consist of current acceleration and speed
    # a, v
    
    # Decision making
    if obstacle:
        if Delta_s < 100:
            Delta_t = Delta_s/v
            a = v / Delta_t
            F=m*a
    else:
        F=0
        a=0

    # Action: Apply breaks if F>0
    Break(F)
    
    # Do it again :-)
```

+++ {"slideshow": {"slide_type": "subslide"}}

### Goal based agents

The goal based agents are not only reacting to the current situation but instead they plan to reach their goals. The planning usually demands a model which they can use for searching action sequences for reaching the goal. For example autonomous taxi can find a way to the target by searching it's model (the map) and can carry out actions (steering) to reach the goal.

![image.png](kuvat/goal_agents.png)


The goal based agents can also assess the probable consequences of their actions and they are therefore capable of planning.

+++ {"slideshow": {"slide_type": "subslide"}}

### Utility based agents

Utility, the fitness or worth for some purposes. An action has higher utility if it is more usefull or leads to smaller losses in the given situation. The goal of the optimization is to maximize the utility. Exactly symmetrical optimization goal is to minimize losses, since losses are negative utility and utility is negative loss. Utility based agents try to behave so that the utility gained by their actions is maximized. In other words, they try to reach their goal in an optimal way.

![image.png](kuvat/utility_agents.png)

The utility agents extend the goal and model based agents by also considering the utility what is gained by reaching the goal through different action sequences.

+++ {"slideshow": {"slide_type": "subslide"}}

For example, an automated vehicle controlled by a utility based agent would try to find an optimal path from the current location to the destination. The utility could be for example the negative of time spend or fuel consumed, or a combination of both. The agent may have many optional actions to take, and the utility agent selects the one which according to it's knowledge or beliefs leads to higher utility.

+++ {"slideshow": {"slide_type": "subslide"}}

### Learning agents

Alan Turing estimated in 1950 the amount of programming needed to gain AI. According to methods of 50's, he estimated that programming of AI which had similar capabilities than a person would take 50 years. He concludes that *Some more expeditious method seems desirable*, and proposes a learning machine 

In contrast to programmed AI, the learning AI learns the rules behind the actions without explicit programming. The benefits are that the agent can operate in an environment, which is initially unknown. In a long run it can also learn rules which would be very complex to program. 

The structure of the learning agent is consisted of the following four components
1. *Performance element*
1. *Critic element*
1. *Learning element*
1. *Problem generator*

+++ {"slideshow": {"slide_type": "subslide"}}

![image.png](kuvat/learning_agents.png)

1. *Performance element* receives perceptions from the sensors and carries out actions by using actuators. This element includes the operations of the previously described agents, but here it also exhanges information with the learning element and receives suggestions from the problem generator.
1. *Critic element* observes the perceptions and uses the performance standard to assess how well the agent is performing and provides that information to the learning element. 
1. *Learning element* is responsible on making improvements on the performance element according to the feedback received from the citic element.
1. *Problem generator* suggests actions leading to new and informative experiences to explore the world to find even better solutions in the long run.

+++ {"slideshow": {"slide_type": "subslide"}}

![image.png](kuvat/learning_agents.png)


The learning agents extend the previous agents by adding a critic, learning and problem generator elements. The critic element provides feedback to the learning element, which updates the performance element. The learning element sets new learning goals to the problem generator, which suggest new exploratory actions to the performance element to explore unknown ares of the world.

+++ {"slideshow": {"slide_type": "subslide"}}

**Discussion topic**
Can any agent act meaningfully if a world is not observable at all?


**Discussion topic**
How would an autonomous car or vacuum cleaner would work, if it was simple reflex, model based goal based or utility based agent? How would learning change the behaviour?

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
print("The End")
```
