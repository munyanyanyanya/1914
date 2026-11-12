import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='calc-logs.log',
                    filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.info("Calc has started...")
while True:
    try:
        a = int(input("a: "))
        o = input("+, -, *, /: ")
        b = int(input("b: "))

        if o == '+':
            print(f"{a} + {b} = {a+b}")
            logging.info(f"{a} + {b} = {a+b}")
        elif o == '-':
            print(f"{a} - {b} = {a-b}")
            logging.info(f"{a} - {b} = {a-b}")
        elif o == '*':
            print(f"{a} x {b} = {a*b}")
            logging.info(f"{a} * {b} = {a*b}")
        elif o == '/':
            print(f"{a} / {b} = {a/b}")
            logging.info(f"{a} / {b} = {a/b}")
        else:
            print(f"'{o}' - Incorrect operation...")
            logging.warning(f"'{o}' - Incorrect operation...")

        if input("Continue? (y/n): ").lower() == 'n':
            break

    except ValueError:
        print("Incorrect input data...")
        logging.error("Incorrect input data...")
    except ZeroDivisionError as zde:
        print("Not allowed operation...")
        logging.error("Not allowed operation...")

logging.info("Calc has stopped...")
