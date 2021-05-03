from functions import*

for i in range(1,41):
    H_load = trip_load_with_player("trip_load_652_A_h_"+str(i),"AS","House_652_A_"+str(i),"HOUSE"+str(i))
    L_load = trip_load_with_player("trip_load_652_A_L_"+str(i),"AS","Load_652_A_"+str(i),"DRYER"+str(i))

    i=i+1
    print(H_load)
    print(L_load)
