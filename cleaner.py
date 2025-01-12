import os, glob, shutil

class Cleaner:
    path = ""
    targets = {}
    folders = []
    extensions = []
    def __init__(self,path,folders,extensions):
        self.path = path
        self.folders = folders
        self.extensions = extensions
        self.targets = dict(zip(folders,extensions))


    def magic(self):
        for folder,extension in self.targets.items():
            Cleaner.single(self.path,folder,extension)


    def single(aPath,aFolder,aExtension):
        complete = os.path.join(aPath,aFolder)
        if not os.path.isdir(complete):
            print("Creating folder")
            os.mkdir(complete)
        files = glob.glob(f"{aPath}/{aExtension}")
        for file in files:
            shutil.move(file,complete)


#clean = Cleaner("C:/Users/Muhammad/Desktop",["Text","Images"],["*.txt","*.png"])
#clean.magic()



    





# path = "C:/Users/Muhammad/Desktop"
        # textFolder = "Text_Docs"
        # complete = os.path.join(path,textFolder)
        # if not os.path.isdir(complete):
        #     print("Creating text document path")
        #     os.mkdir(os.path.join(path, textFolder))
        
        # extension = "*.txt"
        # textFiles = glob.glob(f"{path}/*.txt")
        # for file in textFiles:
        #     shutil.move(file,complete)
