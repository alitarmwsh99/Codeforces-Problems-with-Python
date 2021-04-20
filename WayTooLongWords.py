#Problem Link   : https://codeforces.com/problemset/problem/71/A
#Problem Name   : Way Too Long Words
#Language:      :Python 3.9.4
#Programmer     : Ali Ahmed Tarmoush
#Status         : Accepted
n=input()
n=int(n)
while n != 0 :
    string=input()
    if len(string) <= 10 :
        print(string)
    else :
        print(string[0]+str(len(string)-2)+string[len(string)-1])
    n=n-1
