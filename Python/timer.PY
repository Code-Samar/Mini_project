import time

class Timer:
    def __init__(self, duration):
        self.duration = duration
        self.remaining_time = duration

    def start(self):
        print(f"Timer started for {self.duration} seconds.")
        start_time = time.time()
        while self.remaining_time > 0:
            time.sleep(1)
            self.remaining_time = self.duration - int(time.time() - start_time)
            print(f"Remaining time: {self.remaining_time} seconds", end='\r')
        print("\nTimer finished!")

if __name__ == "__main__":
    duration = int(input("Enter the duration of the timer in seconds: "))
    timer = Timer(duration)
    timer.start()