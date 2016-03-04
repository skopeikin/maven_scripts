__author__ = 'skopeikin'
def create_dictionary_from_files (filename1, filename2):
    file = open(filename1)
    lines = file.readlines()
    file_output=open(filename2, "w")
    dict=''
    for line in lines:
        line=line.strip()
        dict=dict+line
    file_output.write(dict)
    file_output.close()
    file.close()
create_dictionary_from_files("skuurls.txt","items_dict2")