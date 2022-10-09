# hypothesis testing:
# List method .sort(with slice() as key function) works as fast as simple .sort()
# compare timings

import random
import string
import datetime

def MyFn(s):
  return s[:10]

letters=string.ascii_lowercase
l=[]

for i in range(1000000):
    ss=''
    for i in range(30):
      ss+=random.choice(letters)
    #print(ss)
    l.append(ss)

print('*')

l1=l.copy()
l2=l.copy()
l3=l.copy()
l11=l.copy()
l21=l.copy()
l31=l.copy()
l111=l.copy()
l211=l.copy()
l311=l.copy()

print('simple .sort()')
st1=datetime.datetime.now().timestamp()
l1.sort()
fin1=datetime.datetime.now().timestamp()
print(fin1-st1)

st11=datetime.datetime.now().timestamp()
l11.sort()
fin11=datetime.datetime.now().timestamp()
print(fin11-st11)

st111=datetime.datetime.now().timestamp()
l111.sort()
fin111=datetime.datetime.now().timestamp()
print(fin111-st111)

print('\nsort with MyFn')
st2=datetime.datetime.now().timestamp()
l2.sort(key=MyFn)
fin2=datetime.datetime.now().timestamp()
print(fin2-st2)

st21=datetime.datetime.now().timestamp()
l21.sort(key=MyFn)
fin21=datetime.datetime.now().timestamp()
print(fin21-st21)

st211=datetime.datetime.now().timestamp()
l211.sort(key=MyFn)
fin211=datetime.datetime.now().timestamp()
print(fin211-st211)

print('\nsort with MyFn, reverse')
st3=datetime.datetime.now().timestamp()
l3.sort(key=MyFn, reverse=True)
fin3=datetime.datetime.now().timestamp()
print(fin3-st3)

st31=datetime.datetime.now().timestamp()
l31.sort(key=MyFn, reverse=True)
fin31=datetime.datetime.now().timestamp()
print(fin31-st31)

st311=datetime.datetime.now().timestamp()
l311.sort(key=MyFn, reverse=True)
fin311=datetime.datetime.now().timestamp()
print(fin311-st311)

# results (2 turns):

# simple .sort()
# 0.3618202209472656
# 0.3661668300628662
# 0.3598899841308594
# 0.35790514945983887
# 0.3662090301513672
# 0.3566288948059082

# sort with MyFn
# 0.4809691905975342
# 0.49204492568969727
# 0.4828190803527832
# 0.5336320400238037
# 0.5332598686218262
# 0.5427169799804688

# sort with MyFn, reverse
# 0.4949350357055664
# 0.5246028900146484
# 0.5309109687805176
# 0.5518741607666016
# 0.5212829113006592
# 0.5242209434509277