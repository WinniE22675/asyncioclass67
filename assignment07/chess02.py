import time
import asyncio

my_compute_time = 0.1
opponent_compute_time = 0.5
opponents = 24
move_pairs = 30

async def main(x):
    # Loops 30 times to simulate both players making a move
    board_start_time = time.perf_counter()
    for i in range (move_pairs):
        # We think for 5 seconds
        time.sleep(my_compute_time)
        print(f'Board {x+1} {i+1} Judit made a move')
        # Opponents think for 55 seconds
        await asyncio.sleep(opponent_compute_time)
        print(f'Board {x+1} {i+1} Opponent made a move')
    time_use = round(time.perf_counter() - board_start_time)
    print(f'Board-{x+1} - >>>>>>>>>>>>>>>>> Finished move in {time_use} secs.\n')
    return round(time.perf_counter() - board_start_time)

async def async_io():
    # Again same structure as in async-io.py
    tasks = [main(i) for i in  range (opponents)]
    await asyncio.gather(*tasks)
    print(f'Board exhibition finished in {round(time.perf_counter() - start_time)} secs.')

if __name__ == '__main__':
    start_time = time.perf_counter()
    asyncio.run(async_io())
    print(f'Finished in {round(time.perf_counter() - start_time)} secs.')