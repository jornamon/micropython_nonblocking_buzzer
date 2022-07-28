"""
asyncio implmenentation of a non-blocking buzzer
This file is to test how this implementation affects de delay and timing of the main loop
"""

import uasyncio

async def buzz(buzzer, notes, delay_note=50, delay_inter=25, delay_rep=100, reps=1, MUTE=False):
    if not MUTE:
        for i in range(reps):
            for note in notes:
                buzzer.freq(note)
                buzzer.duty(512) # 0 to 1023
                await uasyncio.sleep_ms(delay_note)
                buzzer.duty(0)
                await uasyncio.sleep_ms(delay_inter)
            await uasyncio.sleep_ms(delay_rep)

async def main():
    buzzer = PWM(Pin(5), freq=2048, duty=0)
    MUTE = False

    buzz(buzzer, (262*4,262*4,523*4), reps=3)

    NUM_SAMPLES = 1000
    check_time_samples = array('f', [0] * NUM_SAMPLES)

    uasyncio.create_task(buzz(buzzer, (262*4,262*4,523*4), reps=500))
    for i in range(NUM_SAMPLES):
        loop_start = time.ticks_us()
        await uasyncio.sleep_ms(10)
        check_time_samples[i] = time.ticks_diff(time.ticks_us(), loop_start) / 1000
        #print(check_time_samples[i])
        
    stats = data_stats(check_time_samples)
    print("Stats: (num samples, min, max, range, std. dev, avg, overhead)")
    print(stats['num_samples'])
    print(stats['min'])
    print(stats['max'])
    print(stats['range'])
    print(stats['stdev'])
    print(stats['avg'])
    print(stats['ovh'])
    buzzer.duty(0)


import time
from machine import Pin, PWM
from array import array
from data_stats import data_stats

uasyncio.run(main())