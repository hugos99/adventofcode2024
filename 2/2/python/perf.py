import timeit
import cProfile
import main

if __name__ == '__main__':
    execution_count = 100000
    print("Performance of 1/2/python/main.py in milliseconds:")
    print((timeit.timeit("main.run()", setup="import main", number=execution_count)/execution_count)*1000)

    cProfile.run("main.run()", filename=main.path.as_posix()+"/perf.prof")
