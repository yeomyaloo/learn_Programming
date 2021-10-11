from typing import MutableSequence

def shell_sort(array):
    n = len(array)
    h = n//2 # 4-정렬/ 2-정렬/ 1-정렬 수행할 것

    whlie h > 0:
        for i in range(h,n):
            j = i - h
            tmp = array[i]
            while j >= 0 and array[j] > tmp: #4-정렬인 경운 array[0] > tmp(=array[4]])
                array[j+h] = array[j]
                j -= h
            array[j+h] = tmp

            h//=2
            
                
    
