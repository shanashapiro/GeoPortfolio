#%% Task 1
#1a. Creating the initial buffer script 
import arcpy

streams = "V:\\ENV859_PS4\\Data\\streams.shp"
outFeatureClass = "V:\\ENV859_PS4\\Scratch\\StrmBuff1km.shp"
buffDist = '1000 meters'

arcpy.Buffer_analysis(streams, outFeatureClass, buffDist, "", "", dissolve_option = "ALL")

print(arcpy.GetMessages())

