from django.urls import path, include

from book.views import book_list, book_detail, post_share, tag_list_book

urlpatterns = [
    path('', book_list),
    path('book/<int:id>/<str:name>', book_detail),
    path('share/<int:id>', post_share),
    path('book-list/<str:slug>', tag_list_book),
]
