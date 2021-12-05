import os

def main():
    i = 0
    path = "/home/sumant/Downloads/Work/Projects/Python Projects/Renaming bulk files/Renamed Files/"
    for fileName in os.listdir(path):
        renameFiles = "img" + str(i) + ".jpg"
        sourceFiles = path + fileName
        renameFiles = path + renameFiles
        os.rename(sourceFiles, renameFiles)
        i += 1

if  __name__ == "__main__":
    main()