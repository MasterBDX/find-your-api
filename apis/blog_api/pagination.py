from rest_framework.pagination import PageNumberPagination

class BasicPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'page'