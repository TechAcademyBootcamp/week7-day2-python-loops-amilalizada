s = input("Input a string")
d=l=0
for i in s:
    if i.isdigit():
        d=d+1
    elif i.isalpha():
        l=l+1
    
print("Letters", l)
print("Digits", d)
