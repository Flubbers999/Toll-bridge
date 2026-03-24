from vehicle import Vehicle


class Bridge:
    def __init__(self, amount_vehicles, total_weight):
        self.amount_vehicle = amount_vehicles
        self.total_weight = total_weight
        self.vehicles: list[Vehicle] = []

    def calc_total_weight(self) -> float:
        ret = 0
        for i in self.vehicles:
            ret += i.Weight
        return ret

    def add_vehicle(self, v: Vehicle) -> bool:
        """Adds a vehicle to the bride. Returns true if added and false if failed to add vehicle"""
        if len(self.vehicles) > 19:
            return False

        for i in self.vehicles:
            if i.RegistrationNumber == v.RegistrationNumber:
                return False

        self.vehicles.append(v)
        return True

    def remove_vehicle(self, reg: str) -> bool:
        for i in self.vehicles:
            if i.RegistrationNumber == reg:
                self.vehicles.remove(i)
                return True
        return False
