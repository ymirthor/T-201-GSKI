import time

# start = timeit.timeit()
# print("hello" * 1000)
# end = timeit.timeit()
# print(end - start)




class Time():
    def __init__(self, start = 0,  end = 0):
        self.pauseStart = 0
        self.pauseEnd = 0
        self.time = 0
        self.start = start
        self.end = end
    
    def __str__(self):
        return "{:.10f}".format(self.time)

    def startTime(self):
        self.start = time.time()
        self.end = False
        return "{:.10f}".format(0)

    def currentTime(self):
        if not self.pauseEnd:
            current = time.time() - float(self.start)
            return "{:.10f}".format(current)
        else:
            pause = self.pauseEnd-self.pauseStart
            current = time.time() - float(self.start) - pause
            return "{:.10f}".format(current)

    def endTime(self):
        if not self.pauseEnd:
            self.end = time.time()
            current = time.time() - float(self.start)
            self.time = current
            return "{:.10f}".format(current)
        else:
            pause = self.pauseEnd-self.pauseStart
        self.end = time.time()
        current = float(self.end) - float(self.start) - pause
        self.time = current
        return "{:.10f}".format(current)

    def pause(self):
        self.pauseStart = time.time()
        self.pauseEnd = False
    
    def unpause(self):
        self.pauseEnd = time.time()

a = Time()
a.startTime()
print("lol")
time.sleep(1)
print(a.currentTime())
print("lol")
print("lol")
a.pause()
time.sleep(1)
a.unpause()
print("lol")
a.endTime()
print(a)