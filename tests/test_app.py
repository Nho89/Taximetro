import unittest
from app import createTaximeter, initRide

class testTaxi(unittest.TestCase):

    def setUp(self):
        self.state = createTaximeter()

    def test_initRide(self):
        state = self.state.copy()
        initRide(state)
        self.assertIsNotNone(state['startTime'])
        self.assertEqual(state['currentStatus'], 'move')

if __name__ == '__main__':
    unittest.main()