__author__ = 'skopeikin'
file_new=open('new_url_ids')
file_old=open('old_url_ids')
file_301=open('301_categories','w')

new_urls=file_new.readlines()
new_urls_dict={line.strip().split("\t")[0]:line.strip().split("\t")[1] for line in new_urls}
old_urls=file_old.readlines()
old_urls_dict={line.strip().split("\t")[0]:line.strip().split("\t")[1] for line in old_urls}
new_urls_keys=new_urls_dict.keys()
old_urls_keys=old_urls_dict.keys()
for key in new_urls_keys:
    if key in old_urls_keys:
        file_301.write("Redirect 301"+" "+old_urls_dict.get(key)+" "+new_urls_dict.get(key)+"\n")
file_new.close()
file_old.close()
file_301.close()