class MyIterator:
    def __init__(self,start,end):
        self.current=start 
        self.end=end 
    def __iter__(self):
        return self 
    def  __next__(self):
        if self.current < self.end:
            value=self.current 
            self.current+=1
            return value 
        else:
            raise StopIteration
my_iter=MyIterator (1,7)
for num in my_iter:
    print(num)