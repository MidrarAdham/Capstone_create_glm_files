from functions import *

def trips(counter, fromNode, node, label, hsPhase, lsPhase, lineConfig):
    node_OL = overhead_lines_objects(f"OL_{node}_{label}_xfmr_{node}_{label}_{counter}", hsPhase, f"meter_{node}_{label}",f"xfmr_meter_{node}_{label}_{counter}", lineConfig)
    print(node_OL)
    HS_meter = meter_object(f"xfmr_meter_{node}_{label}_{counter}", hsPhase)
    print(HS_meter)
    xfmr = center_tapped_xfmr_object(f"xfmr_{node}_{label}_{counter}", lsPhase, f"xfmr_meter_{node}_{label}_{counter}", f"trip_node_{node}_{label}_{counter}", f"{lsPhase}100_config")
    print(xfmr)
    trip_line = triplex_line(f"xfmr_trip_line_{node}_{label}_{counter}", f"xfmr_meter_{node}_{label}_{counter}", f"trip_node_{node}_{label}_{counter}", lsPhase)
#    print(trip_line)
    trip_nodes = trip_node(f"trip_node_{node}_{label}_{counter}", lsPhase)
    print(trip_nodes)
    for k in range(1,9):
        trip_line_counter = 8 * (counter - 1) + k
        meterName = f"house_meter_{node}_{label}_{trip_line_counter}"
        meter = trip_meter_object(meterName, lsPhase)
        trip_lines = triplex_line(f"trip_line_{node}_{label}_{trip_line_counter}", fromNode, meterName, lsPhase)
        trip_lines_H = triplex_line(f"trip_line_{node}_{label}_h_{trip_line_counter}", meterName, f"trip_load_{node}_{label}_h_{trip_line_counter}", lsPhase)
        trip_lines_L = triplex_line(f"trip_line_{node}_{label}_L_{trip_line_counter}", meterName, f"trip_load_{node}_{label}_L_{trip_line_counter}", lsPhase)
        print(trip_lines)
        print(meter)
        print(trip_lines_H)
        print(trip_lines_L)

nodes = [
         (652, 'A', 'AN', 'AS', 655), 
         (611, 'C', 'CN', 'CS', 605), 
         (684, 'C', 'CN', 'CS', 605),
         (684, 'A', 'AN', 'AS', 655),
         (645, 'B', 'BN', 'BS', 656),
         (645, 'C', 'CN', 'CS', 605),
         (633, 'A', 'AN', 'AS', 655)
        ]
for (i, (node, label, hsPhase, lsPhase, lineConfig)) in enumerate(nodes):
    counter = 1
    for j in range(1, 6):
        trips(counter, f"trip_node_{node}_{label}_{j}", node, label, hsPhase, lsPhase, lineConfig)
        counter += 1