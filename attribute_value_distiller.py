__author__ = 'skopeikin'
file = open('brands')
lines=file.readlines()
attribute_values=[]
for line in lines:
    line=line.strip()
    if line not in attribute_values:
        attribute_values.append(line)
    else:
        pass
print(len(attribute_values))
print(attribute_values)
file.close()