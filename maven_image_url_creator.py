__author__ = 'skopeikin'
file = open ("export_product.csv", encoding="utf8")
file_output = open("export_images.txt","w",encoding="utf8");
lines = file.readlines()
for line in lines:
    urls=[]
    splitted = line.split(",")
    images = splitted[0]
    splitted_images=images.split(";")
    for image in splitted_images:
            if len(image)>0:
                url="https://funandfunction.com/media/catalog/product"+image[0:2]+"/"+image[2]+image;
            else:
                url=image
            urls.append(url)
    final_string = str(urls) +";"+splitted[1];
    file_output.write(final_string)
file.close()
file_output.close()
