from unittest.mock import Mock

from django.db.models.functions import Lower

from django_filters_addons.filters import OrderingFilter

__all__ = (
    'test_field_cases_on_ordering_filter',
)


def test_field_cases_on_ordering_filter():
    ordering_filter = OrderingFilter(
        fields={'username': 'account', 'first_name': 'first_name', 'last_name': 'last_name', 'email': 'email'},
        field_cases={'username': Lower, 'email': Lower},
    )
    queryset = Mock()
    ordering_filter.filter(queryset, ('account', '-account'))
    queryset.order_by.assert_called_once_with(Lower('username'), Lower('username').desc())
    queryset.reset_mock()
    ordering_filter.filter(queryset, ('first_name', '-first_name', 'last_name', '-last_name'))
    queryset.order_by.assert_called_once_with('first_name', '-first_name', 'last_name', '-last_name')
    queryset.reset_mock()
    ordering_filter.filter(queryset, ('email', '-email'))
    queryset.order_by.assert_called_once_with(Lower('email'), Lower('email').desc())
