from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.translation import ugettext as _

from .forms import (
    UserForm,
    MemberForm,
    LoginForm
)

from .models import User

from funtograph.settings.base import SHOW_TRANSLATIONS

# Create your views here.
class MemberHomePageView(TemplateView):
    """
    Member home page
    """

    template_name = 'members/index.html'

    def get(self, request, *args, **kwargs):
        '''Serve GET request'''

        if request.user.is_authenticated():
            self.template_name = 'members/index.html'

            return render(request, self.template_name,
                          dict(request=request, )
            )
        else:
            return HttpResponseRedirect(reverse('lander:index'))


class MemberRegisterView(TemplateView):
    """
    Handles showing and parsing registration form.
    """

    def post(self, request, *args, **kwargs):
        """
        Serve POST request - when user submits registration form
        """

        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = MemberForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user_form.clean()
            profile_form.clean()

            new_user = User(username=user_form.cleaned_data[u'username'],
                            email=user_form.cleaned_data[u'email']
            )

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            new_user.set_password(user_form.cleaned_data[u'password1'])
            new_user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = new_user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Login this new user so they can get Welcome page

            new_user_login = authenticate(username=new_user.username, password=new_user.password)

            if new_user_login is not None:
                if new_user_login.is_active:
                    login(request, new_user)
                    # Redirect to a success page.
                    return HttpResponseRedirect(reverse('members:welcome'))
                else:
                    # Return a 'disabled account' error message
                    return HttpResponseRedirect(reverse('members:disabled'))
            else:
                # Return an 'invalid login' error message.
                login_form = LoginForm()
                return render(request,
                              'members/login.html',
                              dict(
                                  # Todo: insert Login form here
                                  login_form=login_form,
                                  errors_login=_('You can now login.'),
                              )
                )



        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            # redirect to registration form
            new_user_form = UserForm()
            new_profile_form = MemberForm()
            return render(request,
                          'members/register.html',
                          dict(
                              user_form=new_user_form,
                              profile_form=new_profile_form,
                              errors_user=user_form.errors,
                              errors_profile=profile_form.errors,
                          )
            )


    def get(self, request, *args, **kwargs):
        """
        Serve GET request - swoh registration form
        """

        registered = False

        user_form = UserForm()
        profile_form = MemberForm()

        # Render the template depending on the context.
        return render(request,
                      'members/register.html',
                      dict(
                          user_form=user_form,
                          profile_form=profile_form,
                          errors_user=None,
                          errors_profile=None,
                      )
        )


class MemberLoginView(TemplateView):
    """

    """

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('members:dashboard'))
        else:
            # return HttpResponseRedirect(reverse('members:login'))
            login_form = LoginForm()

            return render(request,
                          'members/login.html',
                          dict(
                              login_form=login_form,
                              errors_login=None,
                          )
            )

    def post(self, request, *args, **kwargs):
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            # Use Django's machinery to attempt to see if the username/password
            # combination is valid - a User object is returned if it is.
            login_form.clean()
            username = login_form.cleaned_data[u'username']
            password = login_form.cleaned_data[u'password']
            user = authenticate(username=username,
                                password=password
            )

            # If we have a User object, the details are correct.
            # If None (Python's way of representing the absence of a value), no user
            # with matching credentials was found.
            if user:
                # Is the account active? It could have been disabled.
                if user.is_active:
                    # If the account is valid and active, we can log the user in.
                    # We'll send the user back to the homepage.
                    login(request, user)
                    return HttpResponseRedirect(reverse('members:dashboard'))
                else:
                    # An inactive account was used - no logging in!
                    # return HttpResponse("Your Funtograph account is disabled.")
                    return HttpResponseRedirect(reverse('members:disabled'))

            else:
                login_form = LoginForm()
                return render(request,
                              'members/login.html',
                              dict(
                                  login_form=login_form,
                                  errors_login=_('Username or password invalid. Please try again.'),
                              )
                )
        else:
            login_form = LoginForm()
            return render(request,
                          'members/login.html',
                          dict(
                              login_form=login_form,
                              errors_login=_('Username or password invalid. Please try again.'),
                          )
            )


class MemberWelcomeView(TemplateView):
    template_name = 'members/welcome-new-member.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return render(request,
                          self.template_name,
                          dict(
                          )
            )
        else:
            return HttpResponseRedirect(reverse('members:register'))


class MemberDashboardView(TemplateView):
    template_name = 'members/dashboard.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return render(request,
                          self.template_name,
                          dict(
                          )
            )


class MemberDisabledView(TemplateView):
    template_name = 'members/disabled.html'

    def get(self, request, *args, **kwargs):
        return render(request,
                      self.template_name,
                      dict(
                      )
        )


class MemberLogoutView(TemplateView):
    template_name = 'members/logout.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            logout(request)
            return render(request,
                          self.template_name,
                          dict(
                          )
            )