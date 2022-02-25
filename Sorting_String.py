"""
Caroline Forbes is an intelligent girl, every time she wins in any contest or programme, 
and solves complex problems so I want to give her a challenge problem that is. 
Sort an array of strings according to string lengths. 
If you are smarter than her, try to solve the problem faster than her? 
Input 
You           are       beautiful          looking 
Output 
You           are       looking            beautiful     
"""
def sort(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            temp=""
            if(arr[i].len()>arr.len()):
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
                

arr=["you","are","looking","beautiful"]
n=len(arr)
sort(arr,n)
for i in range(n):
    print(arr[i]+" ")