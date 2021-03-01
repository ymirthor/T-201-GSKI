import sys

class IO_API:
    def read_file(self, file_name):
        ret_list = list()
        with open(sys.path[0] + "\\data\\" + file_name, "r", encoding="utf-8") as fileobject:
            for line in fileobject.readlines():
                try:
                    # convert to keyword
                    key, value = line.strip().split(",")
                    item = {key: int(value)}
                    ret_list.append(item)
                except:
                    ret_list.append(line.strip())
        return ret_list
    
    def write_file(self, alist, file_name):
        with open(sys.path[0] + "\\data\\" + file_name, "w+", encoding="utf-8") as fileobject:
            for word in alist:
                try:
                    name, score = list(word.items())[0]
                    word = "{},{}".format(name, score)
                except:
                    None
                fileobject.write(word + "\n")
       