class solution:
    def fun(self,arr):
        
        hashh={}
        for i in range(0,len(arr)):
            if arr[i] not in hashh:
                hashh[arr[i]]=0
            hashh[arr[i]]=+1
        print(hashh)
        #instead of printing dict directly we can dp below step:-
        #for key, val in hashh.itrms():
        #print(key,val)

        
obj=solution()
arr=[2,3,3,1,5,4,5,0]
arr.sort()

obj.fun(arr)


