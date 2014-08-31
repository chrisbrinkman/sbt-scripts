import os
from sys import argv

defaultScalaVer = "2.11.2"
defaultVer = "1.0-SNAPSHOT"
defaultDir = "."

scalaVer = raw_input("scala version (" + defaultScalaVer + "): ")
name     = raw_input("project name: ")
ver      = raw_input("project version (" + defaultVer + "): ")
rootDir  = raw_input("project dir (" + defaultDir + "): ")

if scalaVer == "": scalaVer = defaultScalaVer
if ver == "": ver = defaultVer
if rootDir == "": rootDir  = "."

if not os.path.exists(rootDir):
    os.makedirs(rootDir)

target = open(rootDir + "/build.sbt", 'w')
target.write("name := \"" + name + "\"")
target.write("\n")
target.write("\nversion := \"" + ver + "\"")
target.write("\n")
target.write("\nscalaVersion := \"" + scalaVer + "\"")
target.write("\n")
target.close()

print "wrote " + rootDir + "/build.sbt"
