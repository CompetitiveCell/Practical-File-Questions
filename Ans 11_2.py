import random
import time

def roll_dice():
    a = random.randint(1,6)
    print("Rolling the dice.....")
    time.sleep(3)
    print("Value is\n",a)

roll_dice()
