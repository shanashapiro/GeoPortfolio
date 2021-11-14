#The following script fetches data, uses geoprocessing tools in Python, and utilizes ArcPy functions
#Shana Shapiro
#Fall 2021 

#%% Task 1
#1a. Creating the initial buffer script 
import arcpy

streams = "V:\\ENV859_PS4\\Data\\streams.shp"
outFeatureClass = "V:\\ENV859_PS4\\Scratch\\StrmBuff1km.shp"
buffDist = '1000 meters'

arcpy.Buffer_analysis(streams, outFeatureClass, buffDist, "", "", dissolve_option = "ALL")

print(arcpy.GetMessages())

# Task 1b: Setting environment values in the script
import arcpy

arcpy.env.workspace = "V:\\ENV859_PS4\\Data" #sets the environment setting
arcpy.env.overwriteOutput = True

streams = "streams.shp"
outFeatureClass = "V:\\ENV859_PS4\\Scratch\\StrmBuff1km.shp"
where_clause = '"CLASS" = \'4\''

buffDist = '1000 meters'

arcpy.Buffer_analysis(streams, "V:\\ENV859_PS4\\Scratch\\StrmBuff1km.shp", buffDist)

print(arcpy.GetMessages())

# Task 1c: Enabling user input 
import arcpy,sys

arcpy.env.workspace = "V:\\ENV859_PS4\\Data" #sets the environment setting
arcpy.env.overwriteOutput = True

# static input
streams = "streams.shp"
# user input variables and no need to do error trapping 
# assume output filename supplied by user will include the full file path “V:\ENV859_PS4\Scratch\StrmBuff1km.shp”
# run configuration per file and enter inputs via the Command line options: line 
outputFeatureClass = sys.argv[1]
buffDist = f"{sys.argv[2]} meters"

arcpy.Buffer_analysis(streams, outputFeatureClass, buffDist)

# Task 1d. Adding auto-generated output names 
import arcpy,sys 

arcpy.env.workspace = "V:\\ENV859_PS4\\Data" #sets the environment setting
arcpy.env.overwriteOutput = True

streams = "streams.shp"
buffDist = sys.argv[1]
outFeatureClass = f"V:\\ENV859_PS4\\Scratch\\buff_{sys.argv[1]}m.shp"

arcpy.Buffer_analysis(streams, outFeatureClass, buffDist)

# Task 2

import arcpy 

# set the environment 
arcpy.env.workspace = "V:/ENV859_PS4/Data" 
arcpy.env.overwriteOutput = True 

roads = r"V:\\ENV859_PS4\\Data\\Roads.shp"

roads_ct = "0;201;203"
road_type = roads_ct.split(";")

for rt in road_type:
    arcpy.analysis.Select(roads, f"V:\ENV859_PS4\Scratch\Roads_{rt}.shp", f"ROAD_TYPE = {rt}")

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


# Task 4 

import arcpy

# set the environment 
arcpy.env.workspace = "V:/ENV859_PS4/Data" 
arcpy.env.overwriteOutput = True 

#user specified datasets
inFC = arcpy.GetParameterAsText(0)
#outFC = arcpy.GetParameterAsText(1)

# Describe a feature class using arcpy.Describe
desc = arcpy.Describe(inFC)
#indicate the dataset's catalogPath property 
arcpy.AddMessage("{}".format(inFC))

#examine the extent properties
xmin = desc.extent.XMin
xmax = desc.extent.XMax
ymin = desc.extent.YMin
ymax = desc.extent.YMax
arcpy.AddMessage(f"XMin: {xmin} \nYMin: {ymin} \nXMax: {xmax} \nYMax: {ymax}")


#Check dataset's datasetType and execute based on what it is 
if desc.datasetType == "FeatureClass":
    arcpy.AddWarning("Shapetype: " + desc.shapeType)
if desc.datasetType == "RasterDataset":
    rowcount =  arcpy.management.GetRasterProperties(inFC, "ROWCOUNT")
    colcount = arcpy.management.GetRasterProperties(inFC, "COLUMNCOUNT")
    arcpy.AddWarning(f"Format: {desc.format} \n# of rows: {rowcount} \n# of columns: {colcount}")
else:
    arcpy.AddMessage(desc.datasetType)

#Task 5

import arcpy
# set the environment 
arcpy.env.workspace = "V:/ENV859_PS4/Data" 
arcpy.env.overwriteOutput = True 

#user specified datasets
inFC = arcpy.GetParameterAsText(0)
userField = arcpy.GetParameterAsText(1)

point = arcpy.Point(587000,265000)

cur = arcpy.da.SearchCursor(inFC,["SHAPE@",userField])
for row in cur:
    recShape = row[0]
    if point.within(recShape):
        arcpy.AddMessage(f"County containing point: {row[1]}")


