__author__ = 'skopeikin'
file=open('final_categories.txt')
file_output=open('series_column','w')
lines=file.readlines()
print(len(lines))
series=[]
def series_finder(categories):
    for category in categories:
        if 'Series' in category and category not in series and '\n' not in category:
            series.append(category)
        if 'Series' in category and '\n' not in category  and 'Shop By Series' not in category:
            file_output.write(category +'\n')
            break
    return True
for line in lines:
    category_pathes=line.split('#')
    if 'Series' not in line:
        file_output.write(''+'\n')
    elif 'Series' in line:
        for path in category_pathes:
            #flag_series=False
            categories=path.split('/')
            for category in categories:
                if 'Series' in category and category not in series and '\n' not in category:
                    series.append(category)

print(len(series))
print(series)
file.close()