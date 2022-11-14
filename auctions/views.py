from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView,DetailView

from .models import User,Listing,Bid
from .forms import ListingForm,BidForm


def index(request):
    listings = Listing.objects.filter(is_actif=True)
    context={
        "listings":listings
    }
    return render(request, "auctions/index.html", context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def watchlistEdit(request,*args,**kwargs):
    if request.method=='POST':
        id_=request.POST['id']
        listing = get_object_or_404(Listing,id=id_)
        user = request.user
        if user in listing.watchlist.all():
            listing.watchlist.remove(user)
        else: listing.watchlist.add(user)
        return HttpResponseRedirect(reverse('ListingDetail',kwargs={'id':id_}))
    if request.method=='GET':
        return HttpResponseRedirect(reverse('watchlist'))

def watchlist(request,*args,**kwargs):
    listings=Listing.objects.filter(watchlist=request.user)
    if len(listings)==0:
        empty=True
    else: empty=False
    context={
        'objects':listings,
        'empty':empty
    }
    return render(request,'auctions/watchlist.html',context)

def detailView(request,id):
    listing=Listing.objects.get(id=id)
    if listing.is_actif==False:
        return closedView(request,id=id)
    user = request.user
    inWatchlist=""
    if request.user in listing.watchlist.all():
        inWatchlist="Remove from watchlist"
    else: inWatchlist="Add to watchlist"
    bidForm = BidForm(request.POST or None,bider=user,aListing=listing)
    if bidForm.is_valid():
            bidForm.save()
            listing.watchlist.add(user) #adding the Listing to watchlist after bidding
            bidForm = BidForm()
            return HttpResponseRedirect(reverse('ListingDetail',kwargs={'id':id}))
    allBids = Bid.objects.filter(listing=listing).order_by('-amount')

    context={
        'object':listing,
        'inWatchlist':inWatchlist,
        'bidForm':bidForm,
        'bidList':allBids,
    }
    return render(request,'auctions/detailListing.html',context)

def listingClose(request,*args,**kwargs):
    if request.method == 'POST':
        id_=request.POST['id']
        listing = get_object_or_404(Listing,id=id_)
        print("request.user= ",request.user,"  lister= ",listing.lister)
        if not request.user==listing.lister:
            print("request.user=",request.user,"  lister=",listing.lister)
            return HttpResponseRedirect(reverse('index'))
        else:
            listing.is_actif=False
            listing.save()
    return HttpResponseRedirect(reverse('ListingDetail',kwargs={'id':id_}))

def closedView(request,id):
    listing = get_object_or_404(Listing,id=id)
    winner = None
    try:
        bids = Bid.objects.filter(listing=listing).order_by('-amount')
        winner = bids[0].bider
    except:
        pass
    
    is_lister = False
    if request.user==listing.lister:
        is_lister = True
    context = {
        'object':listing,
        'is_lister':is_lister,
        'winner':winner
    }
    return render(request,'auctions/closedListing.html',context)

class ListingCreateView(CreateView):
    template_name = 'auctions/createListing.html'
    form_class = ListingForm
    queryset = Listing.objects.all()

# class ListingDetailViews(DetailView):
#     queryset = Listing.objects.all()
#     template_name = 'auctions/detailListing.html'
#     def get_context_data(self, **kwargs):
#         context =super().get_context_data(**kwargs)
#         user = self.request.user
#         obj=Listing.objects.get(id=kwargs['id'])
#         inWatchlist="Add to watchlist"
#         context["inWatchlist"]=inWatchlist
#         if user in obj.watchlist:
#             context['inWatchlist']="Remove from watchlist"
#         return context
#     def get_object(self):
#         id_= self.kwargs.get('id')
#         return get_object_or_404(Listing,id=id_)
