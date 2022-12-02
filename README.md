<h1 align="center">Traveling Salesperson Problem</h1> 


<a href=""><img width="990" height="600" align='center' src="https://github.com/DiegoHurtad0/USA-Traveling-Salesman-Tour/blob/main/output/USATravelingSalesmanProblem.png?raw=true?raw=true"></a>
<h3 align="center">Efficient route planning for travelling salesman problem for 48 USA States</h3> 

<h2 align="left">TSP</h2> 
The Traveling Salesman Problem (TSP) is one of the most widely studied combinatorial optimization problems. Its statement is deceptively simple, and yet it remains one of the most challenging problems in Operational Research. Laporte, G et al.


The TSP consists of determining a minimum distance circuit passing through each vertex once and only once. Such a circuit is known as a tour or Hamiltonian circuit (or cycle)

Many methods have been used to solve routing problem, because of the complexity of the problem (NP-hard), in some cases exact methods, but usually metaheuristics, classic heuristics.  D. Hurtado-Olivares et al.

<h3 align="left">Exact algorithms:</h3> 

A large number of exact algorithms have been proposed for the TSP. These can be best understood and explained in the context of integer linear programming (ILP)
This section presents an example that shows how to solve the Traveling Salesperson Problem (TSP) for the locations shown on the map below.


<h3 align="left">Heuristic algorithms:</h3>

Since the TSP is a NP-hard problem, it is natural to tackle it by means of heuristic algorithms.  TSP heuristics can be classical into tour construction procedures which involve gradually building a solution by adding a new vertex at each step, and tour improvement procedures which improve upon a feasible solution by performing various exchanges performance. Laporte, G et al.

Heuristic methods often produce a near-optimal solution or the optimal solution in some cases; in large problems, they produce a good solution in a reasonable amount of computer time D. Hurtado-Olivares et al.

In combinatorial optimization, the aim is to move from a given initial solution to a minimumcost solution, by performing gradual changes to the starting solution. 

<h3 align="left">Solving the Traveling Salesman Problem with or-tools from Google [3]</h3> 

<h3 align="left">Routing model with Solvers</h3> 

This section describes some of the options for the routing solver from Google

<h3 align="left">First solution strategy</h3> 

The first solution strategy is the method the solver uses to find an initial solution. The following table lists the options for first_solution_strategy. [4]


|       Algorithm         |        Description     	  |
|:----------------------:	|:------------------------:	|
|      AUTOMATIC        	|        Lets the solver detect which strategy to use according to the model being solved.       	  |
|      PATH_CHEAPEST_ARC        	|        Starting from a route "start" node, connect it to the node which produces the cheapest route segment, then extend the route by iterating on the last node added to the route.       	  |
|      PATH_MOST_CONSTRAINED_ARC        	|        Similar to PATH_CHEAPEST_ARC, but arcs are evaluated with a comparison-based selector which will favor the most constrained arc first. To assign a selector to the routing model, use the method ArcIsMoreConstrainedThanArc().       	  |
|      EVALUATOR_STRATEGY        	|        Similar to PATH_CHEAPEST_ARC, except that arc costs are evaluated using the function passed to SetFirstSolutionEvaluator().       	  |
|      SAVINGS        	|        Savings algorithm (Clarke & Wright). Reference: Clarke, G. & Wright, J.W.: "Scheduling of Vehicles from a Central Depot to a Number of Delivery Points", Operations Research, Vol. 12, 1964, pp. 568-581.       	  |
|      SWEEP        	|        	Sweep algorithm (Wren & Holliday). Reference: Anthony Wren & Alan Holliday: Computer Scheduling of Vehicles from One or More Depots to a Number of Delivery Points Operational Research Quarterly (1970-1977), Vol. 23, No. 3 (Sep., 1972), pp. 333-344.       	  |
|      CHRISTOFIDES        	|        Christofides algorithm (actually a variant of the Christofides algorithm using a maximal matching instead of a maximum matching, which does not guarantee the 3/2 factor of the approximation on a metric travelling salesperson). Works on generic vehicle routing models by extending a route until no nodes can be inserted on it. Reference: Nicos Christofides, Worst-case analysis of a new heuristic for the travelling salesman problem, Report 388, Graduate School of Industrial Administration, CMU, 1976.       	  |
|      ALL_UNPERFORMED        	|        Make all nodes inactive. Only finds a solution if nodes are optional (are element of a disjunction constraint with a finite penalty cost).       	  |
|      BEST_INSERTION        	|        Iteratively build a solution by inserting the cheapest node at its cheapest position; the cost of insertion is based on the global cost function of the routing model. As of 2/2012, only works on models with optional nodes (with finite penalty costs).       	  |
|      PARALLEL_CHEAPEST_INSERTION        	|        Iteratively build a solution by inserting the cheapest node at its cheapest position; the cost of insertion is based on the arc cost function. Is faster than BEST_INSERTION.       	  |
|      LOCAL_CHEAPEST_INSERTION        	|        Iteratively build a solution by inserting each node at its cheapest position; the cost of insertion is based on the arc cost function. Differs from PARALLEL_CHEAPEST_INSERTION by the node selected for insertion; here nodes are considered in their order of creation. Is faster than PARALLEL_CHEAPEST_INSERTION.       	  |
|      GLOBAL_CHEAPEST_ARC        	|        Iteratively connect two nodes which produce the cheapest route segment.       	  |
|      LOCAL_CHEAPEST_ARC        	|        Select the first node with an unbound successor and connect it to the node which produces the cheapest route segment.       	  |
|      FIRST_UNBOUND_MIN_VALUE        	|        elect the first node with an unbound successor and connect it to the first available node. This is equivalent to the CHOOSE_FIRST_UNBOUND strategy combined with ASSIGN_MIN_VALUE (cf. constraint_solver.h).       	  |

<h3 align="left">Local search options:</h3>

The following table lists the options for local search strategies (also called metaheuristics). See Changing the search strategy for examples of setting these options. [4]

|       Algorithm         |        Description     	  |
|:----------------------:	|:------------------------:	|
|      AUTOMATIC        	|       Lets the solver select the metaheuristic.       	  |
|      GREEDY_DESCENT        	|       Accepts improving (cost-reducing) local search neighbors until a local minimum is reached.       	  |
|      GUIDED_LOCAL_SEARCH        	|       Uses guided local search to escape local minima (cf. http://en.wikipedia.org/wiki/Guided_Local_Search); this is generally the most efficient metaheuristic for vehicle routing.       	  |
|      SIMULATED_ANNEALING        	|       Uses simulated annealing to escape local minima (cf. http://en.wikipedia.org/wiki/Simulated_annealing).       	  |
|      TABU_SEARCH        	|       Uses tabu search to escape local minima (cf. http://en.wikipedia.org/wiki/Tabu_search).       	  |
|      GENERIC_TABU_SEARCH        	|       Uses tabu search on the objective value of solution to escape local minima.       	  |

<h3 align="left">Routing Options:</h3>

This section describes some of the options for the routing solver.

<h3 align="left">Search limits:</h3>

Search limits terminate the solver after it reaches a specified limit, such as the maximum length of time, or number of solutions found. You can set a search limit through the solver's search parameters. See Time limits for an example.

The following table describes the most common search limits.

|       Name              |        Type       	      |        	Description       	|  
|:----------------------:	|:------------------------:	|:----------------------:	|
| solution_limit          |int64                      |        Limit to the number of solutions generated during the search.      	  |
| time_limit.seconds      |int64                      |        Limit in seconds to the time spent in the search.      	  |
| lns_time_limit.seconds  |int64                      | Lmit in seconds to the time spent in the completion search for each local search neighbor.|


<h3 align="left"> Algorithm performance:</h3>

Comparing the different algorithms with some fixed data of 45 states of USA, there were some interesting results attached below:

Limit in seconds to the time spent in the search was 5 min for each Algorithm


<h3 align="left">First solution strategy:</h3>

The first solution strategy is the method the solver uses to find an initial solution. The following table lists the options for first_solution_strategy.

|       Algorithm Type    |        Algorithm       	  |   Objective Function    |        	Time min       	|   Solver        |
|:----------------------:	|:------------------------:	|:----------------------:	|:----------------------:	|:-----------------:	
|      AUTOMATIC        	|        AUTOMATIC       	  |        17, 418      	  |        0       	        |Google Ortools   |
| AUTOMATIC               |   PATH_CHEAPEST_ARC   	  |        17, 418      	  |        0       	        |Google Ortools   |
| First solution strategy |PATH_MOST_CONSTRAINED_ARC  |        17, 418      	  |        5       	        |Google Ortools   |
| First solution strategy |EVALUATOR_STRATEGY         |        17, 591      	  |        0       	        |Google Ortools   |
| First solution strategy |SAVINGS                    |  ROUTING_NOT_SOLVED     |        0       	        |Google Ortools   |
| First solution strategy |SWEEP                      |  ROUTING_NOT_SOLVED     |        0       	        |Google Ortools   |
| First solution strategy |CHRISTOFIDES               |  ROUTING_NOT_SOLVED     |        0       	        |Google Ortools   |
| First solution strategy |ALL_UNPERFORMED            |        17, 418      	  |        0       	        |Google Ortools   |
| First solution strategy |BEST_INSERTION             |  ROUTING_NOT_SOLVED     |        0       	        |Google Ortools   |
| First solution strategy |PARALLEL_CHEAPEST_INSERTION|  ROUTING_NOT_SOLVED     |        0       	        |Google Ortools   |
| First solution strategy |LOCAL_CHEAPEST_INSERTION   |  ROUTING_NOT_SOLVED     |        0       	        |Google Ortools   |
| First solution strategy |GLOBAL_CHEAPEST_ARC        |        17, 418      	  |        0       	        |Google Ortools   |
| First solution strategy |LOCAL_CHEAPEST_ARC         |        17, 062      	  |        5       	        |Google Ortools   |
| First solution strategy |FIRST_UNBOUND_MIN_VALUE    |  ROUTING_NOT_SOLVED     |        0       	        |Google Ortools   |


<h3 align="left">Local search options:</h3>

The following table lists the options for local search strategies (also called metaheuristics). See Changing the search strategy for examples of setting these options.

|       Algorithm Type    |        Algorithm       	  |   Objective Function    |        	Time min       	|   Solver        |
|:----------------------:	|:------------------------:	|:----------------------:	|:----------------------:	|:-----------------:	
| Local search options    |GREEDY_DESCENT             |        17, 418      	  |        5       	        |Google Ortools   |
| Local search options    |GUIDED_LOCAL_SEARCH        |        17, 102      	  |        5       	        |Google Ortools   |
| Local search options    |SIMULATED_ANNEALING        |        17, 622      	  |        5       	        |Google Ortools   |
| Local search options    |TABU_SEARCH                |        17, 121      	  |        5       	        |Google Ortools   |
| Local search options    |GENERIC_TABU_SEARCH        |        17, 418      	  |        5       	        |Google Ortools   |


<h3 align="left">Visualization of Routes: </h3>

<a href=""><img width="480" height="550" align='left' src="https://github.com/DiegoHurtad0/USA-Traveling-Salesman-Tour/blob/main/output/USAStates.png?raw=true"></a>

<a href=""><img width="480" height="550" align='right' src="https://github.com/DiegoHurtad0/USA-Traveling-Salesman-Tour/blob/main/output/USATravelingSalesmanProblem.png?raw=true"></a>

<br>
<br>
<h4 align="center">Efficient route planning for travelling salesman problem for 48 USA States</h4>

<h3 align="left">Languages:</h3>
<a href="" target="blank"><img align="left" src="https://www.vectorlogo.zone/logos/python/python-icon.svg" alt="diegohurtadoo" height="30" width="40" /></a>
<br>
<h3 align="left">Data Science Tools:</h3>

<img src="https://www.vectorlogo.zone/logos/usepanda/usepanda-icon.svg" alt="plotly" width="40" height="40"/> </a> <a href="" target="_blank" rel="noreferrer">
<img src="https://www.vectorlogo.zone/logos/google_maps/google_maps-tile.svg" alt="seaborn" width="40" height="40"/> </a> <a href="" target="_blank" rel="noreferrer"> 
<img src="https://geopandas.org/en/stable/_images/geopandas_icon_green.png" alt="plotly" width="40" height="40"/> </a> <a href="" target="_blank" rel="noreferrer">


<h3 align="left">Data Visualization Tools: </h3>

<img src="https://www.vectorlogo.zone/logos/plot_ly/plot_ly-official.svg" alt="plotly" width="40" height="40"/> </a> <a href="" target="_blank" rel="noreferrer">
<img src="https://www.vectorlogo.zone/logos/w3_html5/w3_html5-icon.svg" alt="plotly" width="40" height="40"/> </a> <a href="" target="_blank" rel="noreferrer">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="" target="_blank" rel="noreferrer"> 


<h3 align="left">References: </h3>

[1] Laporte, G. (1992). The traveling salesman problem: An overview of exact and approximate algorithms. European Journal of Operational Research, 59(2), 231-247.

[2] Hurtado-Olivares, D., Hernández-Aguilar, J.A., Ochoa-Zezzatti, A., Zavala-Díaz, J.C., Santamaría-Bonfil, G. (2021). Waste Collection of Touristics Services Sector Residues Vehicle Routing Problem with Time Windows to an Industrial Polygon in a Smart City. In: Ochoa-Zezzatti, A., Oliva, D., Juan Perez, A. (eds) Technological and Industrial Applications Associated with Intelligent Logistics. Lecture Notes in Intelligent Transportation and Infrastructure. Springer, Cham. https://doi.org/10.1007/978-3-030-68655-0_6

[3] G. (Ed.). (n.d.). Traveling Salesperson Problem. Retrieved December 01, 2022, from https://developers.google.com/optimization/routing/tsp

[4] Google, G. (Ed.). (n.d.). Routing Options. Retrieved December 02, 2022, from https://developers.google.com/optimization/routing/routing_options#local_search_options
