#1. Bubble Sort 
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist

#2. Merge Sort 
def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
            
    return alist    

#3. Insertion Sort 
def insertionSort(alist):
    for index in range(1,len(alist)):

		currentvalue = alist[index]
		position = index

		while position>0 and alist[position-1]>currentvalue:
		 alist[position]=alist[position-1]
		 position = position-1

		alist[position]=currentvalue

    return alist

#4. Counting Sort
 def countingsort( alist, k ):
    counter = [0] * ( k + 1 )
    for i in alist:
      counter[i] += 1
 
    ndx = 0;
    for i in range( len( counter ) ):
      while 0 < counter[i]:
        alist[ndx] = i
        ndx += 1
        counter[i] -= 1

    return alist

#5. Heap Sort w. moveDown and swap
def heapSort( alist ):
  # convert aList to heap
  length = len( alist ) - 1
  leastParent = length / 2
  for i in range ( leastParent, -1, -1 ):
    moveDown( alist, i, length )
 
  # flatten heap into sorted array
  for i in range ( length, 0, -1 ):
    if alist[0] > alist[i]:
      swap( aList, 0, i )
      moveDown( alist, 0, i - 1 )
  return alist
 
 
def moveDown( alist, first, last ):
  largest = 2 * first + 1
  while largest <= last:
    # right child exists and is larger than left child
    if ( largest < last ) and ( alist[largest] < alist[largest + 1] ):
      largest += 1
 
    # right child is larger than parent
    if alist[largest] > alist[first]:
      swap( aist, largest, first )
      # move down to largest child
      first = largest;
      largest = 2 * first + 1
      return alist
    else:
      return 'something went wrong'# force exit
 
 
def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp

  return A


# Cycle Sort
def cycleSort(vector):
    "Sort a vector in place and return the number of writes."
    writes = 0
 
    # Loop through the vector to find cycles to rotate.
    for cycleStart, item in enumerate(vector):
 
        # Find where to put the item.
        pos = cycleStart
        for item2 in vector[cycleStart + 1:]:
            if item2 < item:
                pos += 1
 
        # If the item is already there, this is not a cycle.
        if pos == cycleStart:
            continue
 
        # Otherwise, put the item there or right after any duplicates.
        while item == vector[pos]:
            pos += 1
        vector[pos], item = item, vector[pos]
        writes += 1
 
        # Rotate the rest of the cycle.
        while pos != cycleStart:
 
            # Find where to put the item.
            pos = cycleStart
            for item2 in vector[cycleStart + 1:]:
                if item2 < item:
                    pos += 1
 
            # Put the item there or right after any duplicates.
            while item == vector[pos]:
                pos += 1
            vector[pos], item = item, vector[pos]
            writes += 1
 
    return vector