from __future__ import absolute_import, unicode_literals
from celery import shared_task
from datetime import datetime
import time
#import speedtest
#import speedtest

@shared_task(name = "print_msg_main")
def print_message(message, *args, **kwargs):
  print(f"Celery is working!! Message is {message}")

@shared_task(name = "print_time")
def print_time():
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(f"Current Time is {current_time}")
  
@shared_task(name='get_calculation')
def calculate(val1, val2):
  total = val1 + val2
  return total


# @shared_task(name='check_network_speed')
# def check_speed_fortmat():  
#     s = speedtest.Speedtest()
#     number_of_times = 0
#     while number_of_times < 2:
#         time_now = datetime.datetime.now().strftime("%H:%M:%S")
#         downspeed = round((round(s.download()) / 1048576), 2)
#         upspeed = round((round(s.upload()) / 1048576), 2)
#         ping = round(round(s.ping()  / 1048476), 2)
#         print(f"time: {time_now}, downspeed: {downspeed} Mb/s, upspeed: {upspeed} Mb/s , ping:{ping}")
#         time.sleep(60)
#         number_of_times += 1