n = int(input())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))


def solve():
    pass


solve()


def first_solve():

    nums1.sort()
    nums2.sort()

    if nums1 == nums2:
        print("YES")
    else:
        print("NO")


first_solve()
