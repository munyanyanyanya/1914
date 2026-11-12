import logging
import random

logging.basicConfig(level=logging.DEBUG,
                    filename='game-logs.log',
                    filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.info("game")
number = random.randint(1, 100)

while True:
    try:
        g = int(input("число від 1 до 100: "))

        if g == number:
            print("вгадано")
            logging.info(f"use r tried {number}")
            break
        elif g < number:
            print("більше")
            logging.info(f"number is > {g}")
        else:
            print("менше")
            logging.info(f"number is < {g}")

    except ValueError:
        print("Incorrect input data...")
        logging.error("Incorrect input data...")

logging.info("Game has stopped...")