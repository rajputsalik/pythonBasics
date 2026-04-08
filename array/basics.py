from array import *

arr1 = array('f',[2.5,4.8,-3.2,6.7])
print(arr1.buffer_info())
for i in arr1:
  
    print(i)
    if i < 0:
        continue
    print(i)

