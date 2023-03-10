from flask import Flask
from flask import request
from flask_restful import Resource, Api
from flask import jsonify
import json

app = Flask(__name__)
api = Api(app)

list_developer = [
  {
  "id": 0,
  "name": "Carlinhos",
  "skills": ["Python", "JavaScript", "Html5", "Css", "GIT"]
 },
 {
  "id": 1,
   "name": "Clebes",
   "skills": ["Python","Django"]
 }
]
# devolve um desenvolvedor pelo id,  tabm altera e deleta um desenvolvedor
class Developer(Resource):
  def get(self, id):
    try:
     request =list_developer[id]
    except IndexError :
     request = {'status': 'ERRO', 'mensagem':f'Desenvolvedor de id {id}, não existe'}
    except Exception :
     request = {'status':'ERRO', 'mensagem':'Erro desconhecido, Procure o admnistrador da API'}
    return jsonify(request)
  
  def put(self, id):
   datas = json.loads(request.data)
   list_developer[id] = datas
   return datas

  def delete(self, id):
    list_developer.pop(id)
    return jsonify({"message":"deleted item"})
# Está class está relacionado com a leitura da lista de desenvolvedores
class Developer_data(Resource):
  def get(self):
    return list_developer
  # Esse módulo  adiciona os elementos dentro da lista
  def post(self):
    datas = json.loads(request.data)
    position = len(list_developer)
    datas['id'] = position
    list_developer.append(datas)
    return jsonify(list_developer[position])
  

api.add_resource(Developer, '/dev/<int:id>/')
api.add_resource(Developer_data, '/dev/')


if __name__ == '__main__':
  app.run()