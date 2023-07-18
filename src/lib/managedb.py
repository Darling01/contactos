import pathlib
import json

class ManageDb:
    __address_file = "{0}/src/db/dbContacts.json".format(pathlib.Path().absolute())

    def read_contacts(self):
        print(self.__address_file)
        #with open("/db/dbContacts.json", "r") as data:
        #with open("src/db/dbContacts.json", "r") as data:
        with open(self.__address_file, "r") as data:
            return json.loads(data.read())
        #print(data.read())
        
    def write_contacts(self, new_data):
        with open(self.__address_file, "w")  as data:
            data.write(json.dumps(new_data))
        
#md = ManageDb()
#print(md.read_contacts())