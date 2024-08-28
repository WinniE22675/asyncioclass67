# example of using an asyncio queue without blocking
from random import random
import asyncio
import time
 
# coroutine to generate work
async def producer(queue):
    start_put = time.perf_counter()
    print('Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = i
        # block to simulate work
        sleeptime = random()
        print(f"> Producer {value} sleep {sleeptime}")
        await asyncio.sleep(sleeptime)
        # add to the queue
        print(f"> Producer put {value}")
        await queue.put(value)
    # send an all done signal
    await queue.put(None)
    AllPut = time.perf_counter() - start_put
    print('Producer: Done')
    print(f"## Producer: Finish in ", AllPut, "seconds.")
 
# coroutine to consume work
async def consumer(queue):
    start_get = time.perf_counter()
    print('Consumer: Running')
    # consume work
    while True:
        # get a unit of work without blocking
        try:
            item = queue.get_nowait()
        except asyncio.QueueEmpty:
            print('Consumer: got nothing, waiting a while...')
            await asyncio.sleep(0.5)
            continue
        # check for stop
        if item is None:
            break
        # report
        print(f'\t> Consumer got {item}')
    # all done
    AllGet = time.perf_counter() - start_get
    print('Consumer: Done')
    print(f"## Consumer: Finish in ", AllGet, "seconds.")
 
# entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue()
    # run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))

if __name__ == "__main__":
    start_cooking = time.perf_counter() 
    # start the asyncio program
    asyncio.run(main())
    AllDone = time.perf_counter() - start_cooking
    print(f"## Program: Finish in ", AllDone, "seconds.")