
reader = open("installed.txt",'r')
content = reader.read()
reader.close()

lines = content.split("\n")[2:-1]
# skipping the first two lines and the last line of text

writer = open("requirements.txt",'w')

for line in lines:
    print(line.split())
    package, version = line.split()
    new_line = package + "==" + str(version) + "\n"
    writer.write(new_line)

writer.flush()
writer.close()

