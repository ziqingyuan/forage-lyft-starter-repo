import unittest

from tires.carrigan_tires import CarriganTires


class TestCarriganTires(unittest.TestCase):
    def test_should_be_serviced(self):
        wear_sensors_array = [0.9, 0, 0, 0]

        carrigan_tires = CarriganTires(wear_sensors_array)
        self.assertTrue(carrigan_tires.needs_service())

    def test_should_not_be_serviced(self):
        wear_sensors_array = [0.89, 0, 0, 0]

        carrigan_tires = CarriganTires(wear_sensors_array)
        self.assertFalse(carrigan_tires.needs_service())


if __name__ == '__main__':
    unittest.main()