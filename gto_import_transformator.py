__author__ = 'skopeikin'
file = open ("glasstileoasis_latest_feed.txt")
file_output = open("gto_different_category_path.txt","w",encoding="utf8")
file_output.write("sku\tconfigurable_product_sku\tconfigurable_product_options\ttile_amount_type\twebsites\tproduct_type\tmsrp\tcost\tprice\tstock.is_in_stock\tstock.qty\tstatus\tvisibility\tattributeset\ttax_class\tname\tcategories\tbrand\tshort_description\tmeta_title\tdescription\tcolor\tsize\tsheet_size\ttiles_per_sheet\tsold_by\tsize_dimensions\tsheets_per_sf\timage\tsmall_image\tthumbnail\tmedia_gallery\tstock_text\tweight\tship_days\tmaterial\tfinish\ticon_frostresistant\ticon_antislip\ticon_outdoors\ticon_pool\ticon_recycled\ticon_2\tinstallation_instruction_id\tsheets_per_case\torder_by_num\tsticky_note\tmeta_description\tmeta_keywords\n")
lines = file.readlines()
lines[0]=lines[0][:-1]
header=lines.pop(0).split("\t")
#item_id,brand_id,model_num,sample_sku,item_title,item_title2,sample_item_title,meta_title,specifications,sample_description,description,color,size,sheet_size,tiles_per_sheet,sold_by,size_dimensions,sheets_per_sf,price,list_price,cost_price,sample_price,large_image,large_image2,large_image3,large_image4,large_image5,large_image6,sample_image_name,in_stock,stock_text,sample_in_stock,weight,ship_days,is_active,material,finish,icon_frostresistant,icon_antislip,icon_outdoors,icon_pool,icon_recycled,icon_2,installation_instruction_id,deleted,Cat1,Cat2,Cat3,Cat4,Cat5,Cat6,Cat7,CategoryPath1,CategoryPath2,CategoryPath3,CategoryPath4,CategoryPath5,CategoryPath6,CategoryPath7=0
item_id=header.index("item_id")
brand_id=header.index("brand_id")
model_num=header.index("model_num")
sample_sku=header.index("sample_sku")
item_title=header.index("item_title")
item_title2=header.index("item_title2")
sample_item_title=header.index("sample_item_title")
meta_title=header.index("meta_title")
meta_description=header.index("meta_description")
meta_keywords=header.index("meta_keywords")
specifications=header.index("specifications")
sample_description=header.index("sample_description")
description=header.index("description")
color=header.index("color")
size=header.index("size")
sheet_size=header.index("sheet_size")
tiles_per_sheet=header.index("tiles_per_sheet")
sold_by=header.index("sold_by")
size_dimensions=header.index("size_dimensions")
sheets_per_sf=header.index("sheets_per_sf")
price=header.index("price")
cost_price=header.index("cost_price")
list_price=header.index("list_price")
sample_price=header.index("sample_price")
large_image=header.index("large_image")
large_image2=header.index("large_image2")
large_image3=header.index("large_image3")
large_image4=header.index("large_image4")
large_image5=header.index("large_image5")
large_image6=header.index("large_image6")
sample_image_name=header.index("sample_image_name")
in_stock=header.index("in_stock")
stock_text=header.index("stock_text")
sample_in_stock=header.index("sample_in_stock")
weight=header.index("weight")
ship_days=header.index("ship_days")
is_active=header.index("is_active")
material=header.index("material")
finish=header.index("finish")
icon_frostresistant=header.index("icon_frostresistant")
icon_antislip=header.index("icon_antislip")
icon_outdoors=header.index("icon_outdoors")
icon_pool=header.index("icon_pool")
icon_recycled=header.index("icon_recycled")
icon_2=header.index("icon_2")
installation_instruction_id=header.index("installation_instruction_id")
deleted=header.index("deleted")
Cat1=header.index("Cat1")
Cat2=header.index("Cat2")
Cat3=header.index("Cat3")
Cat4=header.index("Cat4")
Cat5=header.index("Cat5")
Cat6=header.index("Cat6")
Cat7=header.index("Cat7")
CategoryPath1=header.index("CategoryPath1")
CategoryPath2=header.index("CategoryPath2")
CategoryPath3=header.index("CategoryPath3")
CategoryPath4=header.index("CategoryPath4")
CategoryPath5=header.index("CategoryPath5")
CategoryPath6=header.index("CategoryPath6")
CategoryPath7=header.index("CategoryPath7")
is_hot_item=header.index("is_hot_item")
sheets_per_case=header.index("sheets_per_case")
sample_stock_text=header.index("sample_stock_text")
order_by_num=header.index("order_by_num")
sample_ship_days=header.index("sample_ship_days")
sheet_type=header.index("sheet_type")
sticky_note=header.index("sticky_note")
category_pathes_indexes=[]
category_pathes_indexes.append(CategoryPath1)
category_pathes_indexes.append(CategoryPath2)
category_pathes_indexes.append(CategoryPath3)
category_pathes_indexes.append(CategoryPath4)
category_pathes_indexes.append(CategoryPath5)
category_pathes_indexes.append(CategoryPath6)
category_pathes_indexes.append(CategoryPath7)
images_indexes=[]
images_indexes.append(large_image2)
images_indexes.append(large_image3)
images_indexes.append(large_image4)
images_indexes.append(large_image5)
images_indexes.append(large_image6)
brands={"100":"Absolut Glass","101":"Botanical Glass","122":"Champion Tile", "102":"Creative Decore", "103":"Davinci", "104":"Euro Glass", "121":"Flicker Tile", "106":"Fusion", "125":"Horizon  Tile", "107":"ISI", "120":"Jet Stone Corporation", "130":"Matrix",  "108":"Millenium Products", "119":"Moso Mosaics", "129":"Nexgen Coverings", "115":"Ocean Pool Mosaic", "109":"Ocean Water", "105":"Pacific Tile Company", "110":"Quest", "118":"Regency", "111":"Royal Tile & Stone", "112":"Solistone", "113":"Tuscan Glass", "126":"Unicorn", "117":"Universal Glass Designs", "114":"Wall Master"}
def split_category_path(index_of_category):
    splitted_path=[]
    if ">" in splitted[index_of_category]:
        splitted_path=splitted[index_of_category].split(">")
    elif splitted[index_of_category]=="\n":
        pass
    else:
        splitted_path.append(splitted[index_of_category])
    return splitted_path
def build_category_path(splitted_path):
    path=''
    for category in splitted_path:
        path=path+category+'|'
    return path[:-1]
for line in lines:
    splitted = line.split("\t")
    item_title_string= splitted[item_title] if splitted[item_title]!='' else splitted[item_title2]
    categories=''
    series=''
    for index in category_pathes_indexes:
        category_path='[ROOT]'+'|'
        splitted_inner_category_path=split_category_path(index)
        for category in splitted_inner_category_path:
            if 'Series' in category:
                splitted_category_name = category.split(' ')
                series=splitted_category_name[1]
        category_path=category_path+build_category_path(splitted_inner_category_path)
        #category_path=category_path+'#'
        categories=categories+category_path
    categories=categories.strip("\n")
    status = 'Enabled' if splitted[is_active]=='1' else 'Disabled'
    media_gallery = ''
    for index in images_indexes:
        media_gallery=media_gallery+splitted[index]+"#"
    color_string=''
    if '/' in splitted[color]:
        splitted_color = splitted[color].split('/')
        color_string = splitted_color[0]+'#'+splitted_color[1]
    else:
        color_string = splitted[color]
    media_gallery = media_gallery[:-1]
    brand = brands.get(splitted[brand_id],'');
    regular_name = series+' '+item_title_string+' '+splitted[color]+' '+splitted[finish]+' '+splitted[material]
    sample_name = series+' '+splitted[sample_item_title]+' '+splitted[color]+' '+splitted[finish]+' '+splitted[material]
    configurable_product_row=splitted[item_id]+"\t"+""+"\t"+"tile_amount_type"+"\t"+"Regular"+"\t"+"base"+"\t"+"configurable"+"\t"+splitted[list_price]+"\t"+splitted[cost_price]+"\t"+splitted[price]+"\t"+splitted[in_stock]+"\t"+"9999"+"\t"+status+"\t"+"Catalog, Search"+"\t"+"Default"+"\t"+"1"+"\t"+regular_name+"\t"+categories+"\t"+brand+"\t"+splitted[specifications]+"\t"+splitted[meta_title]+"\t"+splitted[description]+"\t"+color_string+"\t"+splitted[size]+"\t"+splitted[sheet_size]+"\t"+splitted[tiles_per_sheet]+"\t"+splitted[sold_by]+"\t"+splitted[size_dimensions]+"\t"+splitted[sheets_per_sf]+"\t"+splitted[large_image]+"\t"+splitted[large_image]+"\t"+splitted[large_image]+"\t"+media_gallery+"\t"+splitted[stock_text]+"\t"+splitted[weight]+"\t"+splitted[ship_days]+"\t"+splitted[material]+"\t"+splitted[finish]+"\t"+splitted[icon_frostresistant]+"\t"+splitted[icon_antislip]+"\t"+splitted[icon_outdoors]+"\t"+splitted[icon_pool]+"\t"+splitted[icon_recycled]+"\t"+splitted[icon_2]+"\t"+splitted[installation_instruction_id]+"\t"+splitted[sheets_per_case]+"\t"+splitted[order_by_num]+"\t"+splitted[sticky_note]+"\t"+splitted[meta_description]+"\t"+splitted[meta_keywords]
    product_row=            splitted[model_num]+"\t"+splitted[item_id]+"\t"+""+"\t"+"Regular"+"\t"+"base"+"\t"+"simple"+"\t"+splitted[list_price]+"\t"+splitted[cost_price]+"\t"+splitted[price]+"\t"+splitted[in_stock]+"\t"+"9999"+"\t"+status+"\t"+"Not Visible Individually"+"\t"+"Default"+"\t"+"1"+"\t"+regular_name+"\t"+categories+"\t"+brand+"\t"+splitted[specifications]+"\t"+splitted[meta_title]+"\t"+splitted[description]+"\t"+color_string+"\t"+splitted[size]+"\t"+splitted[sheet_size]+"\t"+splitted[tiles_per_sheet]+"\t"+splitted[sold_by]+"\t"+splitted[size_dimensions]+"\t"+splitted[sheets_per_sf]+"\t"+splitted[large_image]+"\t"+splitted[large_image]+"\t"+splitted[large_image]+"\t"+media_gallery+"\t"+splitted[stock_text]+"\t"+splitted[weight]+"\t"+splitted[ship_days]+"\t"+splitted[material]+"\t"+splitted[finish]+"\t"+splitted[icon_frostresistant]+"\t"+splitted[icon_antislip]+"\t"+splitted[icon_outdoors]+"\t"+splitted[icon_pool]+"\t"+splitted[icon_recycled]+"\t"+splitted[icon_2]+"\t"+splitted[installation_instruction_id]+"\t"+splitted[sheets_per_case]+"\t"+splitted[order_by_num]+"\t"+splitted[sticky_note]+"\t"+splitted[meta_description]+"\t"+splitted[meta_keywords]
    sample_row=             splitted[sample_sku]+"\t"+splitted[item_id]+"\t"+""+"\t"+"Sample"+"\t"+"base"+"\t"+"simple"+"\t"+splitted[list_price]+"\t"+splitted[cost_price]+"\t"+splitted[sample_price]+"\t"+splitted[sample_in_stock]+"\t"+"9999"+"\t"+status+"\t"+"Not Visible Individually"+"\t"+"Default"+"\t"+"1"+"\t"+sample_name+"\t"+categories+"\t"+brand+"\t"+splitted[specifications]+"\t"+splitted[meta_title]+"\t"+splitted[sample_description]+"\t"+color_string+"\t"+splitted[size]+"\t"+splitted[sheet_size]+"\t"+splitted[tiles_per_sheet]+"\t"+splitted[sold_by]+"\t"+splitted[size_dimensions]+"\t"+splitted[sheets_per_sf]+"\t"+splitted[sample_image_name]+"\t"+splitted[sample_image_name]+"\t"+splitted[sample_image_name]+"\t"+media_gallery+"\t"+splitted[sample_stock_text]+"\t"+splitted[weight]+"\t"+splitted[sample_ship_days]+"\t"+splitted[material]+"\t"+splitted[finish]+"\t"+splitted[icon_frostresistant]+"\t"+splitted[icon_antislip]+"\t"+splitted[icon_outdoors]+"\t"+splitted[icon_pool]+"\t"+splitted[icon_recycled]+"\t"+splitted[icon_2]+"\t"+splitted[installation_instruction_id]+"\t"+splitted[sheets_per_case]+"\t"+splitted[order_by_num]+"\t"+splitted[sticky_note]+"\t"+splitted[meta_description]+"\t"+splitted[meta_keywords]
    file_output.write(configurable_product_row+"\n")
    file_output.write(product_row+"\n")
    file_output.write(sample_row+"\n")
file_output.close()
file.close()