from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, get_list_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, RedirectView, View

from .models import Prime,Sold
from .forms import AddForm,SoldForms


# Create your views here.
class MainView(TemplateView):
    template_name = 'main.htm'


class PostListView(ListView):
    model = Prime
    fields = 'all'
    template_name = 'prime_list.htm'

    def get_queryset(self):
        return Prime.objects.filter(saled__lte=timezone.now()).order_by('-saled')


class PostDetailView(DetailView):
    model = Prime
    fields = 'all'
    template_name = 'detail.htm'
    success_url = reverse_lazy('prime_list')



class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    # original
    success_url = reverse_lazy('prime_list')
    template_name = 'add.htm'

    form_class = AddForm
    model = Prime
    #fields = 'all'



class UpdatePostView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    # template_name = 'blog/post_detail.htm'
    success_url = reverse_lazy('prime_list')
    template_name = 'add.htm'


    # redirect_field_name = 'blog/post_detail.htm'
    form_class = AddForm
    model = Prime


class DeletePostView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    success_url = reverse_lazy('prime_list')
    model = Prime
    fields = 'all'


class DraftPostView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'detail.htm'
    template_name = 'draft_list.htm'
    
    model = Prime
    fields = 'all'

    def get_queryset(self):
        return Prime.objects.filter(saled__isnull=True).order_by('-created_date')

@login_required
def item_saled(request, pk):
    post = get_object_or_404(Prime, pk=pk)
    post.sell()
    return redirect('/list/', pk=pk)



 # form = SoldForms(request.POSTor None)

# 
@login_required
def transferitm(request,pk):
    
    items = Prime.objects.get(pk=pk)
    quantity=request.POST.get("quantity")
    transaction=Sold(quantity=quantity,items=items)
    if request.method =='POST':
        # value = transaction.save(commit = False)
        # value.quantity = 1
        transaction.save()
        items.quantity=items.quantity-int(quantity)
        items.save()
        return redirect('/list/', pk=pk)
        
        
        
    return render(request,'sold2.htm', {' transaction':transaction,'quantity':quantity,'items':items})

@login_required
def buy(request,pk):
    
    items = Prime.objects.get(pk=pk)
    quantity=request.POST.get("quantity")
    transaction=Sold(quantity=quantity,items=items)
    if request.method =='POST':
        # value = transaction.save(commit = False)
        # value.quantity = 1
        transaction.save()
        items.quantity=items.quantity+int(quantity)
        items.save()
        return redirect('/list/', pk=pk)
        
        
        
    return render(request,'buy.htm', {' transaction':transaction,'quantity':quantity,'items':items})

@login_required
def cart(request):
    
    items = Prime.objects.get_
    price = Prime.objects.get()
    quantity=request.POST.get("quantity")
    total = request.POST.get("total")
    transaction=Sold(quantity=quantity,items=items)
    if request.method =='POST':
    
        transaction.save()
        items.total = items.quantity * items.price
        items.save()
        return redirect('/list/')
    
    return render(request,'cart.htm', {'id':id,' transaction':transaction,'quantity':quantity,'items':items,'price':price,'total':total})











# def sold(request):
#     form = SoldForms(request.POST or None)

#     item = form.__getitem__('items')
#     item = form.__getitem__('items')
#     item = form.__getitem__('items')

#     if form.is_valid():
        
#         sell = get_object_or_404(Prime)
        

#         sold = sell.quantity - sell.Numbers_sold
#         check = form.save(commit = False)
        
#         check.save()

        
#     return render(request,'sold.htm',{'form':form })

@login_required
def item_remove(request, pk):
    post = get_object_or_404(Prime, pk=pk)
    if post:
        post.delete()
        
        return HttpResponseRedirect('prime_list')
    return redirect('prime_list', pk=pk)
