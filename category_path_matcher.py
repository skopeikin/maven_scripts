__author__ = 'skopeikin'
file_new=open('files/404-old-sku-path')
file_old=open('files/new_sku_pathes')
file_match=open('match2','w')
file_notmatch=open('unmatch2','w')

new_pathes=file_new.readlines()
new_pathes_dict={line.strip().split("\t")[1]:line.strip().split("\t")[0] for line in new_pathes}
old_pathes=file_old.readlines()
old_pathes_dict={line.strip().split("\t")[0]:line.strip().split("\t")[1] for line in old_pathes}
new_pathes_keys=new_pathes_dict.keys()
old_pathes_keys=old_pathes_dict.keys()
for key in new_pathes_keys:
    if key in old_pathes_keys:
        file_match.write(key+"\t"+new_pathes_dict.get(key)+"\t"+old_pathes_dict.get(key)+"\n")
    else:
        file_notmatch.write(key+"\t"+new_pathes_dict.get(key)+"\n")
for key in old_pathes_dict:
    if key not in new_pathes_dict:
        file_notmatch.write(key+"\t"+old_pathes_dict.get(key)+"\n")
file_new.close()
file_old.close()
file_match.close()
file_notmatch.close()
