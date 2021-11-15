# Task 1d. Adding auto-generated output names 
import arcpy,sys 

arcpy.env.workspace = "V:\\ENV859_PS4\\Data" #sets the environment setting
arcpy.env.overwriteOutput = True

streams = "streams.shp"
buffDist = sys.argv[1]
outFeatureClass = f"V:\\ENV859_PS4\\Scratch\\buff_{sys.argv[1]}m.shp"

arcpy.Buffer_analysis(streams, outFeatureClass, buffDist)

