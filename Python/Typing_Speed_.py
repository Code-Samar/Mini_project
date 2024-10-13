import tkinter
from timeit import default_timer as timer
import random


import time

def typing_speed_test():
    print("Welcome to the Typing Speed Test!")
    input("Press Enter to start the test...")
    
    start_time = time.time()
    text = "The quick brown fox jumps over the lazy dog"
    print("Type the following text:")
    print(text)
    
    user_input = input("Your text: ")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    words_per_minute = len(text.split()) / (elapsed_time / 60)
    
    print("\nTest Results:")
    print(f"Time taken: {elapsed_time:.2f} seconds")
    print(f"Words per minute: {words_per_minute:.2f}")

if __name__ == "__main__":
    typing_speed_test()
