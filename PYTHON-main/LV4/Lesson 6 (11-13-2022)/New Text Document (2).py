import time as t
numbers = [12, 75, 150, 180, 145, 525, 50]

# iterate each item of a list

for item in numbers:

  if item > 500:

    break

  elif item > 150:

    continue

  elif item % 5 == 0:

    print(item)
t.sleep(1) 
