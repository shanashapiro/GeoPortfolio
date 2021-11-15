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
    
