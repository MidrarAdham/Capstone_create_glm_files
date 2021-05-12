import os
import re

source_file = r".\feeder_configuration.glm"

# open our original glm file
file = open(source_file, "r")
contents = file.read()

# create a match pattern for the resistance in triplex_line_configuration
r = re.compile("diameter \d*\.\d*")

# run gridlabd 8 times using increments of 1/7 and modifying the triplex_line_configuration resistance
for i in range(0, 7):
    diameter = 0.368 + i * 1
    newContent = r.sub(f"diameter {diameter}", contents, 1)
    newFile = open(r".\test_feeder_configuration.glm", "w+")
    newFile.truncate()
    newFile.write(newContent)
    newFile.flush()
    newFile.close()
    # run gridlab on the new file
    os.system(fr"gridlabd .\test_feeder_configuration.glm")