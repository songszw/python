import easygui as g
import sys
import os
#-----------------------------------------------------------------------
# create "settings", a persistent Settings object
# Note that the "filename" argument is required.
# The directory for the persistent file must already exist.
#-----------------------------------------------------------------------
settingsFilename = os.path.join("C:", "FishCApp", "settings.txt")  # Windows example
settings = Settings(settingsFilename)