import os
import shutil
import time

def main():

    path = input("Enter the name of the directory to be sorted: ")
    days = 30
    seconds = time.time() - (days*24*60*60)
    deletedFoldersCount = 0
    deletedFilesCount = 0

    if(os.path.exists(path)):
        for rootFolder, folders, files in os.walk(path):
            #comparing the days
            if seconds >= getFileOrFolderAge(rootFolder):
                #removing the folders
                removeFolder(rootFolder)
                deletedFoldersCount = deletedFoldersCount + 1
                break
            else:
                #checking folder from root folder
                for folder in folders:
                    #folder path
                    folderPath = os.path.join(rootFolder, folder)

                    #comparing with the days
                    if seconds >= getFileOrFolderAge(folderPath):
                        removeFolder(folderPath)
                        deletedFoldersCount = deletedFoldersCount + 1

                #checking current directory files
                for file in files:
                    filePath = os.path.join(rootFolder, file)

                    if seconds >= getFileOrFolderAge(filePath):
                        removeFile(filePath)
                        deletedFilesCount = deletedFilesCount + 1

                    else:
                        #if path is not a directory
                        #comparing with the days
                        if seconds >= getFileOrFolderAge(path):
                            removeFile(path)
                            deletedFilesCount = deletedFilesCount + 1
        
    else:
        #file or folder is not found
        print(f"{path} is not found")
    print(f"Total folders deleted: {deletedFoldersCount}")
    print(f"Total filed deleted: {deletedFilesCount}")


            
        
def removeFolder(path):
    if(not shutil.rmtree(path)):
        print(f"{path} has been removed successfully")
    else:
        print("Unable to delete the path"+ path)
    
def removeFile(path):
    if(not os.remove(path)):
        print(f"{path} has been removed successfully")
    else:
        print("Unable to delete the path", path)

def getFileOrFolderAge(path):
    ctime = os.stat(path).st_ctime
    return ctime

if __name__ == '__main__':
    main()
