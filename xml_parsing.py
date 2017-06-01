#!/usr/bin/python3

import xml.etree.ElementTree as etree

root = etree.parse('./Data/weatherDaily').getroot()  # gets the local XML file
# and it's root for parsing

i = 0

dataFile = open('./Data/Weather-Daily_Parsed.json', 'w')

for child in root:  # loop for going through the proper nested lists in the
    # XML and writes them to a local file
    dataFile.write(
        '\n{"Time" : "%s", ' % root[i][0][1].text +
        '"Type" : "%s" , ' % root[i][0][2].text +
        '"Value": "%s"}\n\n' % root[i][0][3].text)  # extremely shitty format
    #  conversion
    i += 1

dataFile.close()

# TODO: Better json convert
