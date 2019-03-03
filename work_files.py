import json
class shig():
    def read_file(self, name):
        file = open(name, mode='r')
        if '.json' in name:
            data = json.load(file)
        else:
            data = file.read()
        file.close()        
        return data

    def write_file(self, name, data):
        file = open(name, mode='w')
        if '.json' in name:
            json.dump(data,file)
        else:
            file.write(str(data))
        file.close()
    
