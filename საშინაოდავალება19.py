import multiprocessing
import threading
import time


def make_tea(name, seconds):
    print(f"{name}: იწყება")
    time.sleep(seconds)
    print(f"{name}: მზადაა")


def cpu_task(n):
    while n > 0:
        n -= 1


def io_task(seconds):
    time.sleep(seconds)


def run_sequential(task, jobs):
    for job in jobs:
        task(job)


def run_threads(task, jobs):
    threads = []
    for job in jobs:
        t = threading.Thread(target=task, args=(job,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()


def run_processes(task, jobs):
    processes = []
    for job in jobs:
        p = multiprocessing.Process(target=task, args=(job,))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()


def measure(runner, task, jobs):
    start = time.perf_counter()
    runner(task, jobs)
    return time.perf_counter() - start


if __name__ == "__main__":
    teas = [("მწვანე ჩაი", 1.0), ("შავი ჩაი", 1.5), ("ბალახის ჩაი", 2.0)]

    start = time.perf_counter()
    for name, seconds in teas:
        make_tea(name, seconds)
    sequential = time.perf_counter() - start
    print(f"თანმიმდევრულად: {sequential:.1f} წმ")

    start = time.perf_counter()
    threads = []
    for name, seconds in teas:
        t = threading.Thread(target=make_tea, args=(name, seconds))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    threaded = time.perf_counter() - start
    print(f"thread-ებით: {threaded:.1f} წმ")

    print(f"დაჩქარება: {sequential / threaded:.1f}x")


    cpu_jobs = [10_000_000] * 4
    io_jobs = [1.0] * 4

    print()
    print(f"{'':<10}│ {'თანმიმდევრულად':<16}│ {'thread-ები':<16}│ პროცესები")
    for label, task, jobs in (("CPU-bound", cpu_task, cpu_jobs), ("I/O-bound", io_task, io_jobs)):
        t_seq = measure(run_sequential, task, jobs)
        t_thr = measure(run_threads, task, jobs)
        t_proc = measure(run_processes, task, jobs)
        print(
            f"{label:<10}│ {t_seq:5.2f} წმ ({t_seq / t_seq:4.1f}x) "
            f"│ {t_thr:5.2f} წმ ({t_seq / t_thr:4.1f}x) "
            f"│ {t_proc:5.2f} წმ ({t_seq / t_proc:4.1f}x)"
        )
