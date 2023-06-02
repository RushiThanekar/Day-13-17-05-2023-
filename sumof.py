def summ(s):
    if s<=1:
        return 1
    return summ (s-1) + s
s=int(input("Enter no= "))
print(summ(s))