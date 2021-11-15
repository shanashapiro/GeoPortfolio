# Task 3

import arcpy, sys, os 

# set the environment 
arcpy.env.workspace = "V:\\ENV859_PS4\\Data" 
arcpy.env.overwriteOutput = True 

#input counties as variable
counties = 'V:\\ENV859_PS4\\Data\\TriCounties.shp'
excellent = 'V:\\ENV859_PS4\\Data\\BMR_excellent.shp'

#check product 
if arcpy.CheckProduct("ArcInfo") == "Available": 
    arcpy.Split_analysis(excellent,counties,"CO_NAME","V:\\ENV859_PS4\\Scratch")
else: 
    msg = "ArcGIS for Desktop Advanced license not available" 
    print(msg)
    sys.exit(msg)
    
bmr = arcpy.ListFeatureClasses('BMR*')

for quality in bmr: 
    folders = arcpy.management.CreateFolder("V:\\ENV859_PS4\\Scratch", quality[:-4])
    arcpy.Split_analysis(quality,counties,"CO_NAME",folders)


