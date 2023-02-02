from django.urls import path, include
from . import views

app_name = 'content'

urlpatterns = [
    path('',views.IndexView, name='coursepage_overview_url'),
    path('Domain/<int:domain_id>/',views.DomainView,name='Domain_url'),
    path('sources/',views.SourceView,name='source_url')
]