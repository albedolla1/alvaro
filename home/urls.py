from django.urls import path, include 
from .views import home, sixA, sixB, sixC, sixE, AddSixA, AddSixB, AddSixC, AddSixE, EditSixA, EditSixB, EditSixC, EditSixE, DeleteSixA, DeleteSixB, DeleteSixC, DeleteSixE 
from .views import SignUpView

urlpatterns = [
    path('', home, name='home'),
    path('6a', sixA, name='sixA'),
    path('6b', sixB, name='sixB'),
    path('6c', sixC, name='sixC'),
    path('6e', sixE, name='sixE'),


    path('add/sixa', AddSixA.as_view(), name='addSixA'),
    path('add/sixb', AddSixB.as_view(), name='addSixB'),
    path('add/sixc', AddSixC.as_view(), name='addSixC'),
    path('add/sixe', AddSixE.as_view(), name='addSixE'),

    path('edit/sixa/<int:pk>', EditSixA.as_view(), name='editSixA'),
    path('edit/sixb/<int:pk>', EditSixB.as_view(), name='editSixB'),
    path('edit/sixc/<int:pk>', EditSixC.as_view(), name='editSixC'),
    path('edit/sixe/<int:pk>', EditSixE.as_view(), name='editSixE'),

    path('delete/sixa/<int:pk>', DeleteSixA.as_view(), name='deleteSixA'),
    path('delete/sixb/<int:pk>', DeleteSixB.as_view(), name='deleteSixB'),
    path('delete/sixc/<int:pk>', DeleteSixC.as_view(), name='deleteSixC'),
    path('delete/sixe/<int:pk>', DeleteSixE.as_view(), name='deleteSixE'),
    

    path('signup/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]