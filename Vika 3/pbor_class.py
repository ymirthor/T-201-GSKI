class pbor_class:

    def __init__(self, inst_var):
        self.inst_var = inst_var

    def reassign(self):
        print("inst_var before reasign: " + str(self.inst_var))
        self.inst_var = [0,1]
        print("inst_var after reasign: " + str(self.inst_var))

    def change(self):
        print("inst_var before change: " + str(self.inst_var))
        self.inst_var.append(1)
        print("inst_var after change: " + str(self.inst_var))