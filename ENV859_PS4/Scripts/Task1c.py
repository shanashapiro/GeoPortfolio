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
