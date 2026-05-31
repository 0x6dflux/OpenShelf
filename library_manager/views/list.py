from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views import View


class ListView(View):
    def get(self, request: HttpRequest, entity: str) -> HttpResponse:
        if entity not in ["book", "author"]:
            return HttpResponseNotFound()
            # design a page that shows the error
            # provide a link to return home

        return render(request, "library_manager/list.html", context={"entity": entity})
