# list = [1,2,3,4,5]
# tup = (1,2,3,4,5,6,7,8,9,0)

# for val in tup :
#     print(val)

# nums = [1,4,9,16,25,36,49,64,81,100]
# for i in nums:
#     print(i)

# nums = [1,4,9,16,25,36,49,64,81,100]
# x=16

# for i in nums:
#     if i == x:
#         print("found at index" , nums.index(i))
#         break
# else:
#  print("not found")


# for i in range(10):
#     print(i)

# for i in range(100,0,-1):
#     print(i)

# n = int(input("enter a number:"))
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")

# n = int(input("enter a number:"))
# sum = 0
# for i in range(1,n+1):
#     sum+=i
# print(sum)

# n = int(input("enter a number:"))
# sum = 0
# i = 1 
# while i<=n:
#     sum+=i
#     i+=1
# print(sum)    


# n = int(input("enter a number:"))
# fact = 1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

# n = int(input("enter a number:"))
# fact = 1
# i = 1
# while i<=n:
#     fact*=i
#     i+=1
# print(fact)



# n = int(input("enter a number:"))

# for i in range(2,n):
#     if n % i ==0:
#         print("This is not prime number")
#         break
# else:
#     print("this is a prime number")

# n= int(input("enter a number:"))
# for i in range(1,n+1):
#     print(" " *(n-i),end="")
#     print("*" *(2*i-1) ,end="")
#     print("")

# n= int(input("enter a number:"))
# for i in range(1,n+1):
#     print("*" *i,end="")
#     print("")    

n= int(input("enter a number:"))
for i in range(1,n+1):
    if i==1 or i==n:
      print("*" *n,end="")
    else:
     print("*" , end="")
     print(" " * (n-2),end="")
     print("*" , end="") 
    print("") 

n= int(input("enter a number:"))
for i in range(10, 0 , -1):
    print(n*i)
  