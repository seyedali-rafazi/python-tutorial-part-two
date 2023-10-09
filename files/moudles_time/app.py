import time

def item_define_time():
  for i in range(10000):
    pass
    
start = time.time()
item_define_time()  
end = time.time()

duration = end - start
print(duration)