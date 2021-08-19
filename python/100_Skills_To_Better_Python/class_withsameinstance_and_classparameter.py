class commonparams:
    name = "Person"
    def __init__(self,name):
        self.name = name

jon = commonparams("Jon")
print(jon.name)
love = commonparams("Love")
print(love.name)