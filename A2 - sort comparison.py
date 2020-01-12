"""
Spyder Editor

This is a temporary script file.
"""

def insertionSort(A, t): 
    if t <= 1: 
        return    
    insertionSort (A, t - 1)   
    r = A[t - 1] 
    j = t - 2  
    while (j >= 0 and A[j] > r): 
        A[j + 1] = A[j] 
        j = j - 1 
   
    A[j + 1] = r  
  
def mergeSort(A): 
    if len(A) > 1: 
        mid = len(A) // 2 
        p = A[:mid]   
        q = A[mid:]
        mergeSort(p) 
        mergeSort(q)
        i = j = k = 0       
        while i < len(p) and j < len(q): 
            if p[i] < q[j]: 
                A[k] = p[i] 
                i += 1
            else: 
                A[k] = q[j] 
                j += 1
            k += 1         
        while i < len(p): 
            A[k] = p[i] 
            i += 1
            k += 1      
        while j < len(q): 
            A[k] = q[j] 
            j += 1
            k += 1
            
def partition(A,p,q): 
    i = ( p-1 )         
    pivot = A[q]      
    for j in range(p , q): 
        if   A[j] <= pivot:  
            i = i+1 
            A[i],A[j] = A[j],A[i]   
    A[i+1],A[q] = A[q],A[i+1] 
    return ( i+1 ) 
  
def quickSort(A,p,q): 
    if p < q: 
        pi = partition(A,p,q) 
        quickSort(A, p, pi-1) 
        quickSort(A, pi+1, q)

def showArray(A): 
    for i in range( len(A )):         
        print(A[i], end=" ") 
    print()
    print()

  

if __name__ == '__main__':
    
    ''' 
    Testing opening text files
    '''
    with open('10_Random.txt') as f:
        o = [int(x) for x in next(f).split()] 
        A = []
        for line in f: 
            A.append([int(x) for x in line.split()])
 
    
        mergeSort(A) 
        showArray(A)
        
        n = len(A)
        insertionSort(A, n)
        showArray(A)
        
        quickSort(A, 0, n - 1) 
        showArray(A)
        f.close()

    with open('10_Reverse.txt') as f:
            o = [int(x) for x in next(f).split()] 
            A = []
            for line in f: 
                A.append([int(x) for x in line.split()])
     
        
            mergeSort(A) 
            showArray(A)
            
            n = len(A)
            insertionSort(A, n)
            showArray(A)
            
            quickSort(A, 0, n - 1) 
            showArray(A)
            f.close()

    with open('10_Sorted.txt') as f:
        o = [int(x) for x in next(f).split()] 
        A = []
        for line in f: 
            A.append([int(x) for x in line.split()])
 
    
        mergeSort(A) 
        showArray(A)
        
        n = len(A)
        insertionSort(A, n)
        showArray(A)
        
        quickSort(A, 0, n - 1) 
        showArray(A)
        f.close()
    
    with open('100_Random.txt') as f:
        o = [int(x) for x in next(f).split()] 
        A = []
        for line in f: 
            A.append([int(x) for x in line.split()])
 
    
        mergeSort(A) 
        showArray(A)
        
        n = len(A)
        insertionSort(A, n)
        showArray(A)
        
        quickSort(A, 0, n - 1) 
        showArray(A)
        f.close()

    with open('100_Reverse.txt') as f:
        o = [int(x) for x in next(f).split()] 
        A = []
        for line in f: 
            A.append([int(x) for x in line.split()])
 
    
        mergeSort(A) 
        showArray(A)
        
        n = len(A)
        insertionSort(A, n)
        showArray(A)
        
        quickSort(A, 0, n - 1) 
        showArray(A)
        f.close()
        
    with open('100_Sorted.txt') as f:
        o = [int(x) for x in next(f).split()] 
        A = []
        for line in f: 
            A.append([int(x) for x in line.split()])
 
    
        mergeSort(A) 
        showArray(A)
        
        n = len(A)
        insertionSort(A, n)
        showArray(A)
        
        quickSort(A, 0, n - 1) 
        showArray(A)
        f.close()
        
    with open('1000_Random.txt') as f:
        o = [int(x) for x in next(f).split()] 
        A = []
        for line in f: 
            A.append([int(x) for x in line.split()])
 
    
        mergeSort(A) 
        showArray(A)
        
        n = len(A)
        insertionSort(A, n)
        showArray(A)
        
        quickSort(A, 0, n - 1) 
        showArray(A)
        f.close()
        
    with open('1000_Reverse.txt') as f:
        o = [int(x) for x in next(f).split()] 
        A = []
        for line in f: 
            A.append([int(x) for x in line.split()])
 
    
        mergeSort(A) 
        showArray(A)
        
        n = len(A)
        insertionSort(A, n)
        showArray(A)
        
        quickSort(A, 0, n - 1) 
        showArray(A)
        f.close()
        
    with open('1000_Sorted.txt') as f:
        o = [int(x) for x in next(f).split()] 
        A = []
        for line in f: 
            A.append([int(x) for x in line.split()])
 
    
        mergeSort(A) 
        showArray(A)
        
        n = len(A)
        insertionSort(A, n)
        showArray(A)
        
        quickSort(A, 0, n - 1) 
        showArray(A)
        f.close()































