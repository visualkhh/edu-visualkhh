class MyHashMap:

    def __init__(self):
        self.d = dict()


    def put(self, key: int, value: int) -> None:
        self.d['key_'+str(key)] = value


    def get(self, key: int) -> int:
        if 'key_'+str(key) in self.d:
            return self.d['key_'+str(key)]
        else:
            return -1


    def remove(self, key: int) -> None:
        del self.d['key_'+str(key)]


if __name__ == '__main__':
    obj = MyHashMap()
    obj.put(1, 111)
    param_2 = obj.get(1)
    print(param_2)
    param_2 = obj.remove(1)
    print(param_2)
    param_2 = obj.get(1)
    print(param_2)



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
