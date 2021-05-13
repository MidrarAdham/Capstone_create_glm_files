from functions import*

nodes = [
         (652, "A", "AS"), 
         (611, "C", "CS"), 
         (684, "C", "CS"),
         (684, "A", "AS"),
         (645, "B", "BS"),
         (645, "C", "CS"),
         (633, "A", "AS")
        ]
fileNumber = 1

for (i, (node, label, phase)) in enumerate(nodes):
    for objectNumber in range(1, 41):
        H_load = trip_load_with_player(f"trip_load_{node}_{label}_h_{objectNumber}", phase, f"House_{node}_{label}_{objectNumber}", f"HOUSE{fileNumber}")
        print(H_load)
        L_load = trip_load_with_player(f"trip_load_{node}_{label}_L_{objectNumber}", phase, f"Load_{node}_{label}_{objectNumber}", f"DRYER{fileNumber}")
        print(L_load)
        
        fileNumber += 1

'''
for i in range(1,41):
    H_load = trip_load_with_player("trip_load_652_A_h_"+str(i),"AS","House_652_A_"+str(i),"HOUSE"+str(i))
    L_load = trip_load_with_player("trip_load_652_A_L_"+str(i),"AS","Load_652_A_"+str(i),"DRYER"+str(i))

    i=i+1
    print(H_load)
    print(L_load)

for i,k in zip(range(1,41),range(41,83)):
    H_load = trip_load_with_player("trip_load_611_C_h_"+str(i),"CS","House_611_C_"+str(i),"HOUSE"+str(k))
    L_load = trip_load_with_player("trip_load_611_C_L_"+str(i),"CS","Load_611_C_"+str(i),"DRYER"+str(k))

    i = i + 1
    k = k + 1
    print(H_load)
    print(L_load)
'''