class Register:
    def __init__(self, initial_value=0, bits=8):
        self.value = 0
        self.mask = 0
        for i in bits:
            self.mask = (self.mask << 1) | 1
        self.set(initial_value)

        
    def set(self, newval):
        self.value = newval & self.mask
    
    def get(self):
        return self.value


class Flags(dict):
    def __init__(self, **kwargs):
        super.__init__()
        for key in kwargs.keys():
            self[key] = kwargs[key]
