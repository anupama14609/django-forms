from django.urls import path
from .views import home, CrispyFormHome,DefaultFormHome, TweakFormHome

urlpatterns = [ 
    path('', home, name='home'),
    path('crispyform-home', CrispyFormHome, name='crispyform-home'),
    path('tweakform-home', TweakFormHome, name='tweakform-home'),
    path('defaultform-home', DefaultFormHome, name='defaultform-home'),
    
]

