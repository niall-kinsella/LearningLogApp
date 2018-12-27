"""Defines URL patterns for Learning_Logs"""


from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # home page
    path('', views.index, name='index'),

    # topics page
    path('topics/', views.topics, name='topics'),

    # individual topics pages
    path('topics/(?<topic_id>\d+', views.topic, name='topic'),

    # add new topic page
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page for adding entries to topics
    path('new_entry/(<int:topic_id>)', views.new_entry, name='new_entry'),

    # Page for editing an entry
    path('edit_entry/(<int:entry_id>)', views.edit_entry, name='edit_entry')
]
