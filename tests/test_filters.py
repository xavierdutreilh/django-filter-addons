from unittest.mock import Mock

from django.db.models.functions import Lower

from django_filters_addons.filters import OrderingFilter

__all__ = (
    'test_field_cases_on_ordering_filter',
)


def test_field_cases_on_ordering_filter():
    ordering_filter = OrderingFilter(fields={'name': 'name', 'kind': 'kind'}, field_cases={'name': Lower})
    queryset = Mock()
    ordering_filter.filter(queryset, ('name', '-name', 'kind', '-kind'))
    queryset.order_by.assert_called_once_with(Lower('name'), Lower('name').desc(), 'kind', '-kind')
