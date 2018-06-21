from .models import MissingPerson, FoundPerson
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm, MissingForm, FoundForm
from django.views.generic import View
from django.shortcuts import render, get_object_or_404

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def home(request):
    return render(request, 'home/home.html')


def MissingProfiles(request):
    all_Mprofiles = MissingPerson.objects.all()
    context = {'all_Mprofiles': all_Mprofiles}
    return render(request, 'home/MissingPerson.html', context)


def FoundProfiles(request):
    all_Fprofiles = FoundPerson.objects.all()
    context = {'all_Fprofiles': all_Fprofiles}
    return render(request, 'home/FoundPerson.html', context)


def missingDetails(request, pk):
    mprofile = get_object_or_404(MissingPerson, pk=pk)
    return render(request, 'home/missingDetails.html', {'mprofile': mprofile})


def foundDetails(request, pk):
    fprofile = get_object_or_404(FoundPerson, pk=pk)
    return render(request, 'home/foundDetails.html', {'fprofile': fprofile})


def logedin(request):
    return render(request, 'home/logedin.html')


def contactus(request):
    return render(request, 'home/contactus.html')


def about(request):
    return render(request, 'home/about.html')


def mprofilecreate(request):
    if not request.user.is_authenticated():
        return render(request, 'home/LogIn_form.html')
    else:
        form = MissingForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            mprofile = form.save(commit=False)
            mprofile.user = request.user
            mprofile.MissingPersonImage = request.FILES['MissingPersonImage']
            file_type = mprofile.MissingPersonImage.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'mprofile': mprofile,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'home/mprofileform.html', context)
            mprofile.save()
            return render(request, 'home/logedin.html', {'mprofile': mprofile})
        context = {
            "form": form,
        }
        return render(request, 'home/mprofileform.html', context)


def fprofilecreate(request):
    if not request.user.is_authenticated():
        return render(request, 'home/LogIn_form.html')
    else:
        form = FoundForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            fprofile = form.save(commit=False)
            fprofile.user = request.user
            fprofile.FoundPersonImage = request.FILES['FoundPersonImage']
            file_type = fprofile.FoundPersonImage.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'fprofile': fprofile,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'home/fprofileform.html', context)
            fprofile.save()
            return render(request, 'home/logedin.html', {'fprofile': fprofile})
        context = {
            "form": form,
        }
        return render(request, 'home/fprofileform.html', context)


class UserFormView(View):
    form_class = UserForm
    template_name = 'home/registeration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                # if user.is_active:
                login(request, user)
                return redirect('home:logedin')

        return render(request, self.template_name, {'form': form})


def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'home/logedin.html')
            else:
                return render(request, 'home/LogIn_form.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'home/LogIn_form.html', {'error_message': 'Invalid login'})
    return render(request, 'home/LogIn_form.html')
