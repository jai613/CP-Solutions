for _ in range(int(input())):
 s=input()
 cur_day=set()
 d=0
 for i in range(len(s)):
  if s[i] not in cur_day and len(cur_day)==3:
   cur_day=set()
   cur_day.add(s[i])
   d+=1
  else:
   cur_day.add(s[i])
 print(d+1)