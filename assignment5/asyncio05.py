# Cook wait()
from random import random
import asyncio
from time import sleep, time

# coroutine to execute in a new task
# Rice
async def rice():
    # generate a random value between 0 and 1
    value = 1 + random()
    # block for a moment
    await asyncio.sleep(value)
    # report the value
    print(f'Microwave (Rice):        Cooking {value} seconds')
    await asyncio.sleep(1)
    return print('Microwave (Rice):        Finished cooking')

# Noodle
async def noodle():
    # generate a random value between 0 and 1
    value = 1 + random()
    # block for a moment
    await asyncio.sleep(value)
    # report the value
    print(f'Microwave (Noodle):      Cooking {value} seconds')
    await asyncio.sleep(1)
    return print('Microwave (Noodle):      Finished cooking')

# Curry
async def curry():
    # generate a random value between 0 and 1
    value = 1 + random()
    # block for a moment
    await asyncio.sleep(value)
    # report the value
    print(f'Microwave (Curry):       Cooking {value} seconds')
    await asyncio.sleep(1)
    return print('Microwave (Curry):       Finished cooking')

# main coroutine
async def main():
    # create many tasks
    # all_tasks = [task_rice(), task_noodle(), task_curry()]
    # tasks = [asyncio.create_task(task_noodle(i)) for i in range(10)]
    task_rice = asyncio.create_task(rice(), name = 'Rice')
    task_noodle = asyncio.create_task(noodle(), name = 'Noodle')
    task_curry = asyncio.create_task(curry(), name = 'Curry')
    tasks = [task_rice, task_noodle, task_curry]
    # wait for all tasks to complete
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    # get the first task to complete
    num = len(done)
    first = done.pop()
    # print(f'Microwave ({first.get_name()}):      Finished cooking')
    # report results
    print(f'Completed task: {num}')
    print(f' - {first.get_name()} is completed')
    print(f'Uncompleted task: {len(pending)}')

# start the asyncio program
asyncio.run(main())