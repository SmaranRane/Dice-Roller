import time

class RNG:
    def __init__(self):
        self.current_time = int(time.time_ns()//100)
        self.primes = [4024845983, 7941363301, 1218835801, 3551543503, 8626421821, 6179370737, 1055250641, 5185100231, 3883733891, 1389641663, 3296031499, 7320532481, 9164970083, 9017614747, 9639958087, 4776171923, 5409073973, 9787786207, 2055861887, 2733194053, 6423958103, 2650787669, 5816011181, 4129546319, 9859872263, 9534943021, 2579307287, 1583045297, 8974712059, 1648343153]
        self.m = 2147483648; # Modulus (2^31)
        self.a = 1103515245; # Multiplier
        self.c = 12345;      # Increment
    
    def seed(self):
        current_prime = self.primes[(time.time_ns() * 7) % (len(self.primes))]
        seed = time.time_ns() * current_prime
        return seed

    def rand_unit_interval(self):
        curr_seed = (self.a * self.seed() + self.c) % self.m
        return curr_seed / self.m

    def rand_int(self, max_value):
        return int(self.rand_unit_interval() * max_value)

    def rand_float(self, max_value):
        return self.rand_unit_interval() * max_value