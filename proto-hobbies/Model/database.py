from Model.hobby import Hobby
from Model.proton import Proton

class Database:

    def _init_(self):
        self.protons = []
        self.hobbies = []


    def addHobby(self,hobby: Hobby):

        self.hobbies.append(hobby)
        

    def registerProton(self,proton: Proton):
        
        self.protons.append(proton)
        

    def findHobby(self,hobbyTitle: str):
        
          for h in self.protons:

            if h.title == hobbyTitle:

                return h #in the view write (the name already exists)
            
            return False
            
    def findProton(self,protonName: str):

        for p in self.protons:

            if p.name == protonName:

                return p #in the view write (the name already exists)
            
        return False
        

    def deleteProton(self,protonName: str):

        for g in self.protons:

            if g.name == protonName:

                self.protons.remove(g)
            
        
    def deleteHobby(self,hobbyName: str):

        for i in self.protons:

            if i.title == hobbyName:

                self.protons.remove(i)
