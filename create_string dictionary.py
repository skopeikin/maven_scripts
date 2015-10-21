__author__ = 'skopeikin'
file = open('categories')
lines = file.readlines()
file_output=open('ccategories_string_dictionary','w')
dict=''
for line in lines:
    line=line.strip()
    dict=dict+line
file_output.write(dict)
file_output.close()
file.close()
