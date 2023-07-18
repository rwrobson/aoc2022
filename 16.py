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
        self.path_set = False
        self.parent_address = None
        self.distance_to_root = None
        self.path_to_root = None
        self.alternate_paths_to_root = []

    def set_parent(self, parent_node):
        if self.path_set:
            new_path = (parent_node.path_to_root + " " + self.address).strip()
            assert self.distance_to_root == parent_node.distance_to_root + 1
            self.alternate_paths_to_root.append(new_path)
        else:
            self.path_set = True
            self.parent_address = parent_node.address
            new_path = (parent_node.path_to_root + " " + self.address).strip()
            self.distance_to_root = parent_node.distance_to_root + 1
            self.path_to_root = new_path



    def set_root(self):
        assert not self.path_set
        self.path_set = True
        self.parent_address = ""
        self.distance_to_root = 0
        self.path_to_root = self.address

    def __repr__(self):
        if self.path_set:
            return "Node(%s, %d, %s)" % (self.path_to_root,
                                         self.flow_rate,
                                         self.connecting_addresses)
        else:
            return "Node(%s, %d, %s)" % (self.address,
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


def evaluate_paths(nodes: dict[str, Node], start_node: str, time_limit: int) -> dict:
    accumulated_paths = {}
    closed_valves = set([node_address for node_address in nodes.keys() if nodes[node_address].flow_rate > 0])

    def build_paths(nodes: dict[str, Node], closed_valves: set[str], time_left: int, current_path: str, current_path_value: int, accumulated_paths: dict[str, int]):
        if len(closed_valves) == 0 or time_left == 0:
            # all the valves are open, or we are out of time, nothing left to do
            accumulated_paths[current_path] = current_path_value
            print (current_path_value, current_path)
            return
        this_node_address = current_path[-2:]
        if this_node_address in closed_valves:
            # if this valve is closed, try opening it, and then recurse to self
            new_closed_valves = closed_valves.copy()
            new_closed_valves.remove(this_node_address)
            added_value = (time_left - 1) * nodes[this_node_address].flow_rate
            build_paths(nodes, new_closed_valves, time_left - 1, current_path + " %d " % added_value + this_node_address, current_path_value + added_value, accumulated_paths)
        # also try going down all other corridors - in this scenario, the valve state doesn't change
        for node_address in nodes[this_node_address].connecting_addresses:

            build_paths(nodes, closed_valves, time_left - 1, current_path + " " + node_address, current_path_value, accumulated_paths)

    build_paths(nodes, closed_valves, time_limit, start_node, 0, accumulated_paths)
    return accumulated_paths


def populate_distance_to_root(nodes: dict[str, Node], root_node_address: str):
    nodes[root_node_address].set_root()

    orphan_node_count = len(nodes)
    orphan_node_count_previous = orphan_node_count + 1

    parent_depth = 0
    while 0 < orphan_node_count < orphan_node_count_previous:
        orphan_node_count_previous = orphan_node_count
        for node_address in nodes:
            node = nodes[node_address]
            if not node.path_set:
                for possible_parent_address in sorted(node.connecting_addresses):
                    possible_parent = nodes[possible_parent_address]
                    if possible_parent.path_set and possible_parent.distance_to_root == parent_depth:
                        node.set_parent(nodes[possible_parent_address])
        orphan_node_count = 0
        for node_address in nodes:
            if not nodes[node_address].path_set:
                orphan_node_count += 1
        parent_depth += 1


def print_node_tree(nodes):
    for node_address in sorted(nodes):
        node = nodes[node_address]
        print("%s, %d, %s, %d, %s" % (node.address, node.distance_to_root, node.path_to_root,  node.flow_rate,
                                      ", ".join(sorted(node.connecting_addresses))))

# test_paths = evaluate_paths( parse_text(test_input_text), "AA", 30)


test_nodes = parse_text(test_input_text)
populate_distance_to_root(test_nodes, "AA")
#print_node_tree(test_nodes)



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
populate_distance_to_root(real_data_nodes, "AA")
print_node_tree(real_data_nodes)