from scipy.special import lambertw
from scipy.special import factorial
import numpy as np
from intersect import intersection
import matplotlib.pyplot as plt
import math


def calculate_lambert(x):
    return (1 + (lambertw((-1 * x * np.power(np.e, -1 * x)))) / x)

def calculate_s_by_lambert(mean_k):
    c = np.arange(1.1, 5.0, 0.1)
    s = calculate_lambert(c)

    plt.plot(c,s.real)
    plt.xlabel('c')
    plt.ylabel('s')
    plt.savefig('lambert.svg')
    plt.close()
    s=calculate_lambert(mean_k).real.astype(np.float32)
    return s

def calculate_s_by_curves_intersections(mean_k):
    x = np.arange(0, 1.1, 0.1)
    y = 1 - np.power(np.e, -1 * mean_k * x)
    plt.plot(x, y)
    plt.plot(x, x, '-r')
    plt.xlabel('S')
    plt.ylabel('y')
    plt.xticks(np.arange(0, 1.1, 0.1))
    plt.yticks(np.arange(0, 1.1, 0.1))
    _x, _y = intersection(x, y, x, x)
    plt.plot(_x, _y, "*k")

    plt.savefig('giant_component_size_curve_intersection.svg')
    plt.close()
    return list(_x)


def calculate_probability_k_max(k_max,mean_k):

    return np.power(np.e,-1*mean_k)*(np.power(mean_k,k_max+1))/factorial(k_max+1)


def calculate_kmax_from_guess(N,mean_k):
    ideal_max_count=1
    k_max=np.floor(mean_k)-1
    difference=float('inf')
    while difference > 1:
        k_max += 1
        p_max=calculate_probability_k_max(k_max,mean_k)
        k_max_count=p_max*N
        difference=k_max_count-ideal_max_count
    return int(k_max)




def calculate_s_by_binary_search(mean_k):
    s = 0.5
    min_s, max_s = 0, 1
    dif = s - 1 + math.exp(-mean_k * s)
    while math.fabs(dif) > 1e-5:
        if dif > 0:
            max_s = s
        else:
            min_s = s
        s = (min_s + max_s) / 2
        dif = s - 1 + math.exp(-mean_k * s)

    return s


def calculate_k_max_by_series(N,mean_k):
    k_max_the = math.floor(mean_k - 1)
    critical = 1 - 1 / N
    f_k_max = 0
    while f_k_max < critical:
        k_max_the += 1
        f_k_max = 0
        for k in range(0, k_max_the + 1):
            f_k_max = f_k_max + (mean_k ** k) / math.factorial(k)
        f_k_max = math.exp(-mean_k) * f_k_max

    return k_max_the
