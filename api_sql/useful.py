from models import People
#Inserir os dados na tabela
def insert_person():
  person = People(name="Paulo", age="25")
  print(person)
  person.save()
#Ver os dados ta tabela
def query_person():
  person = People.query.all()
  print(person)
# Atualizar os dados da tabela
def change_person():
  person = People.query.filter_by(name="Paulo").first()
  person.age = 23
  person.save()
#Exclui os dados  da tabela pessoa 
def delete_person():
  person = People.query.filter_by(name="Paulo").first()
  person.delete()


if __name__ =="__main__":
  # insert_person()
  delete_person()
  query_person()
  # change_person()

