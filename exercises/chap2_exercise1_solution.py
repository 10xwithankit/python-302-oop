class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"{self.make} {self.model} engine started!")

    def stop_engine(self):
        print(f"{self.make} {self.model} engine stopped!")


bugati_chiron = Vehicle("Bugatti", "Chiron", 2022)
bugati_chiron.start_engine()
bugati_chiron.stop_engine()

ferrari_roma = Vehicle("Ferrari", "Roma", 2022)
ferrari_roma.start_engine()
ferrari_roma.stop_engine()
