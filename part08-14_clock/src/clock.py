# Write your solution here:

class Clock:

    def __init__ (self, hh = 0, mm = 0, ss = 0):
        self.hh = hh
        self.mm = mm
        self.ss = ss

    def __str__ (self):
        return f'{self.hh:02}:{self.mm:02}:{self.ss:02}'

    def tick(self):

        self.ss += 1

        if self.ss == 60:
            self.mm +=1 
            self.ss = 0

            if self.mm == 60:
                self.hh += 1
                self.mm = 0

            if self.hh == 24:
                self.hh = 0

    def set(self, hh =0 , mm = 0, ss = 0):
        self.hh = hh
        self.mm = mm
        self.ss = ss


# clock = Clock(23, 59, 55)
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)

# clock.set(12, 5)
# print(clock)    
