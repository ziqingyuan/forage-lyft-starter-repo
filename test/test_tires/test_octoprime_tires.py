import unittest

from tires.octoprime_tires import OctoprimeTires


class TestCarriganTires(unittest.TestCase):
    def test_should_be_serviced(self):
        wear_sensors_array = [1, 1, 1, 0]

        octoprime_tires = OctoprimeTires(wear_sensors_array)
        self.assertTrue(octoprime_tires.needs_service())

    def test_should_not_be_serviced(self):
        wear_sensors_array = [0.99, 1, 1, 0]

        octoprime_tires = OctoprimeTires(wear_sensors_array)
        self.assertFalse(octoprime_tires.needs_service())


if __name__ == '__main__':
    unittest.main()