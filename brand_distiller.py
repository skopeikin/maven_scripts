__author__ = 'skopeikin'
file=open('cutted_categories.txt')
file_output=open('final_categories.txt','w')
lines=file.readlines()
for line in lines:
    line=line.strip()
    splitted_line=line.split('#')
    final_category_line=''
    for category in splitted_line:
        if 'Brand' in category:
            splitted_category=category.split("/")
            category=splitted_category[0]+"/"+splitted_category[1]+"/"+splitted_category[2]
        else:
            pass
        final_category_line=category+'#'
    final_category_line=final_category_line.strip()
    file_output.write(final_category_line + '\n')
file_output.close()
file.close()