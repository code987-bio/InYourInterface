class Teams:
    def __init__(self, members):
        self.__myTeam = members
        self.__index = 0
        
    
    def __len__(self):
        return len(self.__myTeam)

    def __contains__(self, param):
      """Expect string value as param"""
      return True if param in self.__myTeam else False
    
    #Not sure what this does
    def __iter__(self):
      return self
    
    def __next__(self):
      #if index is out of range of myTeam stop iteration
      if(self.__index >= len(self.__myTeam)):
          raise StopIteration
          
      #Else return the next element
      element = self.__myTeam[self.__index]
      self.__index += 1
      return element

def main():
    classmates = Teams(['John','Steve','Tim'])
    print(len(classmates))
    
    #Here is called __contains__ method
    print("Tim" in classmates and "Sam" in classmates)

    print("---------------")
    for person in classmates:
      print(person)
    
main()
