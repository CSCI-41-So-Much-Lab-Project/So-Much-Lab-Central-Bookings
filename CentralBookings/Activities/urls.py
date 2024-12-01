from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("activities/", views.activities_list_view, name="activity list"),
    path("organizer/", views.organizer_info_list_view, name="organizer_info"),
    path("participant-booking/", views.participant_activity_booking_list_view, name="participant_booking"),
]