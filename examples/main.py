import argparse
from servo_control import sweep


def main():
    parser = argparse.ArgumentParser(description="MG90S servo demo")
    parser.add_argument("--pin", type=int, default=18,
                        help="BCM GPIO pin connected to the servo")
    args = parser.parse_args()
    sweep(args.pin)


if __name__ == "__main__":
    main()
