from flask import Flask
from flask_restful import Resource, Api, request
from models import People, Activities

app = Flask(__name__)
api = Api(app)

class Person(Resource):
  def get (self, name):
    person = People.query.filter_by(name=name).first()
    try:
      response = {
          'name': person.name,
          'age': person.age,
          'id': person.id
      }
    except AttributeError:
        response = {
          'status': 'error',
          'mensagem': 'Pessoa não encontrada'
        }
    return response
  
  def put(self, name):
    person = People.query.filter_by(name=name).first()
    datas = request.json
    if 'name' in datas:
      person.name = datas['name']
    if 'idade' in datas:
      person.age = datas['age']

    person.save()
    response = {
      'id':person.id,
      'name': person.name,
      'age': person.age
    }
    return response
  
  def delete(self, name):
    person = People.query.filter_by(name=name).first()
    message = f'Pessoa {person} excluida com sucesso'
    person.delete()
    return {'status': 'Sucesso', 'message': message }

class List_people(Resource):
  def get (self):
     people = People.query.all()
     response = [{'id':i.id, 'name':i.name, 'age':i.age }for i in people]
     return response

  def post(self):
    datas = request.json
    person = People(name=datas['name'], age = datas['age'])
    person.save()
    response = {
      'id':person.id,
      'name':person.name,
      'age':person.age
    } 
    return response

class List_activities(Resource):
  def get(self):
    activities = Activities.query.all()
    response = [{'id': i.id, 'name':i.name, 'person':i.person.name } for i in activities]
    return response
  def post(self):
    datas = request.json
    person = People.query.filter_by(name=datas['person']).first()
    activities = Activities(name=datas['name'], person=person)
    activities.save()
    response = {
      'person': activities.person.name,
      'name': activities.name,
      'id': activities.id
    }
    return response
    
api.add_resource(Person, '/person/<string:name>/')
api.add_resource(List_people, '/person/')
api.add_resource(List_activities, '/activities/')
  
if __name__ == '__main__':
  app.run(debug=True)  