__author__ = 'skopeikin'
file = open('colors')
lines=file.readlines()
colors=[]
for line in lines:
    line=line.strip()
    if line not in colors:
        colors.append(line)
    else:
        pass
print(colors)
file.close()