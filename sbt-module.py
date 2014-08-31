import os
from sys import argv

scalaVer = raw_input("scala version (2.11.2): ")
name = raw_input("module name: ")
ver = raw_input("module version (1.0-SNAPSHOT): ")
rootDir = raw_input("root dir (.): ")

if scalaVer == "": scalaVer = "2.11.2"
if ver == "": ver = "1.0-SNAPSHOT"
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

mainSrc = rootDir + "/src/main/scala"
if not os.path.exists(mainSrc): os.makedirs(mainSrc)

testSrc = rootDir + "/src/test/scala"
if not os.path.exists(testSrc): os.makedirs(testSrc)

print "wrote " + rootDir + "/build.sbt"
