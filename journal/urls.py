from django.urls import path

from journal.views import DailyEntryCreateView, DailyEntryupdateDeleteView


urlpatterns = [
    path('daily-entries/', DailyEntryCreateView.as_view(), name='user-create'),
    path('daily-entries/<int:pk>/', DailyEntryupdateDeleteView.as_view(), name='entry-update-delete'),
]