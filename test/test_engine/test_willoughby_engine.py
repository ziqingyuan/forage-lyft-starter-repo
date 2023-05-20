
import unittest

from engine.willoughby_engine import WilloughbyEngine


class TestWilloughbyEngine(unittest.TestCase):
    def test_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willoughby_engine.needs_service())

    def test_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(willoughby_engine.needs_service())


if __name__ == '__main__':
    unittest.main()