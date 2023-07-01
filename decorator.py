import time

def timeit(func):
 def timed(*args,**kwargs):
  print("Befor timeit decorator") 
  ts=time.time()
  result=func(*args,**kwargs)
  te=time.time()
  minutes,seconds=divmod((te-ts),60)
  print(minutes,seconds)
 
  print("Time taken%8.2f"%((te-ts)*10**6))
  print("After timeit decorator")
 
  return result
 return timed


@timeit
def fib():
 a,b=0,1

 while True:
  yield a
  a,b=b,a+b

num=int(input("Enter the size of fibonacci series"))

fibonacci=fib()

for x in range(num):
 print(next(fibonacci))
