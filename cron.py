#!/usr/bin/python
import os

import random
import time
from main import main

dir_name = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir_name)

minutes_to_sleep = random.randint(5, 30)
seconds_to_sleep = minutes_to_sleep * 60

time.sleep(seconds_to_sleep)

main()

