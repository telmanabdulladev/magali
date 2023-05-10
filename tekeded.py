# a = int(input("ededi daxil et:"))
# b = str(a)
# s=0
# for i in range(len(b)):
#     if int(b[i])%2!=0:
#         s=s+int(b[i])
# print(s)

n = int(input("enter number: "))
s = 0
while n > 0:
    digit = n % 10
    if digit %2!=0:
        s = s + digit
    n = n // 10
print(s)