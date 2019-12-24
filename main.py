import skytrainObj

Edmonds = skytrainObj.Station("Edmonds")
print(Edmonds.getStationName())

test1 = skytrainObj.Train_Line("First")
print(test1.getTrainLineName())

test1.setFirstStation(Edmonds)
print((test1.getFirstStation()).getStationName())

