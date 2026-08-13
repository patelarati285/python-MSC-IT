password =(input("enter password: "))
upper=False
lower=False
digit=False
special=False
repeat=False
special_chars="!@#$%^&()-_+[]{}\\:;'<>,.?/"
for i in range(len(password)):
    if password[i].isupper():
        upper=True
    elif password[i].islower():
        lower=True
    elif password[i].isdigit():
        digit=True
    elif password[i] in special_chars:
        special=True
    if i>0 and password[i]==password[i-1]:
        repeat=True

print("\n Password analysis")
print("Uppercase letters:",upper)
print("Lowercase letters:",lower)
print("Digits:",digit)
print("Special characters:",special)
print("Repeated characters:",repeat)