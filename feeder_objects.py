from functions import *

def trips(counter,From):
    node_OL = overhead_lines_objects("OL_652_A_xfmr_652_A_"+str(counter),"AN","meter_652_A","xfmr_meter_652_A_"+str(counter))
    print(node_OL)
    HS_meter = meter_object("xfmr_meter_652_A_"+str(counter),"AN")
    print(HS_meter)
    xfmr = center_tapped_xfmr_object("xfmr_652_A_"+str(counter),"AS","xfmr_meter_652_A_"+str(counter),"trip_node_652_A_"+str(counter),"AS100_config")
    print(xfmr)
    trip_line = triplex_line("xfmr_trip_line_652_A_"+str(counter),"xfmr_meter_652_A_"+str(counter),"trip_node_652_A_"+str(counter),"AS")
#    print(trip_line)
    trip_nodes = trip_node("trip_node_652_A_"+str(counter),"AS")
    print(trip_nodes)
    for k in range(1,9):
        trip_line_counter = 8*(counter - 1) + k
        meter = trip_meter_object("house_meter_"+str(trip_line_counter),"AS")
        trip_lines = triplex_line("trip_line_652_A"+"_"+str(trip_line_counter),From,"house_meter_"+str(trip_line_counter),"AS")
        trip_lines_H = triplex_line("trip_line_652_A_h_"+str(trip_line_counter),"house_meter_"+str(trip_line_counter),"trip_load_652_A_h"+"_"+str(trip_line_counter),"AS")
        trip_lines_L = triplex_line("trip_line_652_A_L_"+str(trip_line_counter),"house_meter_"+str(trip_line_counter),"trip_load_652_A_L"+"_"+str(trip_line_counter),"AS")
        #trip_load_player = trip_load_with_player("trip_load_652_A_h_"+str(trip_line_counter),"AS","_652_A_"+str())


        print(trip_lines)
        print(meter)
        print(trip_lines_H)
        print(trip_lines_L)

for i in range(1,6):
    trips(i,"trip_node_652_A_"+str(i))

#########################################################################################################
#########################################################################################################
#########################################################################################################

## STARTING NODE 611

#########################################################################################################
#########################################################################################################
#########################################################################################################


def trips_611(counter,From):
    node_OL = overhead_lines_objects("OL_611_C_xfmr_611_C_"+str(counter),"AN","meter_611_C","xfmr_meter_611_C_"+str(counter))
    print(node_OL)
    HS_meter = meter_object("xfmr_meter_611_C_"+str(counter),"CN")
    print(HS_meter)
    xfmr = center_tapped_xfmr_object("xfmr_611_C_"+str(counter),"CS","xfmr_meter_611_C_"+str(counter),"trip_node_611_C_"+str(counter),"CS100_config")
    print(xfmr)
    trip_line = triplex_line("xfmr_trip_line_611_C_"+str(counter),"xfmr_meter_611_C_"+str(counter),"trip_node_611_C_"+str(counter),"CS")
#    print(trip_line)
    trip_nodes = trip_node("trip_node_611_C_"+str(counter),"CS")
    print(trip_nodes)
    for k in range(1,9):
        trip_line_counter = 8*(counter - 1) + k
        meter = trip_meter_object("house_meter_"+str(trip_line_counter),"CS")
        trip_lines = triplex_line("trip_line_611_C_"+str(trip_line_counter),From,"house_meter_"+str(trip_line_counter),"CS")
        trip_lines_H = triplex_line("trip_line_611_C_h_"+str(trip_line_counter),"house_meter_"+str(trip_line_counter),"trip_load_611_C_h"+"_"+str(trip_line_counter),"CS")
        trip_lines_L = triplex_line("trip_line_611_C_L_"+str(trip_line_counter),"house_meter_"+str(trip_line_counter),"trip_load_611_C_L"+"_"+str(trip_line_counter),"CS")
        #trip_load_player = trip_load_with_player("trip_load_652_A_h_"+str(trip_line_counter),"AS","_652_A_"+str())


        print(trip_lines)
        print(meter)
        print(trip_lines_H)
        print(trip_lines_L)

for i in range(1,6):
    trips_611(i,"trip_node_611_C_"+str(i))

'''
for result in results:
    (c,f) = result
    starting_line = trips(c,f,starting_line)

for k in range(40):
    while i < counter:
        trip_lines = triplex_line("trip_line_652A"+"_"+str(i),From,"trip_meter_652_A"+"_"+str(i),"AS")
        meter = meter_object("trip_meter_652_A"+"_"+str(i),"AS")

        print(trip_lines)
        print(meter)
        i = i + 1
        k = k + 1
    print('#######################################')
    print(k)
    print('#######################################')
    counter = 17
    From = "trip_node_652A_2"
    while i < counter:
        trip_lines = triplex_line("trip_line_652A"+"_"+str(i),From,"trip_meter_652_A"+"_"+str(i),"AS")
        meter = meter_object("trip_meter_652_A"+"_"+str(i),"AS")
        print(trip_lines)
        print(meter)
        i = i + 1
        k = k + 1
    counter = 25
    From = "trip_node_652A_3"
    while i < counter:
        trip_lines = triplex_line("trip_line_652A"+"_"+str(i),From,"trip_meter_652_A"+"_"+str(i),"AS")
        meter = meter_object("trip_meter_652_A"+"_"+str(i),"AS")
        print(trip_lines)
        print(meter)
        i = i + 1
        k = k + 1
    counter = 33
    From = "trip_node_652_4"
    while i < counter:
        trip_lines = triplex_line("trip_line_652A"+"_"+str(i),From,"trip_meter_652_A"+"_"+str(i),"AS")
        meter = meter_object("trip_meter_652_A"+"_"+str(i),"AS")
        print(trip_lines)
        print(meter)
        i = i + 1
        k = k + 1
    counter = 41
    From = "trip_node_652_5"
    while i < counter:
        trip_lines = triplex_line("trip_line_652A"+"_"+str(i),From,"trip_meter_652_A"+"_"+str(i),"AS")
        meter = meter_object("trip_meter_652_A"+"_"+str(i),"AS")
        print(trip_lines)
        print(meter)
        i = i + 1
        k = k + 1
'''
