import time 
import os 

lyrics = [
    "Hey are you still there?",
    "Good.",
    "Maybe I’m just not better than this I haven’t tried",
    "Cause maybe you’ll finally choose me after you’ve had more time",
    "I thought I was a fast learner",
    "But guess I won’t ever mind,"

]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_lyrics(lyrics):
    clear_screen()
    print("para saken:\n")
    for line in lyrics:
        for char in line: 
            print(char, end='', flush=True)
            time.sleep(0.09)
        print()  
        time.sleep(0.9)

if __name__ == "__main__":
    display_lyrics(lyrics)            
 