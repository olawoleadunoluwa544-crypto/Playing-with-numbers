large_num=int(input("enter a larger number: "))
small_num=int(input("enter the smaller number"))

while (small_num):
    num_store=small_num
    small_num=large_num%small_num
    large_num=num_store

print(f"HCF of is {large_num}")