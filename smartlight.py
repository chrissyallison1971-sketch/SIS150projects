import unittest
class SmartLight:
    def __init__(self):
        self.is_on = False
        self.brightness = 0

    def turn_on(self):
        self.is_on = True
        print("The light is now ON.")

    def turn_off(self):
        self.is_on = False
        self.brightness = 0
        print("The light is now OFF.")

    def set_brightness(self, level):
        if self.is_on:
            self.brightness = level
            print(f"Brightness set to {level}.")
        else:
            print("Cannot set brightness while the light is off.")
        

# Create an object to test the class
light = SmartLight()
light.turn_on()
light.set_brightness(75)
light.turn_off()        

class TestSmartLight(unittest.TestCase):
    def test_turn_on(self):
        light = SmartLight()
        light.turn_on()
        self.assertTrue(light.is_on)

    def test_turn_off(self):
        light = SmartLight()
        light.turn_on()
        light.turn_off()
        self.assertFalse(light.is_on)
        self.assertEqual(light.brightness, 0)

    def test_set_brightness_while_on(self):
        light = SmartLight()
        light.turn_on()
        light.set_brightness(50)
        self.assertEqual(light.brightness, 50)

    def test_set_brightness_while_off(self):
        light = SmartLight()
        light.set_brightness(50)
        self.assertEqual(light.brightness, 0)

if __name__ == "__main__":
    unittest.main()