#!/usr/bin/env python

import sys

key1 = 'red'
value1 = 'booyah'
key2 = 'blue'
value2 = 'heyho'
key3 = 'orange'
value3 = 'ohhhh yeeeeeah'
keyValuePairs = [(key1, value1), (key2, value2), (key3, value3)]
testMap = {}
for pair in keyValuePairs :
  testMap[pair[0]] = pair[1]
#testMap[key1] = value1
#testMap[key2] = value2

print(testMap)
testMap[key1] = 3
print(testMap)

keys = list(testMap.keys())
keys.sort()
print(keys)

