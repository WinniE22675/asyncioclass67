import time

my_compute_time = 0.1
opponent_compute_time = 0.5
opponents = 3
move_pairs = 30

def game(x):
    # Loops 30 times to simulate both players making a move
    board_start_time = time.perf_counter()
    for i in range (move_pairs):
        # We think for 5 seconds
        time.sleep(my_compute_time)
        print(f'Board {x+1} {i+1} Judit made a move')
        # Opponents think for 55 seconds
        time.sleep(opponent_compute_time)
        print(f'Board {x+1} {i+1} Opponent made a move')
    print(f'Board-{x+1} - >>>>>>>>>>>>>>>>> Finished move in {round(time.perf_counter() - board_start_time)} secs.\n')
    return round(time.perf_counter() - board_start_time)

if __name__ == '__main__':
    start_time = time.perf_counter()
    # Loops 24 times because we are playing against 24 opponents
    board_time = 0
    for board in range(opponents):
        board_time += game(board)
    print(f'Board exhibition finished in {board_time} secs.')
    print(f'Finished in {round(time.perf_counter() - start_time)} secs.')