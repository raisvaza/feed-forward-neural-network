import math
import sys

def linear(x: float) -> float:
    return x

def sigmoid(x: float) -> float:
    return 1/(1 + math.exp(-x))

def relu(x: float) -> float:
    return max(0,x)

def convert(tuple):
    return tuple[0] * 10** tuple[1]

def softmax(x_array: list):
    # print("input array:  ", x_array)
    # print("x: ", x)
    

    def bagi(tup1, tup2):
        num = tup1[0]/tup2[0]
        pangkat = tup1[1]-tup2[1]
        while (num > 10):
            num /= 10
            pangkat += 1
        while (num < 1):
            num *= 10
            pangkat -= 1
        return [num, pangkat]

    def tambah(tup1, tup2):
        pangkat_max = max(tup1[1], tup2[1])
        if (pangkat_max-tup1[1] > 5):
            return tup2
        if (pangkat_max-tup2[1] > 5):
            return tup1
        if (pangkat_max == tup1[1]):
            while (tup2[1] > pangkat_max):
                tup2[1] -= 1
                tup2[0] *= 10
            while (tup2[1] < pangkat_max):
                tup2[1] += 1
                tup2[0] /= 10
        if (pangkat_max == tup2[1]):
            while (tup1[1] > pangkat_max):
                tup1[1] -= 1
                tup1[0] *= 10
            while (tup1[1] < pangkat_max):
                tup1[1] += 1
                tup1[0] /= 10 
        return [tup1[0]+tup2[0], pangkat_max]
    def f_x(val):
        val = val[0]
        hasil2 = 1
        iterate = 0
        if (val > 709):
            while (val > 0):
                if (val > 709):
                    val -= 709
                    iterate += 1
                else:
                    hasil2 *= math.exp(val)
                    val = 0

            hasil1 = math.exp(709)
            pangkat10 = 0
            while (hasil1 > 10):
                hasil1 /= 10
                pangkat10 += 1
            hasil1 *= iterate
            pangkat10 *= iterate
            # print(hasil1)
            # print(pangkat10)
            # print(iterate)
            while (hasil2 > 10):
                hasil2 /= 10
                pangkat10 += 1
            hasil2 *= hasil1
            # print(hasil2, pangkat10)
            return [hasil2, pangkat10]
        else:
            return [math.exp(val), 0]
        
    x_array = [[i, 0] for i in x_array] 
    
    sumExpElmt = [0, 0]
    for elmt in x_array:
        print("elmt", elmt)
        
        f_xx = f_x(elmt)
        print("f_xx", f_xx)
        
        sumExpElmt = tambah(sumExpElmt, f_xx)
    print("sumExpElmt", sumExpElmt)

    output_array = []
    for x in x_array:
        # output_array.append(x/sumExpElmt)
        output_array.append(bagi(x, sumExpElmt))
    print("output_array", output_array)
    output_array2 = []
    for elmt in output_array:
        if elmt[1] < -322:
            output_array2.append(0)
        elif elmt[1] > 307:
            output_array2.append(sys.maxsize)
        else:
            output_array2.append(elmt[0] * (10 ** elmt[1]))
    print("output_array2", output_array2)
    
    # sumExpElmt = 0
    # x_array = [i[0] for i in x_array]
    # for elmt in x_array:

    #     # try:
    #     #     sum
    #     x = math.exp(elmt)
    #     print(x)
    #     sumExpElmt += x
        
        
    #     # except: 
    #     #     elmt_hasil = f_x(elmt)

    #     #     sumExpElmt = sys.maxsize
    # # print("sumExpElmt", sumExpElmt)
    # print(sumExpElmt)

    # output_array = []
    # for x in x_array:
    #     output_array.append(x/sumExpElmt)
    # print("output_array", output_array)
    # # output_array2 = [x[0] for x in output_array]
        
    #     # try:
    #     #     # returnable = math.exp(x)
    #     #     output_array.append(math.exp(x)/sumExpElmt)
    #     # except:
    #     #     # returnable = sys.maxsize
    #     #     output_array.append(sys.maxsize/sumExpElmt)
    #     # output_array.append(returnable/sumExpElmt)
        
    return output_array2

def convertToTuple(value):
    temp_array = []
    nilai = value
    pangkat = 0
    while(abs(nilai) > 1):
        nilai /= 10
        pangkat += 1
        
    temp_array.append(nilai)
    temp_array.append(pangkat)
    return temp_array

def add(value1, value2):
    nilai = 0
    pangkat = 0
    if (value1[1] > value2[1]):
        while (value1[1] > value2[1]):
            value2[0] /= 10
            value2[1] += 1
        nilai = value1[0] + value2[0]
        pangkat = value1[1]
    elif (value1[1] < value2[1]):
        while (value1[1] < value2[1]):
            value1[0] /= 10
            value1[1] += 1
        nilai = value1[0] + value2[0]
        pangkat = value1[1]
    return 0
