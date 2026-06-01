from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views import View


class DetailView(View):
    def get(self, request: HttpRequest, entity: str, identifier: int) -> HttpResponse:
        if entity not in ["book", "author"]:
            return HttpResponseNotFound()
            # design a page that shows the error
            # provide a link to return home

        return render(
            request,
            "library_manager/detail.html",
            context={"entity": entity},
        )
