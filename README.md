# Miller-Rabin-Algorithm
Implementation of the Miller-Rabin algorithm that receives a suspicious number ```n``` and number of rounds of testing to perform ```k```, will most likely return ```true``` the number n is indeed prime and ```false``` if it is certainly not prime.

The algorithm is a Monte-Carlo algorithm whose the correctness of return value ```true``` is ```1 / (4 ^ k)```. The algorithm and its mainly use in the RSA encryption method were taught in the "Algebraic Structure" course.
