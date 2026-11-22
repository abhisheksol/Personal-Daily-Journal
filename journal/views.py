from symtable import Class

from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, filters

from journal.models import DailyEntryModel
from journal.serializer import DailyEntrySerializer
from journal.utils.paginated import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend



class DailyEntryCreateView(
    # generics.CreateAPIView,
    # generics.ListAPIView
    generics.ListCreateAPIView
    ):
    queryset = DailyEntryModel.objects.all()
    serializer_class = DailyEntrySerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination

    # filter search
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        ]
    search_fields = ['date', 'went_well', 'best_moment', 'learned_today', 'went_bad', 'improve_tomorrow', 'mood']

    # data range filter 


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
    
    