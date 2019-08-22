from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        #check if user has already made inquiry

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'you have already made an inquiry for this listing')
                return redirect('/listings/listing_id' )

        contact = Contact( listing=listing, listing_id=listing_id, name=name, email=email, phone=phone,  message=message, user_id=user_id)
        contact.save()

        #send send_mail
        send_mail(
           'property listing inquiry',
           'there has been an inquiry for ' +listing+ '. sign into the admin parnel for more info',
           'ianmuhiajohn@gmail.com',
           [realtor_email],
           fail_silently=False
        )
        messages.success(request, 'your request has been submitted, a realtor will get back to you soon')

        return redirect('/listings/listing_id')
