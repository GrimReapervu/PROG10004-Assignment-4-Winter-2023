class WirelessNetworks:
    def __init__(self, name):

        self.name = name
        self.oxyLevel = 0
        self.temperature = 0
        self.link = []
        self.numNeighbours = 0

        self.ADHOC_Mode = "ON"
        self.BRAND_NAME = "Cisco brand"

    def greetMessage(self):

        print("Welcome to the company's IoT-Based Health System")
