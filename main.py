import time

def c_timer(seconds):
    while seconds > 0:
        print(seconds, end='\r')
        time.sleep(1)
        seconds -= 1
print("Time is Starting !!!")

def main():
    try:
        seconds = int(input("Enter a valid number for seconds: "))
        c_timer(seconds)
    except:
        print("Enter a valid number for seconds please")

if __name__ == "__main__":
    main()






