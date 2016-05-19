
from system.core.model import Model

class WelcomeModel(Model):
    def __init__(self):
        super(WelcomeModel, self).__init__()

    def index(self):
        query = "SELECT * FROM notes"
        values = {}
        return self.db.query_db(query,values)

    def update(self,data,id):
        query = "UPDATE notes set title = :title, description = :description, updated_at = NOW() where id = :id"
        values = {
            "title": data['title'],
            "description": data['description'],
            "id": id
        }
        self.db.query_db(query,values)
    def delete(self,id):
        query = "DELETE from notes WHERE id = :id"
        values = {
            "id" : id
        }
        self.db.query_db(query,values)
    def create(self,data):
        query = "INSERT into notes (title,description, created_at, updated_at) VALUES (:title,:description,NOW(), NOW())"
        values = {
            "title":data['title'],
            "description":data['description']
        }
        self.db.query_db(query,values)
