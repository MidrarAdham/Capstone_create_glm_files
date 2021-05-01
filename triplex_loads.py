from functions import *

'''

i = 0
print("Associated Node:")

node = input()
print("enter phases:")

phases = input()
print("enter a csv file name:")

file_name = input()

house_player = "_player"

print("how many instances?")

counter = input()

while i < int(counter):

	trip_player = trip_load_with_player("House_"+node+"_"+str(i)+"_"+phases,phases,house_player+str(i),file_name+str(i))
	print(trip_player)
	i = i + 1
'''

OL = overhead_lines_objects("OL","C","646","xfrmr")
print(OL)

SP_xfmr = center_tapped_xfmr_object{"xfmr_CT","CS","node 646","trip_node_645","CS25_config"}
print(SP_xfmr)

