from level import *
import sys, importlib

players = []
for index in range(1, len(sys.argv)):
    module = importlib.import_module("AI." + sys.argv[index])
    AI = module.AntiyoyAI(index)
    
    print("Adding '" + AI.getName() + "'")
    players.append(AI)
   
level = Level.fromFile("levels/test_level.txt")
print(level.toString())