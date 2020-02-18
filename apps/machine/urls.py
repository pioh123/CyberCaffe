from django.urls import path
from . import views

urlpatterns = [
    path('list',views.ListMachine.as_view(), name='list_machine'),
    path('addMachine', views.AddMachine.as_view(), name='add_machine'),
    path('editMachine/<int:pk>', views.EditMachine.as_view(), name='edit_machine'),
    path('machineAPI',views.MachineListAPI.as_view(),name='machine_list_API'),
    path('listGame',views.ListGame.as_view(),name='list_game'),
    path('addGame',views.AddGames.as_view(),name='add_game'),
    path('editGame/<int:pk>', views.EditGame.as_view(), name='edit_game'),
    path('gameAPI',views.GameListAPI.as_view(),name='game_list_API'),
    
]