from src.helpers import *


def get_statistics_of_random_network(N,mean_k):
    print('--- Calculcating Giant Component Size (S) ---')
    s_lambert=calculate_s_by_lambert(mean_k)
    print("calculate from lambert w function:")
    print(f"S = {s_lambert}")
    s_curves_intersections=calculate_s_by_curves_intersections(mean_k)
    print("calculate from intersections of curves:")
    for index in range(len(s_curves_intersections)):
        print(f'S({index}) = {float(s_curves_intersections[index])}')
    print("calculate from binary search:")
    s_binary_search = calculate_s_by_binary_search(mean_k)
    print(f"S = {s_binary_search}")
    print('')
    print('--- Calculcating Maximum Degree (K_max) ---')
    print("calculate from Approximation:")
    kmax_approximated=calculate_kmax_from_guess(N,mean_k)
    print(f"k_max = {kmax_approximated}")

    print("calculate from Series:")
    kmax_series=calculate_k_max_by_series(N,mean_k)
    print(f"k_max = {kmax_series}")

    return (s_lambert,*s_curves_intersections,s_binary_search,kmax_approximated,kmax_series)




if __name__ == '__main__':
    mean_k=1.5
    # mean_k=1000
    N=1000
    # N=10**9
    import sys
    if(len(sys.argv)>1):
        mean_k=float(sys.argv[1])
        N=int(sys.argv[2])
    out=get_statistics_of_random_network(N,mean_k)
    print(f'\nout = {out}')
