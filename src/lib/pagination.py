from collections import OrderedDict
from django.utils.translation import ugettext_lazy as _
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class LegacyPaginator(PageNumberPagination):
    page_size = 25

    def get_paginated_response(self, data):
        links = OrderedDict()
        if self.page.has_next():
            links['next'] = OrderedDict([
                ('href', self.get_next_link()),
                ('title', _('page suivante')),
            ])
        if self.page.has_previous():
            links['prev'] = OrderedDict([
                ('href', self.get_previous_link()),
                ('title', _('page précédente')),
            ])

        meta = OrderedDict([
            ('max_results', self.page.paginator.per_page),
            ('total', self.page.paginator.count),
            ('page', self.page.number),
        ])

        return Response(OrderedDict([
            ('_items', data),
            ('_links', links),
            ('_meta', meta),
        ]))
