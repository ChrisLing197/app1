from django import forms
from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse_lazy,reverse
from django.views.generic import edit, list, DetailView 
from django.utils.decorators import method_decorator
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.template import loader, Context
from . import forms
from . import models

from django.template import RequestContext

# User Generic Views.
class UserCreate(edit.CreateView):
    model = models.User
    form_class = forms.MyRegistrationForm
    template_name = "system/registration_form.html"
    success_url = reverse_lazy('system:dashboard')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        logout(self.request)
        return super(UserCreate, self).form_valid(form)

def add(request,id):
    if request.method=='POST':
        item=get_object_or_404(models.Item,pk=id)
        cart=models.Cart
        buyer=item.user
        user=item.user
        name=item.name
        description=item.description
        condition=item.condition
        price=item.price
        quantity=item.quantity#
        allItems=models.Item.objects.all()
        AddCart.as_view()(request)

        objects=models.Cart(name=name,description=description,condition=condition, price=price,quantity=quantity)
        objects.save()
        cartall=models.Cart.objects.all()
        item.save()
        #cartall.save()

        context=RequestContext(request)
    
        #return render(request,'system/buyer_dashboard.html',{"items"allItems)
        return redirect('/dashboard')

#View that lets an admin create other staff accounts
@method_decorator(login_required, name='dispatch')
class StaffCreate(edit.CreateView):
    model = models.User
    form_class = forms.AdminRegistrationForm
    template_name = "system/registration_form.html"
    success_url = reverse_lazy('system:dashboard')

    #Checks to make sure the user the form is being sent to is an admin
    def dispatch(self, request):
        user = get_object_or_404(models.Registration, user=request.user)
        if user.role == models.Registration.ADMIN:
            return super(StaffCreate, self).dispatch(request)
        else:
            return HttpResponseForbidden()

@login_required
def request_page(request):
    if(request.GET.get('AddToCart')):
        model=models.Cart
        #obj=Items.objects.filter(name=request.GET.get(
        fields=['name','description','condition','price','quantity']
    return render(request,'system/items_2.html')

#View for post-account-creation patients to create or update their individual information
# Redirects to proper view based on user role.
@login_required
def register(request):
    user = get_object_or_404(models.Registration, user=request.user)
    if user.role == models.Registration.SELLER:
        return UserEdit.as_view()(request)
    else:
        return StaffEdit.as_view()(request)
    return HttpResponseForbidden()

#View for post-account-creation patients to create or update their individual information
class UserEdit(edit.UpdateView):
    model = models.Registration
    fields = ['primary_care', 'date_of_birth', 'phone_number', 'mail_address']
    template_name = "system/registration_profile_info.html"
    success_url = reverse_lazy('system:dashboard')

    #Retrieves the user from the database
    def get_object(self, queryset=None):
        return get_object_or_404(models.Registration, user=self.request.user)

#Form for post-account-creation staff to create or update their individual information
class StaffEdit(edit.UpdateView):
    model = models.Registration
    fields = ['date_of_birth', 'phone_number', 'mail_address']
    template_name = "system/registration_profile_info.html"
    success_url = reverse_lazy('system:dashboard')

    #Retrieves the user from the database
    def get_object(self, queryset=None):
        return get_object_or_404(models.Registration, user=self.request.user)

#Gets a list of all registered users
@method_decorator(login_required, name='dispatch')
class UserList(list.ListView):
    #Defining Parameters
    model = models.Registration
    queryset = models.Registration.objects.all()

    #Performs the request with the given parameters
    def get(self, request):
        user = get_object_or_404(models.Registration, user=request.user)
        if user.role == models.Registration.ADMIN:
            return super(UserList, self).get(request)
        else:
            return HttpResponseForbidden()

#Displays the details of a single user
@method_decorator(login_required, name='dispatch')
class UserDetail(DetailView):
    model = models.Registration

    #Performs the request with the given parameters
    def get(self, request, pk):
        user = get_object_or_404(models.Registration, user=request.user)
        if user.role == models.Registration.ADMIN:
            return super(UserDetail, self).get(request, pk)
        else:
            return HttpResponseForbidden()

#View to delete a user
@method_decorator(login_required, name='dispatch')
class UserDelete(edit.DeleteView):
    model = models.User
    success_url = reverse_lazy("system:dashboard")

    #Checks to see if the user is admin before deleting the user
    def dispatch(self, request, pk):
        user = get_object_or_404(models.Registration, user=request.user)
        if user.role == models.Registration.ADMIN:
            return super(UserDelete, self).dispatch(request, pk)
        else:
            return HttpResponseForbidden()

#View for the dashboard, each dashboard is generated separately depending on what role the user is
@login_required
def dashboard(request):
    user = get_object_or_404(models.Registration, user=request.user)
    messages = models.Message.objects.filter(recipient=user).order_by('-timestamp')
    items=models.Item.objects.filter(poster=request.user).order_by('-timestamp')
    cart=models.Cart.objects.all()
    if user.role == models.Registration.SELLER:
        appt = models.Appointment.objects.filter(seller=user)
        buyers=models.Registration.objects.filter(role='BU')

        template_name = "system/seller_dashboard.html"
        return render(request, template_name, context={'user':user, 'appts':appt, 'byrs':buyers, 'msgs':messages,'tems':items})
    elif user.role == models.Registration.BUYER:
        appt = models.Appointment.objects.filter(buyer=user)
        template_name = "system/buyer_dashboard.html"
        items=models.Item.objects.all()
        return render(request, template_name, context={'user':user, 'appts':appt, 'msgs':messages,'tems':items,'cart':cart})
    elif user.role == models.Registration.ADMIN:
        system_act = models.Activity.objects.all().order_by('-timestamp')
        users = models.Registration.objects.all()
        stats = GenerateStatisticsContext(request)
        template_name = "system/admin_dashboard.html"
        return render(request, template_name, context={'user':user, 'sys':system_act, 'users':users, 'msgs':messages, 'stat':stats})

    return HttpResponseForbidden()

def add_cart(request):
    context=RequestContext(request)
    if request.method=='post':
        form=CartForm(request.POST)
    return render_to_response('system/add_cart.html',{'form':form},context)

#Home page view
def index(request):
    return render(request, "system/home.html")

#Logout view
def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')

#View to send a message
@method_decorator(login_required, name='dispatch')
class SendMessage(edit.CreateView):
    model = models.Message
    fields = ['recipient', 'text']
    template_name = "system/message_form.html"
    success_url = reverse_lazy("system:dashboard")

    def form_valid(self, form):
        sender = models.Registration.objects.get(user=self.request.user)
        self.object = form.save(commit=False)
        self.object.sender = sender
        self.object.save()
        return super(edit.ModelFormMixin, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class NewItem(edit.CreateView):
    model=models.Item
    fields=['name','description','condition','price','quantity']
    template_name="system/item_form.html"
    success_url=reverse_lazy("system:dashboard")

    def form_valid(self,form):
        user=self.request.user
        self.object=form.save(commit=False)
        self.object.poster=user
        self.object.save()
        return super(edit.ModelFormMixin,self).form_valid(form)

@method_decorator(login_required,name='dispatch')
class AddCart(edit.CreateView):
    model=models.Cart
    fields=['name','description','condition','price','quantity']
    success_url=reverse_lazy("system:dashboard")
    def form_valid(self,form):
        buyer=self.request.user
        self.object=form.save(commit=False)
        self.object.save()
        return super(edit.ModelFormMixin,self).form_valid(form)

#Gets a list of all patients for a doctor
@method_decorator(login_required, name='dispatch')
class buyerList(list.ListView):
    #Defining Parameters
    model = models.Registration
    queryset = models.Registration.objects.filter(role=models.Registration.BUYER)
    template_name = "system/patient_list.html"

    #Performs the request with the given parameters
    def get(self, request):
        user = get_object_or_404(models.Registration, user=request.user)
        if user.role == models.Registration.SELLER:
            return super(PatientList, self).get(request)
        else:
            return HttpResponseForbidden()

#Generates basic statistics and returns them as context to be rendered
def GenerateStatisticsContext(request):
    stats = Context()
    buyers = models.Registration.objects.filter(role=models.Registration.BUYER)
    sellers = models.Registration.objects.filter(role=models.Registration.SELLER)
    stats['tot_pat'] = buyers.count()
    stats['tot_doc'] = sellers.count()
    if sellers.count() != 0:
        ratio = buyers.count() / (sellers.count())
        ratio = float("{0:.2f}".format(ratio))
    else:
        ratio = "No Sellers"
    stats['stf_rat'] = ratio
    return stats

#View to export a record as a csv file
def export_record(request, pk=None):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="record.csv"'

    csv_data = models.Record.objects.filter(id=pk)

    t = loader.get_template('system/export_record.txt')
    c = Context({
        'data': csv_data,
    })
    response.write(t.render(c))
    return response
