import django_filters
from .models import DailyEntryModel




class DaulyEntryfilter(django_filters.FilterSet):
    date_start = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')
    date_end = django_filters.DateFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = DailyEntryModel
        fields = ['date_start', 'date_end']