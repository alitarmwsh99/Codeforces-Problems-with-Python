#Problem Link   : https://codeforces.com/problemset/problem/282/A
#Problem Name   : Bit++
#Language:      :Python 3.9.4
#Programmer     : Ali Ahmed Tarmoush
#Status         : Accepted
n=input()
n=int(n)
sum=0
for i in list(range(n)) :
    st=input()
    if st=='++X' or st=='X++' :
        sum=sum+1
    elif st=='--X' or st=='X--' :
        sum=sum-1
print(sum)
