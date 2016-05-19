"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        self.load_model('WelcomeModel')
        self.db = self._app.db

    def index(self):
        return self.load_view('index.html')

    def notes_index(self):
        notes = self.models['WelcomeModel'].index()
        return self.load_view('partials/_index.html', notes = notes)

    def new(self):
        return self.load_view('partials/_new.html')

    def create(self):
        self.models['WelcomeModel'].create(request.form)
        return redirect('/notes')

    def update(self,id):
        self.models['WelcomeModel'].update(request.form, id)
        pass

    def delete(self,id):
        self.models['WelcomeModel'].delete(id)
        return redirect('/notes')
