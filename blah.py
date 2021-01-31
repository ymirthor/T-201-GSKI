class parent:
    def __init__(self):
        self._name = "Smith"

    @property
    def name(self):
        return self._name

class child(parent):
    def __init__(self, childname):
        super().__init__()
        self._childname = childname

    def getname(self):
        return "child : {} .. parent : {}".format(self._childname, super().name)

def main():
    Dad = parent()
    Son = child("jack")
    print(Son.getname())

if __name__ == "__main__":
    main()