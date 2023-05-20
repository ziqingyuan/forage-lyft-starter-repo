from tires.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, wear_sensors_array: []):
        self.wear_sensors_array = wear_sensors_array

    def needs_service(self):
        sensor_value_sum = 0
        for sensor_value in self.wear_sensors_array:
            sensor_value_sum += sensor_value
        return sensor_value_sum >= 3
