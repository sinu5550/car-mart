from django.shortcuts import render,redirect
from . import models
from . import forms
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
# Create your views here.

class CarDetailView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object 
        comments = car.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    
@login_required
def buy_now(request, id):
    car = models.Car.objects.get(pk=id)
    if car.quantity > 0:
        
        models.userPurchase.objects.create(
            author=request.user,
            car=car,
            quantity_purchased=1,
            total_price=car.price
        )

        car.quantity -= 1
        car.save()

       
    return redirect('car:car_details', id=id)