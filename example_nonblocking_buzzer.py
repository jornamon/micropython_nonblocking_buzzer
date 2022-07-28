"""
Nonblocking Buzzer for Micropython example
Plays some notes pattern while the main loop is running and calculates
some stats about the delay that the check() method introduces in the main loop,
which is the one that needs to be called from the main loop constantly
jornamon 2022
"""


import time, math
from machine import PWM, Pin
from array import array
from nonblocking_buzzer import NonBlocking_Buzzer
from data_stats import data_stats


nbb = NonBlocking_Buzzer(Pin(5))
nbb.start((262*4,262*4,523*4), delay_note=50, delay_inter=25, delay_rep=100,reps=500)
NUM_SAMPLES = 1000
check_time_samples = array('f', [0] * NUM_SAMPLES)

for i in range(NUM_SAMPLES):
    loop_start = time.ticks_us()
    nbb.check()
    time.sleep_ms(10)
    check_time_samples[i] = time.ticks_diff(time.ticks_us(), loop_start) / 1000
    #print(check_time_samples[i])

nbb.stop()


stats = data_stats(check_time_samples)
print("Stats: (num samples, min, max, range, std. dev, avg, overhead)")
print(stats['num_samples'])
print(stats['min'])
print(stats['max'])
print(stats['range'])
print(stats['stdev'])
print(stats['avg'])
print(stats['ovh'])

        
