from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("watchlistEdit/",views.watchlistEdit,name="watchlistEdit"),
    path("listing/watchlist",views.watchlist,name="watchlist"),
    path("create-listing/",views.ListingCreateView.as_view(), name="ListingCreate"),
    path("listing/<int:id>/",views.detailView,name="ListingDetail"),
    path("listingClose/",views.listingClose,name="listingClose")
    
]
