import sys
import json

class NotFound(Exception): pass

class IO:
    def __init__(self):
        self.file = sys.path[0] + '\data.json'

    def read_file(self, data_type=None, get_data=False):
        with open(self.file, encoding="utf-8") as json_file:
            data = json.load(json_file)
            if get_data:
                return data
            elif data_type == None:
                return
            try:
                return data[data_type]
            except KeyError:
                print("Data name not defined")
                return
            
    def check_fields(self, new_data, existing_data):
        for key in existing_data:
            if key not in new_data:
                return False
        return True

    def append_to_file(self, data_type, new_data):
        data = self.read_file(get_data=True)
        try:
            if type(new_data) != dict:
                raise TypeError()
            else:
                data[data_type]
                if self.check_fields(new_data, data[data_type][0]):
                    data[data_type].append(new_data)
                else:
                    raise TypeError()
        except KeyError:
            print("Data name not defined")
            return
        except TypeError:
            print("Not correct data format")
            return

        with open(self.file, 'w', encoding="utf-8") as json_file:
            json.dump(data, json_file)
            

    def remove_from_file(self, data_type, name):
        data = self.read_file(get_data=True)
        try:
            if type(name) != str:
                raise TypeError()
            else:
                data[data_type]
                removed = False
                for i in data[data_type]:
                    if i["name"] == name:
                        data[data_type].remove(i)
                        removed = True
                if not removed:
                    raise NotFound()
        except KeyError:
            print("Data name not defined")
            return
        except TypeError:
            print("Not correct data format")
            return
        except NotFound:
            print("Data does not exist")
            return
        
        with open(self.file, 'w', encoding="utf-8") as json_file:
            json.dump(data, json_file)




io = IO()
# io.append_to_file("members", {
# 'name': "Daniel",
#     'phone': "8959337",
#     'email': "danielc19@ru.is",
#     'year_of_birth': 1995
# })

io.remove_from_file("members", "lol")