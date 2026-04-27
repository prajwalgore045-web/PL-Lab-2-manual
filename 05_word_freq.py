s=input().split();freq={};
for w in s:freq[w]=freq.get(w,0)+1
print(freq)