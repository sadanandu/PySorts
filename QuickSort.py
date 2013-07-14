def QuickSortStable(array):
    """Takes lot of space but it's a stable sort"""
    if len(array) <=1:
        return array
    pivot = array[0]
    greater = list()
    lesser = list()
    for eachItem in array[1:]:
        if eachItem > pivot:
            greater.append(eachItem)
        else:
            lesser.append(eachItem)
    sortedLesser = QuickSortStable(lesser)
    sortedGreater = QuickSortStable(greater)
    sortedLesser.append(pivot)
    sortedLesser.extend(sortedGreater)
    return sortedLesser

def QuickSortFirstElementPivot(array, lower, upper):
    """Partitions array on first element of array
      Worst case performance if list is already sorted"""
    if lower < upper:
        j = PartitionFirstElementPivot(array, lower, upper)
        QuickSortFirstElementPivot(array, lower, j - 1)
        QuickSortFirstElementPivot(array, j+1, upper)

##def PartitionFirstElementPivot(array, lower, upper):
##    pivotIndex = lower
##    left = lower  + 1
##    right = upper -1
##    while(left <= right):
##        while(left <= right and array[left] < array[pivotIndex]):
##            left += 1
##        while(array[right] > array[pivotIndex]):
##            right -= 1
##
##        if left<right:
##            array [left], array[right] = array[right], array[left]
##    array[pivotIndex], array[right] = array[right], array[pivotIndex]
##    return right

def PartitionFirstElementPivot(array, left, right):
    pivotIndex =  left
    pivotValue = array[pivotIndex]
    array[pivotIndex], array[right]  = array[right], array[pivotIndex]
    storeIndex = left
    for i in range(left, right):
      if array[i] <= pivotValue:
          array[i], array[storeIndex] = array[storeIndex], array[i]
          storeIndex = storeIndex + 1
    array[storeIndex], array[right] = array[right], array[storeIndex]
    return storeIndex

def QuickSortMedainPivot(array, lower, upper):
    """Partitions array on median of start and end endices"""
    if lower < upper:
        j = PartitionMedianPivot(array, lower, upper)
        QuickSortMedainPivot(array, lower, j-1)
        QuickSortMedainPivot(array, j+1, upper)

def PartitionMedianPivot(array, left, right):
    pivotIndex =  (left+right)/2
    pivotValue = array[pivotIndex]
    array[pivotIndex], array[right]  = array[right], array[pivotIndex]
    storeIndex = left
    for i in range(left, right):
      if array[i] <= pivotValue:
          array[i], array[storeIndex] = array[storeIndex], array[i]
          storeIndex = storeIndex + 1
    array[storeIndex], array[right] = array[right], array[storeIndex]
    return storeIndex



#import time
##import random
##inputArray = list()
##for item in range(10):
##    inputArray.append(random.randint(1,1000))
###start = time.time()
##inputArray = [22,36,6,79,26,45,75,13,31,62,27,76,33,16,62,47]
###inputArray = [31,33,36]
##array = inputArray[:]
###array = QuickSortSimple(array)
##QuickSortInPlace(array, 0, len(array)-1)
##assert sorted(inputArray) == array
###print QuickSortSimple([10,2,45,5,23,64,6,4,354,343,3,1])
###end = time.time()
###print end - start

