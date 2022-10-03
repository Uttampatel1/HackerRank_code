from itertools import combinations_with_replacement


def main():
    s, n = input().split()
    s = sorted(s)
    n = int(n)
    for i in combinations_with_replacement(s, n):
        print(''.join(i))

main()
