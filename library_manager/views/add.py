from typing import Any, Optional

from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views import View

from library_manager.models.author import Author
from library_manager.models.book import Book


class AddView(View):
    def get(self, request: HttpRequest, entity: str) -> HttpResponse:
        AddView.check_entity(entity)

        context: dict[str, Any] = {"entity": entity}

        if entity == "book":
            context["fields"] = [
                ("id0", "text", "Title"),
                ("id1", "date", "Published Date"),
                ("id2", "text", "ISBN"),
                ("id3", "list", "Authors"),
            ]
        elif entity == "author":
            context["fields"] = [
                Author.first_name,
                Author.last_name,
                Author.age,
                Author.number_of_published_books,
            ]

        print("***", context)

        return render(request, "library_manager/add.html", context)

    def post(self, request: HttpRequest, entity: str) -> HttpResponse:
        AddView.check_entity(entity)

        return render(request, "", context={"entity": entity})

    @staticmethod
    def check_entity(entity: str) -> HttpResponseNotFound:
        if entity not in ["book", "author"]:
            return HttpResponseNotFound()
