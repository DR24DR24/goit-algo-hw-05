import task3_readfile
import task3_KMP
import task3_BM
import task3_RK
import timeit

text=task3_readfile.read_file("стаття 2.txt")

functions=[task3_KMP.kmp_search,task3_BM.boyer_moore_search,task3_RK.rabin_karp_search]

def time_measurements(text,pattern,repetition):
    print("pattern: ", pattern)
    print("text: ",text[0:min(80,len(text))])
    print("repetition: ",repetition)
    i=0
    time_p=[0]*len(functions)
    for f in functions:
        time_p[i]=timeit.timeit(\
        stmt=lambda: f(text,pattern),number=repetition)/repetition
        print(f.__name__, time_p[i], time_p[i]/time_p[0])
        i+=1
    print("\n")    

time_measurements(text,"системах. Наявність", 100)
time_measurements(text,"системах. Наявність", 1000)
time_measurements(text,"системах.  Наявність",100)
time_measurements(text,"системах.  Наявність",1000)

text=task3_readfile.read_file("стаття 2.txt")

time_measurements(text,"Література", 100)
time_measurements(text,"Література", 1000)
time_measurements(text,"Література",100)
time_measurements(text,"Література",1000)
