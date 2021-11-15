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
