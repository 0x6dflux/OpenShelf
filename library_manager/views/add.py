from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views import View


class AddView(View):
    def get(self, request: HttpRequest, entity: str) -> HttpResponse:
        if entity not in ["book", "author"]:
            return HttpResponseNotFound()

        return render(request, "library_manager/add.html", context={"entity": entity})
