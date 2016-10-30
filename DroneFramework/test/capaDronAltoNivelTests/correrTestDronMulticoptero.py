import unittest

import DroneFramework.test.capaDronAltoNivelTests.test_multicoptero as testMulticoptero


class CorrerTestDronMulticoptero ():
    def __init__(self):

        self.suite = unittest.TestLoader().loadTestsFromTestCase(testMulticoptero.MulticopetroTest)

    def correrTest (self):
        unittest.TextTestRunner(verbosity=2).run(self.suite)
