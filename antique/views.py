from django.shortcuts import render
from django.views import View


class MainView(View):
    def get(self, request, *args, **kwargs):
        positions = []
        return render(
            request,
            'antique/index.html',
            context={
                'positions': positions,
                'nav_bar': 'index'
            }
        )
