s = "meetcode"
wordDict = ["meet", "code"]
wordDict = ["meet", "etc", "etcode"]

kvs = {} #{m:[meet]}
for x in wordDict:
  if x[0] in kvs:
    kvs[ x[0] ].append(x)
  else:
    kvs[ x[0] ] = [x]
kmp = {} #word:[0,2] kmp漂移
for x in wordDict:
  tmps = []
  for i,k in enumerate(x):
    if k in kvs:
      tmps.append(i)
  kmp[x] = tmps
print(kmp)
'''
meetcode
meet
    code
'''
def test(s, l, i):
  if i >= l:
    return

  x = s[i]
  if not x in kvs: 
    return
  ws = kvs[x]
  for w in ws:
    if s[i: i+len(w)] == w:
      if i+len(w) == l:
        print("hit")
        return
      for j in kmp[w][1:]:
        test(s, l, i+j+1)
      test(s, l, i+len(w))


test(s, len(s), 0)
