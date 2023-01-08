"""Custom filters."""

import django_filters
from django_filters import CharFilter

from reviews.models import Title


class TitleFilter(django_filters.FilterSet):
    """'Title' resource content display filter."""

    name = CharFilter(lookup_expr="icontains")
    category = CharFilter(field_name="category__slug")
    genre = CharFilter(field_name="genre__slug")

    class Meta:
        model = Title
        fields = ("name", "category", "genre", "year")
