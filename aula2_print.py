# \r\n -> CRLF
# \n -> LF

print(12, 34, sep=", ")
print(12, 34, sep=" ")
print(12, 34, )

print(12, 34, sep=", ", end="##\n")
print(12, 34, sep=" ", end="\n")
print(12, 34, )
