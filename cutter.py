__author__ = 'skopeikin'
def cut_categories(file_name):
    file = open(file_name)
    file_output = open('cutted_categories_2.txt','w')
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        while line[-8:] == '#[ROOT]/':
            line=line[:-8]
        file_output.write(line + "\n")
    file_output.close()
    file.close()
def cut_media_gallery(file_name):
    file = open(file_name)
    file_output = open('cutted_gallery_3.txt','w')
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        while line[-1:] == '#':
            line=line[:-1]
        file_output.write(line + "\n")
    file_output.close()
    file.close()
#cut_categories('new_categories')
cut_media_gallery('new_media')


