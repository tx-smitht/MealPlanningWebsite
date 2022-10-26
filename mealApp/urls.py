from django.urls import path # specifies the ability to extract the path class from the django.urls module
from .views import indexPageView # identifies the name of the function found in the newapp views.py file

# this is kinda like the routes part of a node/express app. This is where I can say, for this specific app, what routes do I want to direct.
# it says, if this rout is chosen, run the function. As stated above, they are imported from views. 
urlpatterns = [
    path('',indexPageView, name='index'),
]