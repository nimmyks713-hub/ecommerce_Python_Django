from django.shortcuts import get_object_or_404, render, redirect,HttpResponse
from . models import Products,CartItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

def index(request):
    offers=[
        {
            "title":"Welcome to shopaholic| Your savings corner",
            "image":[
                "/images/dress.webp",
                "/images/handbag.webp",
                "/images/necklace.webp",
                "/images/jenas.jpg"
            ],
            "subtitle":[
                 "Coupons and Benefits",
                 "Bestsellers",
                 "Today's Deals",
                 "Budget Store"
            ]
        },
        {
            "title":"Upto 20% off - Electronics",
            "image":[
             "/images/Internalssd.webp",
             "/images/gamingdrive.jpg",
             "/images/siliconpower.jpg",
             "/images/playstation.jfif"
            ],
            "subtitle":[
                "Internal SSD",
                 "Gaming Drive",
                 "Silicon Power",
                 "Playstation"
            ]
        },
        {
            "title":"New arrivals|Watches and Jwellery|Upto 50% off",
            "image":[
             "/images/bracelet.webp",
             "/images/goldpetite.jpg",
             "/images/whitegold.jfif",
             "/images/rosegold.webp"
            ],
            "subtitle":[
            "Bracelet",
            "Gold Petite",
            "White Gold",
            "Rose Gold"
            ]
       },
       {
            "title":"Just landed for men|Upto 40% off",
            "image":[
            "/images/backpack.webp",
            "/images/tshirt.jpg",
            "/images/jacket.jpg",
            "/images/casual.webp"
            ],
            "subtitle":[
               "Backpack",
               "T-Shirts",
               "Jacket",
               "Casual"
            ]
        },
        {
            "title":"Upto 30% off - Headsets and Speakers",
            "image":[
             "/images/headsets.jpg",
             "/images/earbuds.jpg",
            "/images/speakers.webp",
            "images/soundbars.jpg"
            ],
            "subtitle":[
             "Headsets",
             "Earbuds",
             "Speakers",
             "Soundbars"
            ]
        },
        
        {
            "title":"Upto 20% off-Gaming corner",
            "image":[
            "/images/gamingconsole.jpg",
            "images/gamingaccessories.avif",
            "/images/pcgaming.jpg",
            "/images/headsets.jpg"
            ],
            "subtitle":[
            "Gaming Console",
            "Gaming Accessories",
            "PC Gaming",
            "Digital Content"
            ]
        },
        {
            "title":"Get your furniture assembled for free",
            "image":[
             "/images/sofa.webp",
             "/images/bed.webp",
             "/images/chair.webp",
             "/images/tableset.webp"
            ],
            "subtitle":[
             "Sofa",
             "Bed",
             "Chair",
             "Table set"
            ]
       },
        {
            "title":"Frequently purchased toys| From AED 12",
            "image":[
              "/images/pushpop.jpg",
              "/images/toys.webp",
              "/images/plush.avif",
              "/images/scooter.jpg"
            ],
            "subtitle":[
             "Push Pop",
             "Toys",
             "Plush Toy",
             "Scooter"
            ]
        }
    ]
    return render(request,'products/index.html',{"offers":offers})

def productlist(request):
    products=Products.objects.all()
    return render(request,'products/productlist.html',{'products':products})

def productdetail(request,product_id):
    product=get_object_or_404(Products,pk=product_id)
    context={"product":product}
    return render(request,'products/productdetail.html',context=context)

def aboutus(request):
    return render(request,'products/aboutus.html')

def contactus(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f"New Contact Message:\nName: {name}\nEmail: {email}\nMessage: {message}")
        return HttpResponse("Thank you for contacting us!")
    return render(request, "products/contactus.html")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"Account created successfully for {user.username}!")
            return redirect("login")  
    else:
        form = UserCreationForm()
    return render(request, "products/signup.html", {"form": form})

@login_required
def profile(request):
    return render(request, 'products/profile.html')

def add_to_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_view')

def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'products/cart.html', {'cart_items': cart_items, 'total': total})

@require_POST
def delete_cart_item(request, item_id):
    item = CartItem.objects.get(id=item_id, user=request.user)
    item.delete()
    return redirect('cart_view')




