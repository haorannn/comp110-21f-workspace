left: str = input("Left-hand side: ")
right: str = input("Right-hand side: ")

exp: str = str(int(left) ** int(right))
float_num: str = str(float(left) / float(right))
int_num: str = str(int(left) // int(right))
resi: str = str(int(left) % int(right))

print(left + " ** " + right + " is " + exp)
print(left + " / " + right + " is " + float_num)
print(left + " // " + right + " is " + int_num)
print(left + " % " + right + " is " + resi)