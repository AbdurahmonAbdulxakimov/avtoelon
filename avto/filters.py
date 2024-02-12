from django_filters import FilterSet, AllValuesFilter
from django_filters import DateTimeFilter, NumberFilter

from avto.models import Post


class RobotFilter(FilterSet):
    # from_manufacturing_date = DateTimeFilter(
    #     field_name="manufacturing_date", lookup_expr="gte"
    # )
    # robotcategory_name = AllValuesFilter(field_name="robot_category__name")

    min_price = NumberFilter(field_name="price", lookup_expr="gte")
    max_price = NumberFilter(field_name="price", lookup_expr="lte")

    min_year = NumberFilter(field_name="json.year", lookup_expr="gte")
    max_year = NumberFilter(field_name="json.year", lookup_expr="lte")

    class Meta:
        model = Post
        fields = (
            "subcategory",
            "region",
            "model",
            "salon",
            "min_price",
            "max_price",
            "has_trade",
            "has_rent",
            "min_year",
            "max_year",
        )
