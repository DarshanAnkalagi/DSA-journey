class solution():
    def q_sort(self,arr,low,high):
        pivot=low
        i=low
        j=high
        while i<j:
            while arr[i]<=arr[pivot] and i<=high-1:
                i+=1
            while arr[j]>arr[pivot]and j>=low+1:
                j-=1
            if i<j:
                arr[i],arr[j]=arr[j],arr[i]
        arr[low],arr[j]=arr[j],arr[low]
        
        return j


    def fun(self,arr,low,high):
        if low<high:
            pivot=self.q_sort(arr,low,high)
            self.fun(arr,low,pivot-1)
            self.fun(arr,pivot+1,high)
obj=solution()
arr=[4,3,1,8,5,9,4]
obj.fun(arr,0,len(arr)-1)
print(arr)
#Time complexity:-O(n*log(n))
#space complexity;-O(n+log(n))=O(n)
    
