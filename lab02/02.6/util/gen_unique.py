import random

class GenerateUnique:
    def generateUniqueId(dep:str)-> str:
        return dep + str(random.randrange(1, 1000))