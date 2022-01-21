s1="acbcbcef"
s2="abcbced"

print(s1, s2)
'''
acbcbcef
a bcbced                                                                                                                                                                                                            
'''
def f():
  l1 = len(s1)
  l2 = len(s2)
  a = [ [0]*l1 for _ in range(l2) ]
  for i in range(l2): # not s1 !!! 颠倒则错
    for j in range(l1):
      if s2[i] == s1[j]:
        if i>0 and j>0:
          a[i][j] = a[i-1][j-1] + 1
        else:
          a[i][j] = 1
  for x in a:
    print(x)
f()
