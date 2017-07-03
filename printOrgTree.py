x=raw_input("Please input the line number")
function printLine(x)
file=open("input.txt","r")
i=file.readlines()
print i[x]
