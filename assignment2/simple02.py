# Synchronous cooking
# 2 kitchen 2 chefs 2 dishes
import multiprocessing
from multiprocessing import Value
import os
from time import sleep, ctime, time
#Basket of sharing
class Basket:
    def __init__(self,eggs) -> None:
        self.eggs = Value('i',eggs)
    def use_eggs(self,index):
        print(f"{ctime()}Kitchen-{index} : Chef-{index} has lock with eggs remaining {self.eggs}")
        self.eggs -= 1
        print(f"{ctime()}Kitchen-{index} : Chef-{index} has released lock with eggs remaining {self.eggs}")
def cooking(index,basket):
    cooking_time = time()
    print(f'{ctime()} Kitchen-{index} : Begin Cooking...PID {os.getpid()}')
    sleep(2)
    duration = time() - cooking_time
    with basket.eggs.get_lock():
        basket.eggs.value = basket.eggs.value - 1
        print(f'{ctime()} Kitchen-{index} : Used Eggs.')
    print(f'{ctime()} Kitchen-{index} : Cooking Done in {duration:0.2f} seconds!.')
def kitchen(index,basket):
    cooking(index, basket)

if __name__ == "__main__":
    #Begin of main thread
    print(f'{ctime()}Main               : Begin Cooking.')
    start_time = time()

    basket = Basket(50)

    #printing main program process id 
    print(f"{ctime()}Main       : ID of Main process: {os.getpid()}")

    #Multi Processes
    kitchens = []    
    for index in range(2):
        p = multiprocessing.Process(target=kitchen,args=(index,basket,))
        kitchens.append(p)
        #starting Process
        p.start()
    for p in kitchens:
        #wait until process is finished
        p.join()
    print(f"{ctime()}Main        : Basket eggs remaining {basket.eggs}")
    duration = time() - start_time
    print(f"{ctime()}Main        : Finished Cooking duration in {duration:0.2f}seconds")