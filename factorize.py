from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count
import time
import logging

def without_remainder(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors
    

def factorize_synchro(*number):
    numbers = list(number)
    return [without_remainder(number) for number in numbers]


def factorize_asynchro(*number):
    with ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        return list(executor.map(without_remainder, list(number)))




if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(message)s")
    factorize_synchro(128, 255, 99999, 10651060)
    factorize_asynchro(128, 255, 99999, 10651060)
    
    start_time = time.time()
    result_synchro = factorize_synchro(128, 255, 99999, 10651060)
    end_time = time.time()
    print("Synchronous Execution Time:", end_time - start_time)

    start_time = time.time()
    result_asynchro = factorize_asynchro(128, 255, 99999, 10651060)
    end_time = time.time()
    print("Asynchronous Execution Time:", end_time - start_time)