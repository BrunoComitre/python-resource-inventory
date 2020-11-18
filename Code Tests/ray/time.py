import time

def stress_function(num):
    return sum([i*j*k for i in range(num) for j in range(i) for k in range(j)])

if __name__ == "__main__":
    inp = int(input("enter a number: "))
    start = time.time()
    _ = [stress_function(inp) for _ in range(inp)]
    print(time.time() - start)
