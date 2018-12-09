import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

print(sigmoid(1))

#def solve_quad(a, b, c, d, e, iters=1000):
def solve_quad(a, b, c, iters=100):
    f = lambda x: a * x ** 2 + b * x + c
    #f = lambda  x: a * x ** 4 + b* x ** 3+ c * x ** 2 + d * x + e
    df = lambda x: 2 * a * x + b
    #df = lambda x: 4 * a * x ** 3 + 3 * b * x ** 2 + 2 * c * x + d
    x = 0
    try:
        for _ in range(iters):
             x -= f(x) / df(x)
        return x
    except:
        return 'x'


MIN_ROOT = -1
MAX_ROOT = 1

train_x = open("train.x", "w")
train_y = open("train.y", "w")
test_x = open("test.x", "w")
test_y = open("test.y", "w")
def make(n_samples, n_degree):
    global MIN_ROOT, MAX_ROOT
    y = np.random.uniform(MIN_ROOT, MAX_ROOT, (n_samples, n_degree))
    #y.sort(axis=1)
    X = np.array([np.poly(_) for _ in y])
    return X, y

# toy case
X, y = make(1, 4)
print(X[0][0], X[0][1],X[0][2],X[0][3])
print(y[0][0], y[0][1], y[0][2], y[0][3])



#print(solve_quad(1,1,1))


for i in range (100000):
    X, Y = make(1, 4)
    if i < 70000:
        train_x.write(str(sigmoid(X[0][0]))+" "+str(sigmoid(X[0][1]))+" "+str(sigmoid(X[0][2]))+" "+str(sigmoid(X[0][3]))+" "+str(sigmoid(X[0][4])))
        train_y.write(str(sigmoid(Y[0][0])))
        train_x.write("\n")
        train_y.write("\n")
    else:
        test_x.write(str(sigmoid(X[0][0]))+" "+str(sigmoid(X[0][1]))+" "+str(sigmoid(X[0][2]))+" "+str(sigmoid(X[0][3]))+" "+str(sigmoid(X[0][4])))
        test_y.write(str(sigmoid(Y[0][0])))
        test_x.write("\n")
        test_y.write("\n")

train_y.close()
train_x.close()
test_x.close()
test_y.close()
