# micropython_nonblocking_buzzer
 A nonblocking implementation of a buzzer class that allows you to play basic melodies or sound patterns without blocking the main loop while the sound is being played.

 ## Usage
 1. Initialize de `NonBlocking_Buzzer` object just with the buzzer pin.
 2. Start the buzzer with the list of frequencies to play, timing information (note duration, delay between notes and delay between repetitions) and the number of repetitions.
 3. Use the `check()` method in the main loop so that the NonBlocking_Buzzer can update its state.


 See the example for more details.


 ## Considerations
 If you have a complex program with different routines that need to collaborate without blocking one another, you should probably check [uasyncio](https://docs.micropython.org/en/latest/library/uasyncio.html). You can implement this kind of nonblocking buzzer with asyncio, but if the buzzer is the only nonblocking routine you need to call, this implementation may be simpler, in fact, in my testing I have seen that this implementation introduces less delay in the main loop than the asyncio version.

 The check() method takes very little time in the main loop, so it introduces very little time penalty, but if your main loop takes too much time, the timing of the notes will get distorted.

 All notes have the same duration and the same delay between them, so it isn't well suited for "complex" melodies, but this way makes it very easy to use for sound patterns that intend to communicate some kind of event or state to the user.

 This nonblocking_buzzer could be easily extender as a nonblocking_led or a nonblocking_whatever. I will probably implement the nonblocking_led, because it seems useful but any contribution is welcome.
