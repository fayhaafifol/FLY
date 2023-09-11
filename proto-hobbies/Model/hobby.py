from Model.proton import Proton

class Hobby:
    def _init_(self,title: str,imagePath: str):
        self.title = title
        self.imagePath = imagePath
        self.hobbyProtons = []

    def addProton(self,proton: Proton):
        
        self.hobbyProtons.append(proton)
        

    def addPhoto(self,imagepath):

        imagepath="hi"
       

    def removeProton(self,protonName : str):
        
        for l in self.hobbyProtons:

            if l.name == protonName:

                self.hobbyProtons.remove(l)


