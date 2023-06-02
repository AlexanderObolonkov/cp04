from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View


from antique.models import Antique, Author, AntiqueProductionAuthor


class MainView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(
            request,
            'antique/index.html',
            context={
                'nav_bar': 'index'
            }
        )


class AntiqueCatalogView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        positions = Antique.objects.all().select_related('antique_production').order_by('-antique_id')
        paginator = Paginator(positions, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            'antique/antique_catalog.html',
            context={
                'page_obj': page_obj,
                'nav_bar': 'catalog',
            }
        )


class AuthorCatalogView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        authors = Author.objects.all()
        paginator = Paginator(authors, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            'antique/author_catalog.html',
            context={
                'page_obj': page_obj,
                'nav_bar': 'catalog',
            }
        )


class AntiquePageView(View):
    def get(self, request: HttpRequest, slug: str, *args, **kwargs) -> HttpResponse:
        position = get_object_or_404(Antique, antique_id=slug)
        authors = []
        if position:
            authors = [' '.join(j for j in i if j) for i in AntiqueProductionAuthor.objects.filter(
                antique_production=position.antique_production
            ).values_list('author__surname', 'author__name', 'author__patronymic')]
        return render(request, 'antique/antique_page.html', context={
            'position': position,
            'authors': authors,
        })
