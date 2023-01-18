import sys
import re
import time
import collections

print(sys.path)

text = 'My phone number is 393939993. my country code is 57 and my lucky number is 16'
res = re.findall('[0-9]+', text)
print(res)

print(time.asctime(time.localtime()))

numbers = [1,1,2,2,2,2,3,1,1,23,3,4,2]
counter = collections.Counter(numbers)
print(counter)