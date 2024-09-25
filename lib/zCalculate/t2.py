sandRange = [0.5, 1, 2, 5, 10, 20, 50, 80, 120]
sand1 = [6, 26.5, 11.5, 11, 31, 8.7, 15.5, 30]
sand2 = [18, 24, 7, 5, 13, 15, 2, 7.9]
sand3 = [10, 11, 9, 9, 11, 13.3, 9, 10]

sandD = [0.75,1.5,3.5,7.5,15,35,65,100]
p1,p2,p3 = [],[],[]
for i in range(len(sandD)):
    p1.append(sand1[i]/sum(sand1))
    p2.append(sand2[i]/sum(sand2))
    p3.append(sand3[i]/sum(sand3))
v1 = sum(sandD[i] * p1[i] for i in range(len(sandD)))/sum(p1)
v2 = sum(sandD[i] * p2[i] for i in range(len(sandD)))/sum(p2)
v3 = sum(sandD[i] * p3[i] for i in range(len(sandD)))/sum(p3)
print(v1,v2,v3)