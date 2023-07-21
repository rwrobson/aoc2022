import re

test_input_text = """
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
"""


class Node:
    def __init__(self, address: str, flow_rate: int, connecting_addresses: list[str]):
        self.address = address
        self.flow_rate = flow_rate
        self.connecting_addresses = connecting_addresses

        self.distances = None

    def calc_distances(self, nodes: dict[str]):
        # Dijkstra
        SOME_BIG_NUMBER = 999999
        unvisited_list = {node_address: SOME_BIG_NUMBER for node_address in nodes.keys()
                          if not node_address == self.address}
        visited_list = {self.address: 0}
        current_address = self.address

        while current_address:
            # Examine the nodes that can be reached directly from the current node, and that have not yet been visited:
            new_cost = visited_list[current_address] + 1
            for neighbor_address in nodes[current_address].connecting_addresses:
                if not neighbor_address in visited_list:
                    """The cost through the current node is the current node's cost + 1.  
                    If that is less than this node's cost, use that instead"""
                    neighbor_cost = unvisited_list[neighbor_address]
                    if neighbor_cost > new_cost:
                        unvisited_list[neighbor_address] = new_cost

            """Pick the node that has the lowest cost (so far) in the unvisited list."""
            current_address = None
            for node_address in unvisited_list.keys():
                if not current_address or unvisited_list[node_address] < unvisited_list[current_address]:
                    current_address = node_address
            if current_address:
                visited_list[current_address] = unvisited_list[current_address]
                del unvisited_list[current_address]

        self.distances = visited_list

    def __repr__(self):
        return "Node(%s, %d, %s)" % (self.path_to_root,
                                     self.flow_rate,
                                     self.connecting_addresses)


def parse_line(text: str) -> Node:
    parse_pattern = "^Valve ([A-Z][A-Z]) has flow rate=([0-9]+); " \
                    "tunnels? leads? to valves? ([A-Z][A-Z](?:, [A-Z][A-Z])*)$"
    matches = re.findall(parse_pattern, text)
    assert len(matches) == 1
    assert len(matches[0]) == 3
    new_node_address = matches[0][0]
    new_node_flow_rate = int(matches[0][1])
    new_node_connecting_addresses = []
    for connecting_address in matches[0][2].split(", "):
        new_node_connecting_addresses.append(connecting_address)
    return Node(new_node_address, new_node_flow_rate, new_node_connecting_addresses)


def parse_text(text: str) -> dict[str, Node]:
    parsed_nodes =  [parse_line(line) for line in text.split("\n") if line.strip() != ""]
    return { node.address : node for node in parsed_nodes }


def evaluate_paths(nodes: dict[str, Node], start_address: str, time_limit: int, actors: int) -> (int, str):
    closed_valves = [address for address in nodes if nodes[address].flow_rate > 0]
    for address in closed_valves:
        nodes[address].calc_distances(nodes)
    nodes[start_address].calc_distances(nodes)

    best_path = ""
    best_value = 0

    def build_paths(closed_valves_in_scenario: list[str], time_left: int, current_path: str, current_path_value: int):
        nonlocal best_path, best_value
        if False and len(closed_valves_in_scenario) == 0 or time_left < 0:
            # all the valves are open, or we are out of time, nothing left to do
            if not best_value or current_path_value > best_value:
                best_path = current_path
                best_value = current_path_value
                print("Found %d at %s" % (best_value, best_path))
            return
        this_node_address = current_path[-2:]
        found_something_better = False
        for next_valve_address in closed_valves_in_scenario:
            distance = nodes[this_node_address].distances[next_valve_address]
            new_time_left = time_left - distance - 1
            if new_time_left > 0:
                found_something_better = True
                new_closed_values = [address for address in closed_valves_in_scenario if address != next_valve_address]
                new_value = current_path_value + nodes[next_valve_address].flow_rate * new_time_left
                build_paths(new_closed_values, new_time_left, current_path+" "+next_valve_address, new_value)
        if not found_something_better:
            if not best_value or current_path_value > best_value:
                best_path = current_path
                best_value = current_path_value
                print("Found %d at %s" % (best_value, best_path))

    build_paths(closed_valves, time_limit, start_address, 0)
    return best_value, best_path


assert evaluate_paths(parse_text(test_input_text), "AA", 30, 1) == (1651, "AA DD BB JJ HH EE CC")

assert evaluate_paths(parse_text(test_input_text), "AA", 26, 2) == (1707, "AA JJ BB CC", "AA DD HH EE")


"""
All that is important are the closed valves that are left.  
What order will you open them in, and what is the fastest way to get there?
For n nodes with non-zero flow, there are n! orders in which you can open them.
In the test data, there are 6 non-zero nodes,so 6! = 720 ways to solve
In the real data, there are 13, so 13! = 6,227,020,800 ways :(

"""

real_data_input_text = """Valve OQ has flow rate=17; tunnels lead to valves NB, AK, KL
Valve HP has flow rate=0; tunnels lead to valves ZX, KQ
Valve GO has flow rate=0; tunnels lead to valves HR, GW
Valve PD has flow rate=9; tunnels lead to valves XN, EV, QE, MW
Valve NQ has flow rate=0; tunnels lead to valves HX, ZX
Valve DW has flow rate=0; tunnels lead to valves IR, WE
Valve TN has flow rate=24; tunnels lead to valves KL, EI
Valve JJ has flow rate=0; tunnels lead to valves EV, HR
Valve KH has flow rate=0; tunnels lead to valves ZQ, AA
Valve PH has flow rate=0; tunnels lead to valves FN, QE
Valve FD has flow rate=0; tunnels lead to valves SM, HX
Valve SM has flow rate=7; tunnels lead to valves WW, RZ, FD, HO, KQ
Valve PU has flow rate=0; tunnels lead to valves VL, IR
Valve OM has flow rate=0; tunnels lead to valves CM, AA
Valve KX has flow rate=20; tunnel leads to valve PC
Valve IR has flow rate=3; tunnels lead to valves PU, CM, WW, DW, AF
Valve XG has flow rate=0; tunnels lead to valves RX, OF
Valve QE has flow rate=0; tunnels lead to valves PH, PD
Valve GW has flow rate=0; tunnels lead to valves JQ, GO
Valve HO has flow rate=0; tunnels lead to valves SM, TY
Valve WU has flow rate=0; tunnels lead to valves SG, RZ
Valve MS has flow rate=0; tunnels lead to valves UE, OF
Valve JS has flow rate=0; tunnels lead to valves DO, ZX
Valve YQ has flow rate=0; tunnels lead to valves BC, SG
Valve EJ has flow rate=0; tunnels lead to valves AA, LR
Valve EI has flow rate=0; tunnels lead to valves BV, TN
Valve NC has flow rate=0; tunnels lead to valves TS, BC
Valve AF has flow rate=0; tunnels lead to valves IR, HX
Valve OX has flow rate=0; tunnels lead to valves HR, BV
Valve BF has flow rate=0; tunnels lead to valves JQ, SY
Valve CA has flow rate=0; tunnels lead to valves YD, HX
Valve KQ has flow rate=0; tunnels lead to valves HP, SM
Valve NB has flow rate=0; tunnels lead to valves OQ, OF
Valve SY has flow rate=0; tunnels lead to valves BF, BV
Valve AA has flow rate=0; tunnels lead to valves KH, EJ, OM, TY, DO
Valve BC has flow rate=11; tunnels lead to valves WE, RX, YQ, LR, NC
Valve HR has flow rate=14; tunnels lead to valves OX, GO, JJ
Valve WE has flow rate=0; tunnels lead to valves DW, BC
Valve MW has flow rate=0; tunnels lead to valves JQ, PD
Valve DO has flow rate=0; tunnels lead to valves JS, AA
Valve PC has flow rate=0; tunnels lead to valves AK, KX
Valve YD has flow rate=0; tunnels lead to valves CA, OF
Valve RX has flow rate=0; tunnels lead to valves XG, BC
Valve CM has flow rate=0; tunnels lead to valves IR, OM
Valve HX has flow rate=6; tunnels lead to valves ZQ, NQ, AF, FD, CA
Valve ZQ has flow rate=0; tunnels lead to valves KH, HX
Valve BV has flow rate=21; tunnels lead to valves SY, OX, EI
Valve AK has flow rate=0; tunnels lead to valves PC, OQ
Valve UE has flow rate=0; tunnels lead to valves MS, JQ
Valve LR has flow rate=0; tunnels lead to valves BC, EJ
Valve JQ has flow rate=8; tunnels lead to valves MW, UE, BF, GW
Valve VL has flow rate=0; tunnels lead to valves PU, ZX
Valve EV has flow rate=0; tunnels lead to valves JJ, PD
Valve TS has flow rate=0; tunnels lead to valves NC, ZX
Valve RZ has flow rate=0; tunnels lead to valves SM, WU
Valve OF has flow rate=13; tunnels lead to valves XG, YD, NB, MS, XN
Valve WW has flow rate=0; tunnels lead to valves SM, IR
Valve TY has flow rate=0; tunnels lead to valves HO, AA
Valve XN has flow rate=0; tunnels lead to valves OF, PD
Valve SG has flow rate=15; tunnels lead to valves WU, YQ
Valve FN has flow rate=25; tunnel leads to valve PH
Valve KL has flow rate=0; tunnels lead to valves TN, OQ
Valve ZX has flow rate=5; tunnels lead to valves JS, HP, VL, NQ, TS"""

real_data_nodes = parse_text(real_data_input_text)
part_1_solution = evaluate_paths(real_data_nodes, "AA", 30)
print("Part 1 - the most pressure than can be released is %d by following path %s" % part_1_solution)

part_2_solution = evaluate_paths(real_data_nodes, "AA", 26, 2)
print("Part 1 - the most pressure than can be released is %d by following path %s" % part_2_solution)

