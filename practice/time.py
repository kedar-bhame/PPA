import time 
start_time = time.perf_counter()

n = 0
while n < 1000000000:
    n+=1
end_time = time.perf_counter()

print(n)
print(f"Execution time: {end_time  - start_time: .3f} seconds")