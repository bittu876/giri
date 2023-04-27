class solution:
    def answer(x):
        a=[]
        n=int(input("enter size of list (size < 10^4)"))
        target=int(input("enter target"))
        print("enter elements into \n(note:elements should not repeat)")
        for i in range(0,n):
            b=int(input())
            a.append(b)
        for i in range(0,n):
            for j in range(i+1,n):
                 if a[i]+a[j] == target:
                   b=[]
                   b.append(i)
                   b.append(j)   
        
        print("index of elements who's sum equal to target are:",b)
               
s=solution()
s.answer()
