from WirelessNetworks import WirelessNetworks


class Application:
    listOfSensors = []

    def getIdName(self):
        # error checking

        print("_*__*__*__*__*__*__*__*__*__*_")
        print("Enter the Sensor Id:")
        global idN
        idN = input("")
        while True:

            if any(char.isdigit() for char in idN) == False:
                return idN
            print("This is an invalid entry for sensor Id! \n")
            print("_*__*__*__*__*__*__*__*__*__*_")
            print("Enter the Sensor Id: ")
            idN = input("")

    def createSensors(self):
        # creating the properties of the sensors
        while True:
            print("Enter the number of sensors: ")
            sensors = input("")
            if sensors.isnumeric() and sensors != "0" and sensors.startswith("-") == False:

                self.sensors = int(sensors)

                break
            print("Invalid Entry \n")
        sensorIndex = 1
        while sensorIndex <= self.sensors:
            name = Start.getIdName()
            sensor = WirelessNetworks(name)
            sensor.numNeighbours = Start.numNeighbours()
            Start.getNeighbours(sensor)
            sensor.oxyLevel = Start.getOxygenLevels()
            sensor.temperature = Start.getTemperatureAmount()
            self.listOfSensors.append(sensor)

            sensorIndex += 1

    def getSourceSensorName(self):
        # inputing the source sensor
        print("Enter the source sensor:")
        source = input("")
        while True:

            if any(char.isdigit() for char in source) == False:
                return source

            print("Enter the source sensor:")
            source = input("")

    def getDestinationSensorName(self):
        # inputing the destination sesnor
        print("Enter the destination sensor:")
        destination = input("")
        while True:

            if any(char.isdigit() for char in destination) == False:
                return destination

            print("Enter the destination sensor:")
            destination = input("")

    def getSourceSensorNameWithCheck(self):
        # error checking with source
        while True:
            sname = Start.getSourceSensorName()
            for sensor in self.listOfSensors:
                if (sensor.name == sname):
                    return sname

            print("The Source is not found\n")

    def getDestinationSensorNameWithCheck(self):
        # error checking with destination
        while True:
            dname = Start.getDestinationSensorName()
            for sensor in self.listOfSensors:
                if (sensor.name == dname):
                    return dname

            print("The Destination is not found\n")

    def numNeighbours(self):
        # finding the connected neighbour to the sensor
        while True:
            print("Enter the number of neighbours: ")
            numofneighbours = input("")
            if numofneighbours.isnumeric() and numofneighbours != "0" and numofneighbours.startswith("-") == False:
                return int(numofneighbours)
            print("This is an invalid entry for the number of neighbours! \n")

    def getNeighbours(self, sensor):

        sensorIndex = 1
        while sensorIndex <= sensor.numNeighbours:
            name = Start.getSensorNeighbourName()
            dist = Start.getDistance(sensor.name)
            sensor.link.append(name)
            sensor.link.append(dist)
            sensorIndex += 1

    def getSensorNeighbourName(self):
        # finding the neighbouring sensor

        print("Enter the neighbour of Sensor", idN, ":")
        sensorN = input("")
        while True:

            if any(char.isdigit() for char in sensorN) == False:
                return sensorN
            print("This is an invalid entry for the neighbour name and/or distance! \n")
            print("Enter the neighbour of Sensor", idN, ":")
            sensorN = input("")

    def getDistance(self, idName):
        # getting the distance
        while True:
            print("Enter the distance to", idN, ":")
            distancemeasure = input("")
            if distancemeasure.isnumeric() and distancemeasure != "0" and distancemeasure.startswith("-") == False:
                return float(distancemeasure)
            print("This is an invalid entry for the neighbour name and/or distance! \n")

    def getOxygenLevels(self):
        # finding the oxygen levels
        print("Enter the Oxygen level in %:")
        oxygenpercent = input("")
        while True:
            if oxygenpercent.isnumeric() and oxygenpercent != "0" and oxygenpercent.startswith("-") == False:

                return int(oxygenpercent)
            print("This is an invalid entry for the oxygen level! \n")
            print("Enter the Oxygen level in %:")
            oxygenpercent = input("")

    def getTemperatureAmount(self):
        # finding the temperature measurement
        print("Enter the temperature measurement: ")

        temperaturenum = input("")
        while True:
            if temperaturenum.isnumeric() and temperaturenum != "0" and temperaturenum.startswith("-") == False:

                return int(temperaturenum)
            print("This is an invalid entry for the temperature! \n")
            print("Enter the temperature measurement: ")
            temperaturenum = input("")

    def convrtToDictionary(self, listOfSensors):
        sensor_dict = {}

        # converting to dictionary list
        for key in listOfSensors:
            sensor_dict.setdefault(key.name, [])
            sensor_dict[key.name].extend(key.link)

        return sensor_dict

    def findPath(self, graph, source, destination, path=[]):
        # finding the best pathway from the source to the destination.
        path = path + [source]

        if source == destination:
            return path

        maxDistance = -99999

        newPath = []
        chosenNode = ""
        found = 0
        index = 0

        while (index < len(graph[source])):
            if ((graph[source][index] not in path) and type(graph[source][index]) != float):
                if (maxDistance < graph[source][index + 1]):
                    maxDistance = graph[source][index + 1]
                    chosenNode = graph[source][index]
                    found = 1
            index += 1
        print(maxDistance)
        if found == 1:
            newPath = self.findPath(graph, chosenNode, destination, path)

        if newPath:
            return newPath

        # finding the max readings of 2 sensors

    def findMaxReading(self):
        print("Finding the maximum Sp02 Reading among two sensors' readings:")
        print("Enter the index of one of the sensors:")
        indexInput1 = int(input(""))
        print("Enter the index of another sensors:")
        indexInput2 = int(input(""))
        print("One Sensor Readings:", self.listOfSensors[indexInput1].oxyLevel)
        print("Another Sensor Reading:",
              self.listOfSensors[indexInput2].oxyLevel)
        if self.listOfSensors[indexInput1].oxyLevel > self.listOfSensors[indexInput2].oxyLevel:
            print("The maximum SpO2 reading: Sensor id:",
                  self.listOfSensors[indexInput1].name, "SpO2:", self.listOfSensors[indexInput1].oxyLevel)

        else:
            print("The maximum SpO2 reading: Sensor id:",
                  self.listOfSensors[indexInput1].name, Start.listOfSensors[indexInput2].name, "SpO2:", self.listOfSensors[indexInput1].oxyLevel)


Start = Application()


print("******************************************************************************")
wn = WirelessNetworks("")
wn.greetMessage()
print("These are sensors of", wn.BRAND_NAME,
      "and their Ad Hoc Mode is ", wn.ADHOC_Mode)
print("******************************************************************************")
Start.createSensors()
source = Start.getSourceSensorNameWithCheck()
destination = Start.getDestinationSensorNameWithCheck()
graph = Start.convrtToDictionary(Start.listOfSensors)
path = Start.findPath(graph, source, destination)
print(path)
Start.findMaxReading()
dictionary = Start.convrtToDictionary(Start.listOfSensors)
print(dictionary)
