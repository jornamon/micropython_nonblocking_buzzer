"""
Nonblocking Buzzer implementation for Micropython
The method check() takes very little time in the main loop
1. Initialize de `NonBlocking_Buzzer` object just with the buzzer pin.
2. Start the buzzer with the list of frequencies to play, timing information (note duration, delay between notes and delay between repetitions) and the number of repetitions.
3. Use the `check()` method in the main loop so that the NonBlocking_Buzzer can update its state.
jornamon 2022
"""

import time
from machine import PWM, Pin


class NonBlocking_Buzzer():
    def __init__(self, pin):
        self._buzzer = PWM(pin, freq=2048, duty=0)
        self._state = 'STOPPED'
        self._duty_on = 512 # 0 to 1023
        
        
    def start(self, notes, delay_note=50, delay_inter=25, delay_rep=150, reps=1, mute=False):     
        
        if mute:
            return
        
        temp_notes = []
        for r in range(reps):
            for n in notes:
                temp_notes.extend([n,0])
            temp_notes.append(0)
        
        self._freq = tuple(temp_notes)
        del temp_notes
        self._duty = ((self._duty_on,0)*len(notes)+(0,))*reps
        self._delay = ((delay_note,delay_inter)*len(notes)+(delay_rep,))*reps
        self._steps = len(self._delay)
                
        self._state = 'WORKING'
        self._buzzer.freq(self._freq[0])
        self._buzzer.duty(self._duty[0])
        self._next_time = time.ticks_add(time.ticks_ms(),self._delay[0])
        self._next_step = 1

    def check(self):
        if self._state == 'STOPPED':
            return
        if time.ticks_ms() < self._next_time:
            return
        if self._duty[self._next_step] != 0:
            self._buzzer.freq(self._freq[self._next_step])
        self._buzzer.duty(self._duty[self._next_step])
        self._next_time = time.ticks_add(time.ticks_ms(),self._delay[self._next_step])
        self._next_step += 1
        if self._next_step == self._steps - 1:
            self._state = 'STOPPED'

    def stop(self):
        self._state = 'STOPPED'
        self._buzzer.duty(0)
            
