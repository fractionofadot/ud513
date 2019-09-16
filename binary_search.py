


def binary_search(input_array, value):
    start = 0
    end = len(input_array) - 1
    while start <= end:
        mid = int((start+end) / 2)
        if input_array[mid] == value:
            return mid
        elif input_array[mid] < value:
            start = mid + 1
        else:
            end = mid - 1

    return -1



def binary_search_old(input_array, value):
    """Your code goes here."""
    length = len(input_array)

    start = 0
    end = length-1
    half = int(length / 2)

    first = input_array[0]
    last = input_array[-1]
    searched = 0
    
    while half != 0:
        value_at_half = input_array[half]

        if value == value_at_half:
            print("searched", searched)
            return half
        if value < value_at_half:
            end = half
            half = int(half/2)
        if value > value_at_half:
            start = half
            half = half + int((end - start) / 2)
            if half == start:
                half+=1
        searched += 1
        if searched == length:
            break     
    return -1


