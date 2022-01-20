coins = [1, 2, 5]                                                                                                                                                                                                   
amount = 11

''' less and less
1 2 3 4 5 
1 2 2 ...
'''
def f():
  arr = [99] * (amount+1)
  arr[0] = 0 
  for c in coins:
    for i in range(c, amount+1):
      arr[i] = min(arr[i-c]+1, arr[i])
  pass
  print(arr)

f()
