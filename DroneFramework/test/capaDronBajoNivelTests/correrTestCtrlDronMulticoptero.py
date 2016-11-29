import unittest

import DroneFramework.test.capaDronBajoNivelTests.ControladorMulticopteroTest as testCtrlMulticoptero


class CorrerTestCtrlDronMulticoptero ():
    def __init__(self):
        self.suite = unittest.TestLoader().loadTestsFromTestCase(testCtrlMulticoptero.ControladorMulticopetroTest)

    def correrTest (self):
        unittest.TextTestRunner(verbosity=2).run(self.suite)
