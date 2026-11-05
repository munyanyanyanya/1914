import random

class Task(object):
    def __init__(self, title, days):
        self.title = title
        self.days = days
        self.done = False

    def info(self):
        status = "виконано" if self.done else "невиконано"
        print(f"завдання: {self.title}, залишилось днів: {self.days} стан: {status}")

    def do_task(self):
        self.done = True
        print(f"завдання '{self.title}' виконано")

    def wait(self):
        self.days -= 1
        print(f"пройшов день для завдання '{self.title}'.")

hw = Task("дз", 6)

for day in range(6):
    print(f"день {day + 1}")
    action = random.randint(1, 2)

    if action == 1:
        hw.do_task()
    else:
        hw.wait()

hw.info()



