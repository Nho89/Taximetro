import unittest
from app import createTaximeter, initRide, finishRide, pauseRide, calculateFee

class testTaxi(unittest.TestCase):

    def setUp(self):                
        self.state = createTaximeter()


    def test_createTaximeter(self):
        state = self.state
        self.assertIsNone(state['startTime'])
        self.assertIsNone(state['lastTime'])
        self.assertEqual(state['currentStatus'], 'move')
        self.assertEqual(state['moveDuration'], 0)
        self.assertEqual(state['stopDuration'], 0)


    def test_initRide(self):
        state = self.state.copy()
        initRide(state)
        self.assertIsNotNone(state['startTime'])  
        self.assertIsNotNone(state['lastTime'])
        self.assertEqual(state['currentStatus'], 'move')    

    def test_finishRide(self):
        state = self.state.copy()
        initRide(state)
        finishRide(state)
        self.assertIsNotNone(state['lastTime'])   
        self.assertEqual(state['currentStatus'], 'move') 

    def test_pauseRide(self):
        state = self.state.copy()
        initRide(state)
        pauseRide(state)
        self.assertIsNotNone(state['lastTime'])
        self.assertEqual(state['currentStatus'], 'pause')

    def test_calculateFee(self):
        state = self.state.copy()
        initRide(state)
        finishRide(state)
        fee = calculateFee(state['moveDuration'], state['stopDuration'])
        self.assertIsInstance(fee, float)
        self.assertGreater(fee, 0, "mensaje")



if __name__ == '__main__':
    unittest.main()