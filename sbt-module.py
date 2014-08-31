import os

def ensureDir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
        print("created dir {}".format(dir))
    return;

def inputOrDefault(prompt, default):
    val = input("{} ({}): ".format(prompt, default))
    if val == "":
        return default;
    return val;

lines = []
def appendSbtKeyVal(key, defaulVal):
    lines.append("\n{} := \"{}\"\n".format(key, inputOrDefault(key, defaulVal)))
    return;

# grab all values needed for the build.sbt file
appendSbtKeyVal("name", "mymodule")
appendSbtKeyVal("version", "1.0-SNAPSHOT")
appendSbtKeyVal("scalaVersion", "2.11.2")

# find the file and folder paths needed
rootDir = inputOrDefault("root directory", ".")

# ensure file locations
ensureDir(rootDir)
ensureDir("{}/src/main/scala".format(rootDir))
ensureDir("{}/src/test/scala".format(rootDir))

# write the build.sbt file
buildFilePath = "{}/build.sbt".format(rootDir)
target = open(buildFilePath, 'w')
print("wrote...:")
for l in lines:
    target.write(l)
    print(l, end="")
target.close()
print("\n...to file {}".format(buildFilePath))






