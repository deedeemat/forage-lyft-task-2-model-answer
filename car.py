import unittests
import function tests
from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery):
        def test_add(self):
        self.engine = engine
        self.assertEqual(functions.add(engine, battery), true)
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
