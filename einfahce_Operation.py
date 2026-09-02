a=float(input("a: "))
b=float(input("b: "))
op=(input("op: (+,-,*,/): "))
match op:
    case '+': print(a+b)
    case '-': print(a-b)
    case '*': print(a*b)
    case '/': print(a/b if b!=0 else "error")


    