
from django.shortcuts import render, redirect, get_object_or_404
from application.models import *
from django.views.decorators.http import require_POST
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from decimal import Decimal

def clear_cart(request):
    if request.method == 'POST':
        request.session['cart'] = {}
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


def index(request):
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts, 8)  # Sahifadagi postlar soni
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj})

def post_detail(request, post_id):
    # Post obyektini bazadan olish yoki topilmaganda 404 xatolik qaytarish
    post = get_object_or_404(Post, id=post_id)

    # Savatcha ma'lumotlarini sessiondan olish, mavjud bo'lmagan holda bo'sh lug'at qaytarish
    cart = request.session.get('cart', {})

    # Mahsulotlar ro'yxatini joylash uchun bo'sh ro'yxat tayyorlash va umumiy narxni boshlash
    products = []
    total_price = 0

    # Savatchadagi har bir mahsulot uchun bu mos keladigan Post obyektini qidirish
    for cart_post_id, quantity in cart.items():
        try:
            cart_post_id = int(cart_post_id)  # cart_post_id ni butun sona aylantiramiz
        except ValueError:
            continue  # Agar cart_post_id to'g'ri butun son emas bo'lsa, bu elementni o'tkazamiz

        # Post obyektini bazadan olish yoki 404 xatolik qaytarish
        cart_post = get_object_or_404(Post, id=cart_post_id)

        # Ushbu mahsulot uchun narxni hisoblash
        product_price = cart_post.price * quantity
        total_price += product_price

        # Mahsulotlar ro'yxatiga mahsulot ma'lumotlarini qo'shish
        products.append({
            'post': cart_post,
            'quantity': quantity,
            'product_price': product_price
        })

    # Barcha maqolalarni olish
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts, 4)  # Sahifadagi postlar soni
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Ma'lumotlarni 'info.html' shabloniga o'tkazish uchun render funksiyasidan foydalanish
    context = {
        'post': post,
        'products': products,
        'total_price': total_price,
        'page_obj': page_obj
    }

    return render(request, 'info.html', context)



@require_POST
def add_to_cart(request):
    post_id = request.POST.get('post_id')
    quantity = request.POST.get('quantity')

    if post_id and quantity:
        cart = request.session.get('cart', {})
        cart[post_id] = int(cart.get(post_id, 0)) + int(quantity)
        request.session['cart'] = cart
        return HttpResponse(status=204)  # Ma'lumotlar muvaffaqiyatli saqlandi
    return JsonResponse({'error': 'Invalid data'}, status=400)


def cart_count(request):
    cart = request.session.get('cart', {})
    cart_item_count = sum(cart.values())
    return JsonResponse({'cart_item_count': cart_item_count})


def calculate_total_price(cart):
    total_price = Decimal(0)
    for post_id, quantity in cart.items():
        post = get_object_or_404(Post, id=post_id)
        product_price = post.price * quantity
        total_price += product_price
    return total_price


@require_POST
def place_order(request):
    if request.method == 'POST':
        name = request.POST.get('ism')
        phone = request.POST.get('telefon')
        address = request.POST.get('manzil')
        cart = request.session.get('cart', {})

        total_price = calculate_total_price(cart)

        # Mahsulotlarni oddiy matn formatida yig'ish
        mahsulotlar = []
        for post_id, quantity in cart.items():
            post = get_object_or_404(Post, id=post_id)
            mahsulotlar.append(f"{post.title} (x{quantity})")
        mahsulotlar_text = ", ".join(mahsulotlar)

        # Buyurtmani saqlash
        buyurtma = Buyurtma.objects.create(
            ism=name,
            telefon=phone,
            manzil=address,
            umumiy_narx=total_price,
            mahsulotlar=mahsulotlar_text  # Mahsulotlar maydoniga saqlash
        )

        # Cartni tozalash
        request.session['cart'] = {}

        return JsonResponse({'success': True, 'order_id': buyurtma.id, 'total_price': str(total_price)})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})


def order(request):
    return render(request, 'order.html')

@require_POST
def update_cart(request, post_id, action):
    cart = request.session.get('cart', {})

    if action == 'update':
        quantity = int(request.POST.get('quantity', 0))
        if quantity > 0:
            cart[str(post_id)] = quantity
        else:
            if str(post_id) in cart:
                del cart[str(post_id)]
    elif action == 'remove':
        if str(post_id) in cart:
            del cart[str(post_id)]

    request.session['cart'] = cart
    return JsonResponse({'success': True, 'total_price': calculate_total_price(cart)})





def remove_from_cart(request, post_id):
    try:
        cart = request.session.get('cart', {})
        if str(post_id) in cart:
            del cart[str(post_id)]
            request.session['cart'] = cart
        return redirect('post_detail', id=post_id)  # order_list sahifasiga o'tish
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
