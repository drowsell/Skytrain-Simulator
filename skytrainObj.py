# Object for Skytrain Stations
class Station:
    def __init__(self, name):
        # Initializing Variables
        self.__name = name
        self.__nextStation = None;
        self.__prevStation = None;
    
    def getStationName(self):
        return self.__name

    def setStationName(self, name):
        self.__name = name
    
    # Look into linked lists for python.
    def setNextStation(self): 
        self.__nextStation = None

    def getNextStation(self):
        self.__prevStation = None

# Object for Skytrain Train Cars
class Train:
    def __init__(self, name, type):
        # Initializing Variables
        self.__name = name
        self.__type = type
    
    def setTrainType(self, type):
        self.__type = type;

    def getTrainType(self, type):
        return self.__type
