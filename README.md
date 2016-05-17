# subnet-monkey
Playground for learning ways to use Python to do simple networking stuff

Initial project for myself:

Write a subnet calculator in Python. Produce often-needed information such as usable IPs (number and range), dotted quad netmask, and network and broadcast addresses.

I'll start with IPv4, but once I get that done, I'll see how much of this can be repurposed for IPv6.

## THINGS THAT DON'T WORK

There are still many things that don't work in this yet, either at all
or in just the way I want them to. I will track them here.

> * Exception handling: I haven't gotten around to playing around with the best way to handle unexpected input.
>
> * ~Network/Broadcast address calculations are off: Yep. Certainly need to fix that!~ (This should be fixed now!)
>
> * Usable host range: While it's not at all difficult to figure out the usabe host range from the network and broadcast addresses, the whole point of having subnet calculator is to make all of this easier. And to generate something that could more easily be copied and pasted. Shouldn't at all difficult, just something I'd like to do.
>
> * Prettifying: I'd also like to make the output a little easier to read and/or copy from.
