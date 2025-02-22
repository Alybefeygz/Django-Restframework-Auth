from django.urls import path, include
from profiller.api.views import ProfilViewSet, ProfilDurumViewSet, ProfilFotoUpdateView

from rest_framework.routers import DefaultRouter

# profil_list = ProfilViewSet.as_view({'get': 'list'})
# profil_detay = ProfilViewSet.as_view({'get': 'retrieve'})

router = DefaultRouter()
router.register(r'profilleri', ProfilViewSet)
router.register(r'durum', ProfilDurumViewSet, basename='durum')

urlpatterns = [
    # path('kullanici-profilleri/', profil_list, name='profiller'),
    # path('kullanici-profilleri/<int:pk>', profil_detay, name='profil-detay')
    
    path('', include(router.urls)),
    path('profil_foto/', ProfilFotoUpdateView.as_view(),name='profil-foto')
]



#? Router ile yorum satırı olarak seçilen satırlar olmadan dilediğimiz işlemi yapabildik