# Task 1d. Adding auto-generated output names 
import arcpy

arcpy.env.workspace = "V:\\ENV859_PS4\\Data" #sets the environment setting
arcpy.env.overwriteOutput = True

streams = "streams.shp"
buffDist = [100, 200, 300, 400, 500]
for dist in buffDist:
    outFeatureClass = f"V:\\ENV859_PS4\\Scratch\\buff_{dist}m.shp"
    arcpy.Buffer_analysis(streams, outFeatureClass, dist)


