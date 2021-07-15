from django.urls import path

from .views import signup, flux, follow_users, create_ticket, create_critics, answer_to_critic, show_own_critics, \
    edit_own_critics, edit_own_ticket, index, logout_user, del_ticket, del_review

urlpatterns = [
    path('', index, name="home"),
    path('home/', index, name="home"),
    path('signup/', signup, name="signup"),
    path('logout/', logout_user, name="logout"),
    path('flux/', flux, name="flux"),
    path('follow/', follow_users, name="follow"),
    path('new-ticket/', create_ticket, name="new-ticket"),
    path('new-critic/', create_critics, name="new-critic"),
    path('answer-critic/', answer_to_critic, name="answer-critic"),
    path('show-critics/', show_own_critics, name="show-critics"),
    path('edit-critics/', edit_own_critics, name="edit-critics"),
    path('edit-ticket/<int:ticket_id>/', edit_own_ticket, name="edit-ticket"),
    path('delticket/<int:ticket_id>/', del_ticket, name="delticket"),
    path('delreview/<int:review_id>/', del_review, name="delreview"),
]