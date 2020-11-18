import time
import ray

@ray.remote
def stress_function(num):
    return sum([i*j*k for i in range(num) for j in range(i) for k in range(j)])

if __name__ == "__main__":
    ray.init(redis_address="localhost:1024")
    inp = int(raw_input("enter a number: "))
    start = time.time()
    # Remote function is invoked by .remote keyword
    _ = ray.get([stress_function.remote(inp) for _ in range(inp)])
    print(time.time() - start)
    
# pip install psutil
# pip install setproctitle
