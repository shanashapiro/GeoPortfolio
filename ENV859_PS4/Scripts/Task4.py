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
