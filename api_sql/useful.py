from models import People, Users
#Inserir os dados na tabela
def insert_person():
  person = People(name="Pedro", age="35")
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

def insert_user(login, password):
  user = Users(login=login, password=password)
  user.save()

def query_list_user():
  user = Users.query.all()
  print(user)



if __name__ =="__main__":
  # insert_person()
  # query_person()
  # change_person()
  insert_user('paulo', '123')
  insert_user('arantes', '4321')
  query_list_user()

