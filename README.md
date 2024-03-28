# Aberway
The code for the Aberway hackathon.

## Directory structure
- `trial`: Directory containing all of the trials that were done during the hackathon
- `aberway_background_code.py`: Main `pygame` code from the organisers
- `data.py`: File containing graph data to traverse
- `generate_graph.py`: File containing code to generate graph data structure
- `ida.py`: Main algorithm (IDA*) file 
- `main.py`: Main file to run the pytest simulation
- `test_algo.py`: Pytests containing the test cases from the organisers

## Replicating results
- Install the dependencies
    ```
    $ pip install -r requirements.txt
    ```
- Run the simulation
    ```
    $ python main.py
    ```
- Ensure the algorithm passes all of the test cases
    ```
    $ pytest
    ```


## Hackathon details
Participants are tasked with finding a path when given a starting position, some nodes that the path must cross through, and the length of the path. From that, the participants must find the path that starts at the starting position, goes through the given nodes, and ends on a node. 

### Tasks:
#### Example A
A Delivery Person (referred to as “DP” from now on) at the Post Office at node 0. DP has a few mandatory packages to deliver that need to be delivered today, those are at nodes 10, 11, and 14. DP’s van only has 676.75 ±0.06 fuel. It is important that DP runs out of fuel at a Place where DP can stop (any node) so that DP can refill the van’s fuel with a fuel canister, so DP can not stop in the middle of the road. Find the path that DP must take, and where DP will have to refuel.

**Values:**

Start Position: 0 

List of nodes their path must cross: `[10,11,14]`

Length (AKA Final weight): 676.75 ±0.06

Correct answer: `0, 2, 10, 13, 11, 14, 15`

#### Example B
Jack (referred to as “J” from now on) is going to go on a run, J will travel 758.97 ±0.06 far. J wants to pass by a street newspaper seller at node 34, J also wants to pass by his favourite ice cream shop at node 27, and run past the dog park at 17. J is self conscious and has to stop running at a node not in the middle of a road. Find the path that J must take, and where J will finish his run.

**Values:**

Start Position: 29

List of nodes their path must cross: `[34, 27, 17] `

Length (AKA Final weight): `758.97 ±0.06`

Correct Answer: `29, 33, 34, 27, 18, 17, 10`


#### Example C
An ice cream van (referred to as “ICV'' from now on) starts at node 53, ICV has 1038.42 ±0.07 fuel and wants to stop by some parks at nodes 54, 51, 38, and 36. What path should ICV take to make sure it runs out of fuel at a node?

**Values:**
Start Position: 53

List of nodes their path must cross: `[54, 51, 38, 36]`

Length (AKA Final weight): `1038.42 ±0.07`

Correct answer: `53, 54, 51, 41, 38, 37, 36, 43`

#### Example D
A Police Officer in a car (referred to as “PO” from now on) starts at the police station at 47. PO has to meet the quota of travelling 2044.79 ±0.14. PO needs to make sure nodes 34, 19, 0,  and 12 are safe. When PO finishes their route, they need to stop and contact the police station, so PO must stop on a Node. What path will the POtake? And What node will PO end on?

**Values:**

Start Position: 47

List of nodes their path must cross: `[34, 19, 0, 12]` 

Length (AKA Final weight): `2044.79 ±0.14`

Correct answer: `47, 45, 43, 42, 37, 34, 27, 26, 19 ,9, 3, 0 ,2, 11, 12`

 

#### Participants Resources:
Base map

![alt text](map.png)
Inverted Base map

![alt text 2](mapI.png)

Map with the node numbers

![alt text 3](mapWithNodeNumbers.png)

#### Base Code
The basecode can be found in the `YourName__AberWay.py` file.

#### Presentation Slides 

If you'd like to revist the slides during the presentation, please use this link 
https://docs.google.com/presentation/d/1Crw7Cx9DMLbHH3xeuuz369dOOmhtPXVfVP9PtoSWJFE/edit?usp=sharing

