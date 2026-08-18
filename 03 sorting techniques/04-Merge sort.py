class solution:
    def merge(self,arr,low,mid,high):
        left,right=low,mid+1
        temp=[]
        while left<=mid and right<=high:
            if arr[left]<=arr[right]:
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                right+=1
        while left<=mid:
            temp.append(arr[left])
            left+=1
        while right<=high:
            temp.append(arr[right])
            right+=1
        for i in range(low,high+1):
            arr[i]=temp[i-low]

    def mergesort(self,arr,low,high):
        if low>=high:
            return
        mid=(low+high)//2
        self.mergesort(arr,low,mid)
        self.mergesort(arr,mid+1,high)
        self.merge(arr,low,mid,high)
obj=solution()
arr=[2,4,1,6,4,8,5,9,0]
obj.mergesort(arr,0,len(arr)-1)
print(arr)
#Time complexity:-O(n*log(n))
#space complexity;-O(n+log(n))=O(n)