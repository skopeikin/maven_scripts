__author__ = 'skopeikin'
file=open('categories.txt')
lines=file.readlines()
unique_categories=[]
for line in lines:
    line=line.strip()
    splitted_line=line.split('#')
    for category in splitted_line:
        if 'Brand' in category:
            splitted_category=category.split("|")
            category=splitted_category[0]+"|"+splitted_category[1]+"|"+splitted_category[2]
        else:
            pass
        if category not in unique_categories:
            unique_categories.append(category)
        else:
            pass
print(len(unique_categories))
file_output=open('unique_categories.txt','w')
for category in unique_categories:
    file_output.write(category + '\n')
file_output.close()
file.close()