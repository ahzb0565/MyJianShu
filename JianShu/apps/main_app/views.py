from django.views.generic import TemplateView
from .forms import LoginForm
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


class Index(TemplateView):
    template_name = 'main_app/index.html'


class LoginView(TemplateView):
    template_name = 'main_app/login.html'

    def get(self, request):
        form = LoginForm()
        return self.render_to_response({'form': form})

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Login successfully!')
                else:
                    return HttpResponse('Account disabled')
            else:
                return HttpResponse('Invalid username or password')
        else:
            return HttpResponse('Invalid login')


class LogoutView(TemplateView):
    template_name = 'main_app/index.html'

    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return HttpResponse('Logout successfully!')

