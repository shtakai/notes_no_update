"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes


routes['default_controller'] = 'Welcome'
routes['GET']['/notes'] = "Welcome#notes_index"
routes['POST']['/notes'] = "Welcome#create"
routes['GET']['/notes/new'] = "Welcome#new"
routes['POST']['/notes/delete/<int:id>'] = "Welcome#delete"
routes['POST']['/notes/update/<int:id>'] = "Welcome#update"

"""
    routes['GET']['/users'] = 'users#index'
    routes['GET']['/users/new'] = 'users#new'
    routes['POST']['/users'] = 'users#create'
    routes['GET']['/users/<int:id>'] = 'users#show'
    routes['GET']['/users/<int:id>/edit' = 'users#edit'
    routes['PATCH']['/users/<int:id>'] = 'users#update'
    routes['DELETE']['/users/<int:id>'] = 'users#destroy'
"""
