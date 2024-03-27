from django_filters import rest_framework as filters
from .models import Pressure_Reading


class PressureReadingFilterSet(filters.FilterSet):
    # from_date = filters.DateTimeFilter(field_name="date_time", lookup_expr="gte")
    # to_date = filters.DateTimeFilter(field_name="date_time", lookup_expr="lt")
    # label = filters.CharFilter()
    # date_time=filters.
    # we will use just variables in the top in URL
    # datetime = filters.DateTimeFromToRangeFilter("date_time")
    # with after and before
    # we put variable_after or variable_before
    # here variable name is datetime wich eill connect to Date_Time field in database

    class Meta:
        model = Pressure_Reading
        fields = {
            "label": ["exact"],
            "date_time": ['lt', 'lte'],
        }

    # if we use fields in class meta with expr , we put field_name__expr in the URL
