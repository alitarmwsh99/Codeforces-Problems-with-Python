#Problem Link   : https://codeforces.com/problemset/problem/785/A
#Problem Name   : Anton and Polyhedrons
#Language:      :Python 3.9.4
#Programmer     : Ali Ahmed Tarmoush
#Status         : Accepted
figures=dict()
figures["Tetrahedron"] = 4
figures["Cube"] = 6
figures["Octahedron"] = 8
figures["Dodecahedron"] = 12
figures["Icosahedron"] = 20
n=input()
n=int(n)
sum=0
while n > 0 :
    s=input()
    sum=sum+figures[s]
    n=n-1
print(sum)
