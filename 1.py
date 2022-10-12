# as I recall, in original example the final ":" after class name was absent ))

# create List of Person instances

class Person:
  def __init__(self, name,nick):
    self.name = name
    self.nick = nick

data = [
  {'name':'Ivan1','nick':'Ivanych1'},
  {'name':'Ivan2','nick':'Ivanych2'},
  {'name':'Ivan3','nick':'Ivanych3'}]

list_of_Persons = []

# main
for i in data: list_of_Persons.append(Person(**i))

# print result
for pers in list_of_Persons:
  print(pers.name, pers.nick)