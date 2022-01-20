s = "abcabcdbb"
'''
abcabcdbb
abc
 bca
  cab
   abcd
'''
def f(s, i, j, ss):
  print(s,i,j,s[i:j])
  if j >= len(s):
    print("max: ", ss)
    return
  #ix, j+1, ssx
  #found in s[i:j] <-
  for x in range(j-1, i-1, -1):
    if s[x] == s[j]:
      #found in ss ->
      for y in range(j+1, len(s)):
        if s[y] in s[x+1:y]:
          j = y - 1
          break
      #get the max ss
      if j - x > len(ss):
        ss = s[x+1:j+1]
      return f(s, x + 1, j+1, ss)
  print("error")

i = 0
for x in range(len(s)):
  if s[x] in s[:x]:
    i = x
    break
f(s, 0, i, s[:x])
