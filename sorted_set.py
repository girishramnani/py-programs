__author__ = 'girish'
class sorted_set:
    def __init__(self,items=[]):
        self._collection = sorted(set(items))
    def __contains__(self, item):
        return item in self._collection
    def __len__(self):
        return len(self._collection)
    def __getitem__(self, item):
        return self._collection[item]
