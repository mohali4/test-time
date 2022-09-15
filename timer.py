from sys import argv
from threading import Thread
from time import sleep
from .model import time
def beep():
    global _beeping
    _beeping = True


def main ():

    from sys import argv
    test_time = time.from_secounds(3) if len(argv) == 1 else time.from_minutes(float(argv[1]))
    start = time.now()

    test_start = time(0)

    def stop():
        stop_start_time = time.now()
        m = input('\nWhat happend: ')
        nonlocal test_start, start
        if m in ['q','exit','quit']:
            global _exit
            _exit()
        elif m in ['r','resume']:
            test_start += stop_start_time.delta_now
            start += stop_start_time.delta_now
        elif m in ['','t','n','next']:
            test_start = time.now()
            start += stop_start_time.delta_now
            


    while True :
        test_start = time.now()
        print_time = lambda: print(f"{start.delta_now.iso()} <- {time(test_time-(time(test_start).delta_now)).iso()}",end='\r')

        while test_start.delta_now < test_time :
            checkexit()
            try:
                sleep(breakt.float)
            except:
                stop()
        print(f'Finished: {time(((start.delta_now+time.from_secounds(0))//breakt)*breakt).iso()}  ')
        beep()


def checkexit():
    global down
    if down == True :
        exit() 

def _beep_thread():
       
    def beep(t=1):
        import beepy
        for _ in range(t): 
            beepy.beep(sound=3)
            checkexit()

    global _beeping

    while True :
        if _beeping == True :
            _beeping = False
            beep(t=3)
        sleep(breakt)
        checkexit()
        sleep(breakt)

def _exit():
    global down
    
    if not down:
        down = True
        print('good bye :)')
        checkexit()


try:
    if __name__ == "__main__":
        down = False
        breakt = time.from_milisecounds(1)
        _beeping=False    
        Thread(target=_beep_thread).start()
        main()
except:
    _exit()


# 09391267690


