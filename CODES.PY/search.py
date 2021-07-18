class lsearch:
 
     def findbig(self,large,ar):
         for i in range(len(ar)):
            if(ar[i]>self.large):
               self.large=ar[i]
     print('the biggest number is',self.large)


num=[3,66,98,4]
ob=lsearch
big=-99
ob.findbig(big,num)
