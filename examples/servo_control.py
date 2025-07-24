from gpiozero import Servo, Device
from gpiozero.pins.lgpio import LGPIOFactory
from time import sleep

Device.pin_factory = LGPIOFactory()


def sweep(pin, positions=None):
    """Sweep servo connected to specified BCM pin through positions."""
    servo = Servo(pin)
    if positions is None:
        positions = [-1, -0.5, 0, 0.5, 1]
    try:
        while True:
            for pos in positions:
                servo.value = pos
                sleep(1)
    except KeyboardInterrupt:
        pass
