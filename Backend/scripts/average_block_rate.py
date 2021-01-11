import time

from Backend.blockchain.Blockchain import Blockchain
from Backend.config import SECONDS

blockchain = Blockchain()

times = []

for i in range(1000):
    start_time = time.time_ns()
    blockchain.add_block(i)
    end_time = time.time_ns()

    time_to_mine = (end_time - start_time) / SECONDS
    times.append(time_to_mine)

    average_time = sum(times) / len(times)

    print(f'New block difficulty : {blockchain.chain[-1].difficulty}')
    print(f'Time to mine a block: {time_to_mine}s')
    print(f'Average time to add a block: {average_time}s\n')
