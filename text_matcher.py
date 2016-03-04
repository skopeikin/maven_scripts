__author__ = 'skopeikin'
def find_matching_strings_in_columns (file_input_name, file_output_name) :
    file_input = open(file_input_name)
    file_output = open(file_output_name,'w')
    lines = file_input.readlines()
    column_1=[]
    column_2=[]
    matches=[]
    unmatches=[]
    for line in lines :
        line = line.strip()
        if len(line.split('\t')) >1:
            column_1.append(line.split('\t')[0])
            column_2.append(line.split('\t')[1])
    for value in column_1:
        if value in column_2:
            matches.append(value)
        else:
            unmatches.append(value)
    print("matched"+ str(len(matches)))
    print ("unmatched"+ str(len(unmatches)))
    file_input.close()
    file_output.close()
find_matching_strings_in_columns("htaccess_matching","test")
