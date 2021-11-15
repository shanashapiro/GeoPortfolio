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