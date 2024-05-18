x,y,z = input("expression: ").split()
x=int(x)
z=int(z)
if y== "+" :
    ans=float(x + z)
    print(ans)
elif y== "-" :
    ans=float(x - z)
    print(ans)
elif y== "*" :
    ans=float(x * z)
    print(ans)
elif y== "/" :
    if z== 0:
        print("divisor cannot be zero ")
    else:
      ans=float(x / z)
      print(ans)
else:
    print("invalid operator")
