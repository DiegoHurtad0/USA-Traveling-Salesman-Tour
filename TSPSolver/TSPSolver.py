from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp


'''
   _____
 /|_||_\`.__
(   _    _ _)
=`-(_)--(_)-' TSP Diego Hurtado
``````````````````````````````````````````````````````````

'''

class RandomMatrix(object):
    """Random matrix."""

    def __init__(self, size, seed):
        """Initialize random matrix."""

        rand = random.Random()
        rand.seed(seed)
        distance_max = 100
        self.matrix = {}
        for from_node in range(size):
            self.matrix[from_node] = {}
            for to_node in range(size):
                if from_node == to_node:
                    self.matrix[from_node][to_node] = 0
                else:
                    self.matrix[from_node][to_node] = rand.randrange(
                        distance_max)

    def Distance(self, manager, from_index, to_index):
        return self.matrix[manager.IndexToNode(from_index)][manager.IndexToNode(
            to_index)]

class Customer:
    def __init__(self, number, x, y, distance_matrix):
        self.number = number
        self.x = x
        self.y = y
        self.distance_matrix = distance_matrix
        """Stores the data for the problem"""
        self.data = {}
        self.data['distance_matrix'] = self.distance_matrix  # yapf: disable
        self.data['num_locations'] = len(data['locations'])
        self.data['depot'] = 0
        self.data['city_name'] = 1
        self.data['num_vehicles'] = 1

        self.data['time_windows'] = []
        self.data['demands'] = []
        self.data['time_per_demand_unit'] = 5  # 5 minutes/unit
        self.data['num_vehicles'] = 4
        self.data['vehicle_capacity'] = 15
        self.data['vehicle_speed'] = 83  # Travel speed: 5km/h converted in m/min

    def __repr__(self):
        return f"C_{self.number}"

    def distance(self, target):
        return math.sqrt(math.pow(self.x - target.x, 2) + math.pow(target.y - self.y, 2))

class RoutingProblem:
    def __init__(self, name, customers: list, vehicle_number, vehicle_capacity):
        self.name = name
        self.customers = customers
        self.vehicle_number = vehicle_number
        self.vehicle_capacity = vehicle_capacity

    def obj_func(self, routes):
        return sum(map(lambda x: x.total_distance, routes))

class Route:
    def __init__(self, problem: RoutingProblem, customers: list):
        self.RoutingProblem: RoutingProblem = RoutingProblem


class TSPSolver:
    def __init__(self, num_nodes, distance_matrix):
        self.num_nodes = num_nodes
        self.distance_matrix = distance_matrix

    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    def manhattan_distance(position_1, position_2):
        """Computes the Manhattan distance between two points"""
        return (
            abs(position_1[0] - position_2[0]) + abs(position_1[1] - position_2[1]))


    def print_solution(manager, routing, solution):
        list_route = []
        """Prints solution on console."""
        # print('Objective: {} miles'.format(solution.ObjectiveValue()))
        fo = solution.ObjectiveValue()
        # print(fo)
        index = routing.Start(0)
        # plan_output = 'Route for vehicle 0:\n'
        plan_output = ''
        route_distance = 0
        
        while not routing.IsEnd(index):
            plan_output += ' {} ->'.format(manager.IndexToNode(index))
            list_route.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
        # plan_output += ' {}\n'.format(manager.IndexToNode(index))
        plan_output += ' 0'
        # plan_output += 'Route distance: {}miles\n'.format(route_distance)

        return list_route, plan_output, fo

    def solve(self):
        # Create routing model
        routing = pywrapcp.RoutingModel(self.num_nodes, 1, 0)
        search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()

        # Define cost of each arc
        def distance_callback(from_index, to_index):
            from_node = routing.IndexToNode(from_index)
            to_node = routing.IndexToNode(to_index)
            return self.distance_matrix[from_node][to_node]

        transit_callback_index = routing.RegisterTransitCallback(distance_callback)
        routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

        # Set constraint: each node is visited exactly once
        routing.AddDimension(
            transit_callback_index,
            0,  # no slack
            self.num_nodes - 1,  # same start and end location
            True,  # start cumul to zero
            "cumul")
        routing.AddDimension(
            transit_callback_index,
            0,  # no slack
            self.num_nodes - 1,  # same start and end location
            True,  # start cumul to zero
            "count")
        count_dimension = routing.GetDimensionOrDie("count")
        routing.AddConstantDimension(1, self.num_nodes, True, "counter")
        routing.AddVariableMinimizedByFinalizer(count_dimension.CumulVar(self.num_nodes-1))
        for node in range(self.num_nodes):
            routing.AddDisjunction([node], 1)

        # Set first node as start node
        routing.SetDepot(0)

        # Solve the problem
        solution = routing.SolveWithParameters(search_parameters)

        # Return solution as list of node indices
        if solution:
            index = routing.Start(0)
            path = [routing.IndexToNode(index)]
            for i in range(1, routing.Size()):
                index = solution.Value(routing.NextVar(index))
                path.append(routing.IndexToNode(index))
            return path
        else:
            return None
        
    def get_solution_heuristic(algorithm):

        solution = None
        data = create_data_model()

        manager = ortools.constraint_solver.pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                                                         data['num_vehicles'], data['depot'])

        routing = ortools.constraint_solver.pywrapcp.RoutingModel(manager)

        transit_callback_index = routing.RegisterTransitCallback(distance_callback)

        routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

        search_parameters = ortools.constraint_solver.pywrapcp.DefaultRoutingSearchParameters()

        start_time = time.time()

        #   .
        #  ..^____/
        # `-. ___ ) First solution strategy
        #   ||  ||

        if algorithm == 'PATH_CHEAPEST_ARC':
            # Starting from a route "start" node, connect it to the node which produces the cheapest route segment, then extend the route by
            # iterating on the last node added to the route.
            search_parameters.first_solution_strategy = (
                routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
            )

            algorithm_type = 'First solution strategy'

        elif algorithm == "PATH_MOST_CONSTRAINED_ARC":
            # Similar to PATH_CHEAPEST_ARC, but arcs are evaluated with a comparison-based selector which will favor the most constrained
            # arc first. To assign a selector to the routing model, use the method ArcIsMoreConstrainedThanArc().
            search_parameters.local_search_metaheuristic = (
                routing_enums_pb2.FirstSolutionStrategy.PATH_MOST_CONSTRAINED_ARC
            )
            algorithm_type = 'First solution strategy'

        elif algorithm == "EVALUATOR_STRATEGY":
            # Similar to PATH_CHEAPEST_ARC, except that arc costs are evaluated using the function passed to SetFirstSolutionEvaluator().
            search_parameters.local_search_metaheuristic = (
                routing_enums_pb2.FirstSolutionStrategy.EVALUATOR_STRATEGY
            )
            algorithm_type = 'First solution strategy'

        elif algorithm == "SAVINGS":
            # Savings algorithm (Clarke & Wright). Reference: Clarke, G. & Wright, J.W.: "Scheduling of Vehicles from a Central Depot to a
            # Number of Delivery Points", Operations Research, Vol. 12, 1964, pp. 568-581.
            search_parameters.local_search_metaheuristic = (
                routing_enums_pb2.FirstSolutionStrategy.SAVINGS
            )
            algorithm_type = 'First solution strategy'

        elif algorithm == "SWEEP":
            # 	Sweep algorithm (Wren & Holliday). Reference: Anthony Wren & Alan Holliday: Computer Scheduling of Vehicles from One or More Depots to a
            # 	Number of Delivery Points Operational Research Quarterly (1970-1977), Vol. 23, No. 3 (Sep., 1972), pp. 333-344.
            search_parameters.local_search_metaheuristic = (
                routing_enums_pb2.FirstSolutionStrategy.SWEEP
            )
            algorithm_type = 'First solution strategy'

        elif algorithm == "CHRISTOFIDES":
            # Christofides algorithm (actually a variant of the Christofides algorithm using a maximal matching instead of a maximum matching,
            # which does not guarantee the 3/2 factor of the approximation on a metric travelling salesperson). Works on generic vehicle routing models by
            # extending a route until no nodes can be inserted on it. Reference: Nicos Christofides, Worst-case analysis of a new heuristic for the
            # travelling salesman problem, Report 388, Graduate School of Industrial Administration, CMU, 1976.
            search_parameters.local_search_metaheuristic = (
                routing_enums_pb2.FirstSolutionStrategy.CHRISTOFIDES
            )
            algorithm_type = 'First solution strategy'

        elif algorithm == "ALL_UNPERFORMED":
            # Make all nodes inactive. Only finds a solution if nodes are optional (are element of a disjunction constraint with a finite penalty cost).
            search_parameters.local_search_metaheuristic = (
                routing_enums_pb2.FirstSolutionStrategy.ALL_UNPERFORMED
            )
            algorithm_type = 'First solution strategy'

        elif algorithm == "BEST_INSERTION":
            # Iteratively build a solution by inserting the cheapest node at its cheapest position; the cost of insertion is based on the global cost function of the routing model.
            # As of 2/2012, only works on models with optional nodes (with finite penalty costs).
            search_parameters.local_search_metaheuristic = (
                routing_enums_pb2.FirstSolutionStrategy.BEST_INSERTION
            )
            algorithm_type = 'First solution strategy'

        elif algorithm == "PARALLEL_CHEAPEST_INSERTION":
            # Iteratively build a solution by inserting the cheapest node at its cheapest position; the cost of insertion is based on the arc cost function.
            # Is faster than BEST_INSERTION.
            search_parameters.local_search_metaheuristic = (
                routing_enums_pb2.FirstSolutionStrategy.PARALLEL_CHEAPEST_INSERTION
            )
            algorithm_type = 'First solution strategy'

        elif algorithm == "LOCAL_CHEAPEST_INSERTION":
            # Iteratively build a solution by inserting each node at its cheapest position; the cost of insertion is based on the arc cost function.
            # Differs from PARALLEL_CHEAPEST_INSERTION by the node selected for insertion; here nodes are considered in their order of creation.
            # Is faster than PARALLEL_CHEAPEST_INSERTION.
            search_parameters.local_search_metaheuristic = (
                routing_enums_pb2.FirstSolutionStrategy.LOCAL_CHEAPEST_INSERTION
            )
            algorithm_type = 'First solution strategy'

        elif algorithm == "GLOBAL_CHEAPEST_ARC":
            # Iteratively connect two nodes which produce the cheapest route segment.
            search_parameters.local_search_metaheuristic = (
                routing_enums_pb2.FirstSolutionStrategy.GLOBAL_CHEAPEST_ARC
            )
            algorithm_type = 'First solution strategy'

        elif algorithm == "LOCAL_CHEAPEST_ARC":
            # Select the first node with an unbound successor and connect it to the node which produces the cheapest route segment.
            search_parameters.local_search_metaheuristic = (
                routing_enums_pb2.FirstSolutionStrategy.LOCAL_CHEAPEST_ARC
            )
            algorithm_type = 'First solution strategy'

        elif algorithm == "FIRST_UNBOUND_MIN_VALUE":
            # Select the first node with an unbound successor and connect it to the first available node.
            # This is equivalent to the CHOOSE_FIRST_UNBOUND strategy combined with ASSIGN_MIN_VALUE (cf. constraint_solver.h).
            search_parameters.local_search_metaheuristic = (
                routing_enums_pb2.FirstSolutionStrategy.FIRST_UNBOUND_MIN_VALUE
            )
            algorithm_type = 'First solution strategy'


        #   .
        #  ..^____/
        # `-. ___ ) Propagation control
        #   ||  ||

        # elif algorithm == "use_full_propagation":
        #     # Use constraints with full propagation in routing model (instead of light propagation only).
        #     search_parameters.local_search_metaheuristic = (
        #         routing_enums_pb2.use_full_propagation.use_full_propagation
        # )

        #   .
        #  ..^____/
        # `-. ___ ) Local search options
        #   ||  ||

        elif algorithm == "GREEDY_DESCENT":
            # Accepts improving (cost-reducing) local search neighbors until a local minimum is reached.
            search_parameters.local_search_metaheuristic = (
                routing_enums_pb2.LocalSearchMetaheuristic.GREEDY_DESCENT
            )
            algorithm_type = 'Local search options'

        elif algorithm == "GUIDED_LOCAL_SEARCH":
            # Uses guided local search to escape local minima (cf. http://en.wikipedia.org/wiki/Guided_Local_Search); this is generally the most efficient metaheuristic for vehicle routing.
            search_parameters.local_search_metaheuristic = (
                routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
            )
            algorithm_type = 'Local search options'

        elif algorithm == "SIMULATED_ANNEALING":
            # Uses simulated annealing to escape local minima (cf. http://en.wikipedia.org/wiki/Simulated_annealing).
            search_parameters.local_search_metaheuristic = (
                routing_enums_pb2.LocalSearchMetaheuristic.SIMULATED_ANNEALING
            )
            algorithm_type = 'Local search options'

        elif algorithm == "TABU_SEARCH":
            # Uses tabu search to escape local minima (cf. http://en.wikipedia.org/wiki/Tabu_search).
            search_parameters.local_search_metaheuristic = (
                routing_enums_pb2.LocalSearchMetaheuristic.TABU_SEARCH
            )
            algorithm_type = 'Local search options'

        elif algorithm == "TABU_SEARCH":
            # Uses tabu search on the objective value of solution to escape local minima.
            search_parameters.local_search_metaheuristic = (
                routing_enums_pb2.LocalSearchMetaheuristic.GENERIC_TABU_SEARCH
            )
            algorithm_type = 'Local search options'

        else:
            # Lets the solver select the metaheuristic.
            search_parameters.local_search_metaheuristic = (
                routing_enums_pb2.LocalSearchMetaheuristic.AUTOMATIC
            )
            algorithm_type = 'Local search options'

        # Limit to the number of solutions generated during the search.
        # search_parameters.solution_limit = 100
        # Limit in seconds to the time spent in the completion search for each local search neighbor
        # search_parameters.lns_time_limit.seconds = 100
        # Limit in seconds to the time spent in the search.
        search_parameters.time_limit.seconds = time_algo
        search_parameters.log_search = True

        solution = routing.SolveWithParameters(search_parameters)

        time_secs = round(time.time() - start_time, 2)

        if solution:
            list_route, plan_output, fo = print_solution(manager, routing, solution)
            print('      __')
            print(" (___()'`;  " + algorithm)
            print(' /,    /`')
            print(' \\"--\\')
            print('Route: ' + plan_output)
            print('Objective Function: ' + f"{fo:,}")
            print('Time: ' + f"{round(time_secs / 60, 2):,}" + ' Minutes')
            print('')
            print('')

            df_stats = get_stats(algorithm_type, algorithm, list_route, plan_output, fo, time_secs)
        else:
            list_route = [0]
            plan_output = 'ROUTING_NOT_SOLVED'
            fo = 9998888
            print('      __')
            print(" (___()X X`;  " + plan_output)
            print(' /,    /`   ' + algorithm)
            print(' \\"--\\')
            print('')
            print('')

            df_stats = get_stats(algorithm_type, algorithm, list_route, plan_output, fo, time_secs)

        return list_route, plan_output, fo, df_stats