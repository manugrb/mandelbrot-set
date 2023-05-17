import numpy
import random
import tkinter


# f(z) = z² + c
# where c = a + bi with a and b being rational numbers and i being i.

pixels = [[]]
        

def devergesToInfinity(a, b):

    # we are representing z with the 2 variables za and zb, which correspond to the real and imaginary part in z like this: z = za + zb * i.
    # at the beginning z is 0. Therefore the real and imaginary part are both 0.
    za = 0
    zb = 0

    maxIterations = 1000

    for iteration in  range(maxIterations):

        # to figure out if z is further than 2 away from 0, we square the real and imaginary part, add them and check if the result is bigger than 2².
        if((za * za + zb * zb) >= 2 * 2):
            # for this c f(z) will diverge to infinity
            return True

        newResult = f(za, zb, a, b)
        za = newResult[0]
        zb = newResult[1]

    return False
    



# this is the function, that represents f(z) = z² + c. It takes in z and c as its real and imaginary components (za and zb for z and a and b for c) and returns the result as an array of 2 numbers, where the first represents the real and the second the imaginary part of the result.
def f(za, zb, a, b):

    # since (a + bi)² = a² - b² + 2abi, we know, that z² = za² - zb² + 2 * za * zb * i. This result can be stored in a real and imaginary part again: zz = zza + zzb * i with zza = za² - zb² and zzb = 2 * za * zb.
    # 
    # zza and zzb will be the real and imaginary part of the result of squaring z.

    zza = za * za - zb * zb
    zzb = 2 * za * zb

    # adding complex number is simple. (zza + zzb * i) + (a + b * i) = zza + a + (zzb + b) * i.   

    resulta = zza + a
    resultb = zzb + b

    return [resulta, resultb]


for a in numpy.arange(-1.4, -1.35, 0.000125):
    column = []
    for b in numpy.arange(-0.025, 0.025, 0.000125):
        column.append(devergesToInfinity(a, b))

    print(a)
    pixels.append(column)