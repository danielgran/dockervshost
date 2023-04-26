import hashlib
import multiprocessing
from datetime import datetime
from itertools import repeat
from multiprocessing import Pool, cpu_count


def do_hash(bytes, count):
    for _ in range(count):
        hash(bytes)

def benchmark_cpu(multiplier):
    file = open("dog.jpg", 'rb')
    bytecode = file.read()
    file.close()

    time_start = datetime.now()

    with Pool(cpu_count()) as p:
        p.starmap(do_hash, zip(bytecode, repeat(multiplier)))

    return datetime.now() - time_start

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    print ("Benchmarking CPU...")
    print ("CPU Cores: " + str(cpu_count()))
    took = benchmark_cpu(multiplier=10000)
    print ("Time taken: " + str(took))