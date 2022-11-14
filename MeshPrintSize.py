# --------------------------------------------------------------------------------
# Original Version from https://gist.github.com/frankbags
# https://gist.github.com/frankbags/c85d37d9faff7bce67b6d18ec4e716ff
# 
# Modified version from https://github.com/kmarty 
# https://github.com/kmarty/klipper_config_km_addons/blob/master/bed_mesh_calibrate/MeshPrintSize.py
#
# Copied straight from HelgeKeck
# https://github.com/HelgeKeck/pam/blob/main/cura/MeshPrintSize.py
#
# thank you frankbags and kmarty!
# --------------------------------------------------------------------------------

import re #To perform the search and replace.

from ..Script import Script

class MeshPrintSize(Script):

    def getSettingDataString(self):
        return """{
            "name": "Mesh Print Size",
            "key": "MeshPrintSize",
            "metadata": {},
            "version": 2,
            "settings":{}
        }"""

    def execute(self, data):
        minMaxXY = {'MINX':0,'MINY':0,'MAXX':0,'MAXY':0}
        re_pattern = re.compile(r'%(' + r'|'.join(minMaxXY.keys()) + r')%')
        minmax_counter = len(minMaxXY)

        for i in range(len(data)):
            # in Cura "layer' != "line" :-(
            for k,v in minMaxXY.items():
                if minmax_counter:
                    result = re.search(r';' + k + r':\s*(\d*\.\d+|\d+)', data[i])
                    if result:
                        minMaxXY[k] = result.group(1)
                        minmax_counter -= 1
                else:
                    if re_pattern.search(data[i]):
                        data[i] = re.sub(r'%' + k + r'%', v, data[i])

        return data