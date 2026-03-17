from abc import abstractmethod

class Vehicle:
    def __init__(self, reg: str, weight: float):
        self.RegistrationNumber = reg
        self.Weight = weight
    
    @abstractmethod
    def CalculateFee(self):
        pass
    
class Motorbike (Vehicle):
    def __init__(self, reg, weight):
        super().__init__(reg, weight)

    def CalculateFee(self):
        return 3

class Car (Vehicle):
    def __init__(self, reg, weight):
        super().__init__(reg, weight)

    def CalculateFee(self):
        fee: float = 5
        if self.Weight > 1590:
            extra = self.Weight - 1590
            extra = extra // 100
        return fee + extra
    
class Lorry (Vehicle):
    def __init__(self, reg, weight):
        super().__init__(reg, weight)

    def CalculateFee(self):
        if self.Weight <= 8000:
            return 10
        return 15