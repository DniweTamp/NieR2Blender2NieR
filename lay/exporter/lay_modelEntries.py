import binascii

from ...utils.ioUtils import write_char
from ...utils.util import *


class ModelEntries:
    def __init__(self):
        self.modelEntries = []
        for obj in bpy.data.collections['lay_layAssets'].all_objects:
            if len(obj.name) > 32:
                print("[!] Asset name too long (must be at most 32 characters):", obj.name)
                continue
            modelName = obj.name.split("_")[0]
            if modelName not in self.modelEntries:
                self.modelEntries.append(modelName)
        
        self.structSize = len(self.modelEntries) * 4

def write_modelEntries(lay_file, data):
    lay_file.seek(data.offsetModelEntries)
    for modelEntry in data.modelEntries.modelEntries:
        write_char(lay_file, modelEntry[0])
        write_char(lay_file, modelEntry[1])
        lay_file.write(binascii.unhexlify(modelEntry[4:]))
        lay_file.write(binascii.unhexlify(modelEntry[2:4]))
    print("[>] numModelEntries:", len(data.modelEntries.modelEntries))
        
