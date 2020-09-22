from django_filters.views import FilterView
from .models import Investment
from .tables import InvestmentTable, InvestmentFilterAndSearch, InvestmentFilter
from django_tables2.views import SingleTableMixin
from django_tables2.paginators import LazyPaginator


class InvestmentTableView(SingleTableMixin, FilterView):
    model = Investment
    table_class = InvestmentTable
    filterset_class = InvestmentFilterAndSearch
    filter_action = ''
    paginator_class = LazyPaginator
    table_pagination = {'per_page': 25}
    template_name = 'partner/investments.html'

    def get_table_kwargs(self):
        kwargs = super(InvestmentTableView, self).get_table_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        search_term = self.request.GET.get('query')

        return super().get_context_data(
            search_term=search_term,
            filter_action=self.filter_action,
            **kwargs,
        )
