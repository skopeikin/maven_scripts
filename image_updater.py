__author__ = 'skopeikin'
file1=open('images')
file2=open('gallery_file')
file_output=open('correct_gallery','w')
lines1=file1.readlines()
lines2=file2.readlines()
for i in range (0,len(lines1)):
    lines1[i]=lines1[i].strip()
    lines2[i]=lines2[i].strip()
    final_line=''
    if lines2[i]=='':
        final_line=final_line+lines1[i]+lines2[i]+'\n'
    else:
        final_line=final_line+lines2[i]+'#'+lines1[i]+'\n'
    file_output.write(final_line)
file_output.close()
file2.close()
file1.close()
