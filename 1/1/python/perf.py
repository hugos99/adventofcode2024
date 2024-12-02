import timeit
import main
import cProfile

if __name__ == '__main__':
    execution_count = 100000
    print("Performance of 1/1/python/main.py in milliseconds:")
    print((timeit.timeit("main.run()", setup="import main", number=execution_count)/execution_count)*1000)

    cProfile.run("main.run()", filename=main.path.as_posix()+"/perf.prof")
