import sys
input_file = open(sys.argv[1], 'r')
c = input_file.readlines()
x = []
for i in c:
    ip = i
    x.append(i)
    print(i)

input_file.close()
del sys.argv[1:]
username = x[0].strip('\n')
password = x[1].strip('\n')
id = x[2].strip('\n')

# username = str(sys.argv[1])
# password = str(sys.argv[2])
# id = str(sys.argv[3])
xmlfile = open('credentials.xml', 'r')
data = xmlfile.read()
print(data)
data=data.format(username=username, password=password,id=id)
print(data)
xmlfile.close()
xmlfile = open('credentials_edited.xml', 'w')
xmlfile.write(data)
