def selec_sort(array): #function takes unsorted array as the input

    for i in range(len(array)):
        #at the end of every ith loop,
        #we will have sorted array till ith index
        temp=0
        min=array[i]
        for j in range(i,len(array)):
            # this array is used to compare the ith element with
            #rest of the unsorted array to find minimum value
             if(min<array[j]):
                 min = array[j]
                 min_index=j
                 #saving information about the minimum value

        if index not == i:
            #swapping the minimum value to ith position
            temp=array[i]
            array[i]=min
            array[min_index]=temp

    return array
