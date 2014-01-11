import threading
from time import sleep

i = 0
def myFunc():
  global i

  while True:
    i += 1
    sleep(0.01)
    i += 1

for j in range(0, 100):
  thread = threading.Thread(target=myFunc)
  thread.start()

while True:
  sleep(.1)
  if (i % 2 == 1):
    print i
