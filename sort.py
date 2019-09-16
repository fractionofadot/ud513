import random

def color(string,c="red"):
    colors = {
        "purple" : '\033[95m',
        "cyan" : '\033[96m',
        "darkcyan" : '\033[36m',
        "blue" : '\033[94m',
        "green" : '\033[92m',
        "yellow" : '\033[93m',
        "red" : '\033[91m',
        "bold" : '\033[1m',
        "underline" : '\033[4m',
        "end" : '\033[0m'
    }
    return colors[c] + str(string) + colors["end"]


def pretty_print(a,pivot,s1,s2):
    print("[",end='')
    for i in range(len(a)):
        ic = "blue"
        jc = "red"
        mx = "purple"
        pc = "underline"

        if i == len(a)-1:
            cm = "]\n"
        else:
            cm = ", "

        if i == a.index(pivot):
            if i == s1 == s2:
                pd = color(color(a[i],pc),mx)
            elif i == s1:
                pd = color(color(a[i],pc),ic)
            elif i == s2:
                pd = color(color(a[i],pc),jc)
            else:
                pd = color(a[i],pc)
            print(pd + cm, end='')
        elif s1 == i:
            print(color(a[i],ic) + cm, end='')
        elif  s2 == i:
            print(color(a[i],jc) + cm, end='')
        else:
            print(str(a[i]) + cm, end='')
# Lomuto
def quicksort_lomuto(a, lo=0, hi=None):
    if hi == None:
        hi = len(a) - 1
    if lo < hi:
        p = partition_lomuto(a, lo, hi)
        quicksort(a, lo, p - 1)
        quicksort(a, p + 1, hi)
    return a

def partition_lomuto(a, lo, hi):
    pivot = a[hi]
    i = lo
    for j in range(lo,hi):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i = i + 1
    a[i], a[hi] = a[hi], a[i]
    return i

def quicksort_hoare(a, lo=0, hi=None):
    if hi == None:
        hi = len(a)-1
    if lo < hi:
        p = partition_hoare(a, lo, hi)
        quicksort_hoare(a, lo, p)
        quicksort_hoare(a, p + 1, hi)

    return a

def partition_hoare(a, lo, hi):
    pivot = a[int(lo + (hi - lo) / 2)]
    print("pivot:", pivot, "lo:", lo, "hi:", hi)
    pretty_print(a,pivot,None,None)
    i = lo - 1
    j = hi + 1

    while True:
        while True:            
            i = i + 1
            pretty_print(a,pivot,i,j)
            if not a[i] < pivot:
                break
        while True:
            j = j - 1
            pretty_print(a,pivot,i,j)
            if not a[j] > pivot:
                break
        if i >= j:
            return j
        print("swap", a[i], a[j])
        a[i], a[j] = a[j], a[i]
        pretty_print(a,pivot,i,j)


# Parker
def p_quicksort(array):
    pivot = len(array) - 1
    i = 0


    # check pivot against first element
    # if pivot is lower, a[p]=a[0], a[0]=a[p-1], a[p-1]=a[p]
    # if pivot is higher, move to next element
    while pivot != 0:
        print(array,pivot,i)
        if array[pivot] < array[i]:
            temp = array[pivot-1]
            if pivot-i == 1:
                array[pivot-1] = array[pivot]
                array[pivot] = temp
            else:
                array[pivot-1] = array[pivot]
                array[pivot] = array[i]
                array[i] = temp

            pivot = pivot - 1
            
        elif array[pivot] > array[i]:
            i = i + 1

        if pivot == i:
            i = 0
            pivot = len(array) -1




    return array

test = [8,3,1,7,0,10,2]
test2 = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
t3 = [6, 1, 5, 9, 7, 2, 8, 3, 0, 4]
t4 = [4, 6, 0, 1, 9]
print (quicksort_hoare(t4))