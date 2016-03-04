__author__ = 'skopeikin'
def column_to_string_converter (file_input_name):
    file_input = open(file_input_name)
    lines = file_input.readlines()
    file_input.close()
    string_line='('
    for line in lines:
        line=line.strip()
        string_line=string_line+line+','
column_to_string_converter('files/pr')

