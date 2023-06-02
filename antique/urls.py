from django.urls import path, URLResolver

from antique.views import AntiqueCatalogView, AuthorCatalogView, AntiquePageView

app_name = 'antique'

urlpatterns = [
    path('antique_catalog/', AntiqueCatalogView.as_view(), name='antique_catalog'),
    path('author_catalog/', AuthorCatalogView.as_view(), name='author_catalog'),
    path('<slug:slug>/', AntiquePageView.as_view(), name='antique_page'),
]
