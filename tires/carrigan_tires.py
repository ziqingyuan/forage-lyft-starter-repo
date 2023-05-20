from tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self, wear_sensors_array: []):
        self.wear_sensors_array = wear_sensors_array

    def needs_service(self):
        for sensor_value in self.wear_sensors_array:
            if sensor_value >= 0.9:
                return True
        return False
