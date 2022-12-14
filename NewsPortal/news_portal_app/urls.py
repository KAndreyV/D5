from django.urls import path
# Импортируем созданные нами представления
from .views import (
   PostsList, PostDetail, PostSearch, NewsCreate, NewsUpdate, NewsDelete, ArticlesCreate, ArticlesUpdate, ArticlesDelete
)


urlpatterns = [
   path('', PostsList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('search', PostSearch.as_view()),
   path('news/create', NewsCreate.as_view(), name='post_create'),
   path('news/<int:pk>/edit', NewsUpdate.as_view(), name='post_update'),
   path('news/<int:pk>/delete', NewsDelete.as_view(), name='post_delete'),
   path('articles/create', ArticlesCreate.as_view(), name='post_create'),
   path('articles/<int:pk>/edit', ArticlesUpdate.as_view(), name='post_update'),
   path('articles/<int:pk>/delete', ArticlesDelete.as_view(), name='post_delete'),
]