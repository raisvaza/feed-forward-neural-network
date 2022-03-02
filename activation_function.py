import math

def linear(x: float) -> float:
    return x

def sigmoid(x: float) -> float:
    return 1/(1 + math.exp(-x))

def relu(x: float) -> float:
    return max(0,x)

def softmax(x: float, x_array: list) -> float:
    sumExpElmt = 0

    for elmt in x_array:
        try:
            sumExpElmt += math.exp(elmt)
        except: 
            sumExpElmt += float('inf')

    try:
        returnable = math.exp(x)
    except:
        returnable = float('inf')
        
    return returnable/sumExpElmt