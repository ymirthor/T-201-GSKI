from pbor_class import *

def reassign(param):
    param = [0,1]
    print("Param: " + str(param))

def change(param):
    param.append(1)
    print("param: " + str(param))

var = [0]

class_inst = pbor_class(var)
print("var before: " + str(var))
class_inst.change()
print("var after: " + str(var))
#print("var2: " + str(var2))
#print("var: " + str(var))