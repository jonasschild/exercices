import numpy as np

f = open('precip_data_1.txt', 'r')
prec1 =[]
prec2 =[]

for x, line in enumerate(f):
    if x >= 3291 and x <= 42003:
        comas1 = ','.join(line.split())
        splitLine1 = comas1.split(',')
        prec1.append(float(splitLine1[2]))
    elif x >= 1 and x <=3290:
        comas2 = ','.join(line.split())
        splitLine2 = comas2.split(',')
        prec2.append(float(splitLine2[2]))

prec1.extend(prec2)

print('minimum is:', np.min(prec1))
print('maximum is:', np.max(prec1))
print('mean is:', np.mean(prec1))



f.close()

#Finished