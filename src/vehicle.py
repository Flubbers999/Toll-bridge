from abc import abstractmethod

class Vehicle:
    def __init__(self, reg: str, weight: float):
        self.RegistrationNumber = reg
        self.Weight = weight
    
    @abstractmethod
    def CalculateFee(self):
        pass