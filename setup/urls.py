from django.urls import path
from django.conf.urls.static import static
from setup import settings

from filmes.views import FilmeCreateView, FilmeDeleteView, FilmeDetailView, FilmeListView, FilmeUpdateView, GeneroCreateView, GeneroDeleteView, GeneroDetailView, GeneroListView, GeneroUpdateView

urlpatterns = [
    path('', GeneroListView.as_view(), name='genero_list'),
    path('create/', GeneroCreateView.as_view(), name='genero_create'),
    path('<int:pk>/', GeneroDetailView.as_view(), name='genero_detail'),
    path('<int:pk>/edit/', GeneroUpdateView.as_view(), name='genero_update'),
    path('<int:pk>/delete/', GeneroDeleteView.as_view(), name='genero_delete'),

    path('filmes/', FilmeListView.as_view(), name='filme_list'),
    path('filmes/create/', FilmeCreateView.as_view(), name='filme_create'),
    path('<int:pk>/', FilmeDetailView.as_view(), name='filme_detail'),
    path('<int:pk>/edit/', FilmeUpdateView.as_view(), name='filme_update'),
    path('<int:pk>/delete/', FilmeDeleteView.as_view(), name='filme_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)