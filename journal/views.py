from symtable import Class

from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions

from journal.models import DailyEntryModel
from journal.serializer import DailyEntrySerializer
from journal.utils.paginated import CustomPagination



class DailyEntryCreateView(
    # generics.CreateAPIView,
    # generics.ListAPIView
    generics.ListCreateAPIView
    ):
    queryset = DailyEntryModel.objects.all()
    serializer_class = DailyEntrySerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return DailyEntryModel.objects.filter(user=self.request.user)


# only delte and update
class DailyEntryupdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DailyEntryModel.objects.all()
    serializer_class = DailyEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return DailyEntryModel.objects.filter(user=self.request.user)
    
    