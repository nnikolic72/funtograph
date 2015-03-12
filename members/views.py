from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect, HttpResponse

from .forms import (
UserForm,
MemberForm
)
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
                          dict(request=request, SHOW_TRANSLATIONS=SHOW_TRANSLATIONS,)
            )
        else:
            return HttpResponseRedirect(reverse('lander:index'))

class MemberRegisterView(TemplateView):

    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('members:welcome'))

    def get(self, request, *args, **kwargs):
        '''Serve GET request'''
        registered = False

        # If it's a HTTP POST, we're interested in processing form data.
        if request.method == 'POST':
            # Attempt to grab information from the raw form information.
            # Note that we make use of both UserForm and UserProfileForm.
            user_form = UserForm(data=request.POST)
            profile_form = MemberForm(data=request.POST)

            # If the two forms are valid...
            if user_form.is_valid() and profile_form.is_valid():
                # Save the user's form data to the database.
                user = user_form.save()

                # Now we hash the password with the set_password method.
                # Once hashed, we can update the user object.
                user.set_password(user.password)
                user.save()

                # Now sort out the UserProfile instance.
                # Since we need to set the user attribute ourselves, we set commit=False.
                # This delays saving the model until we're ready to avoid integrity problems.
                profile = profile_form.save(commit=False)
                profile.user = user

                # Did the user provide a profile picture?
                # If so, we need to get it from the input form and put it in the UserProfile model.
                if 'picture' in request.FILES:
                    profile.picture = request.FILES['picture']

                # Now we save the UserProfile model instance.
                profile.save()

                # Update our variable to tell the template registration was successful.
                registered = True

            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            # They'll also be shown to the user.
            else:
                print user_form.errors, profile_form.errors

        # Not a HTTP POST, so we render our form using two ModelForm instances.
        # These forms will be blank, ready for user input.
        else:
            user_form = UserForm()
            profile_form = MemberForm()

        # Render the template depending on the context.
        return render(request,
                'members/register.html',
                dict(
                    user_form=user_form,
                    profile_form=profile_form,
                    registered=registered
                )
        )

class MemberLoginView(TemplateView):
    """

    """
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('members:dashboard'))
        else:
            return HttpResponseRedirect(reverse('members:register'))

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            # Gather the username and password provided by the user.
            # This information is obtained from the login form.
                    # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                    # because the request.POST.get('<variable>') returns None, if the value does not exist,
                    # while the request.POST['<variable>'] will raise key error exception
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Use Django's machinery to attempt to see if the username/password
            # combination is valid - a User object is returned if it is.
            user = authenticate(username=username, password=password)

            # If we have a User object, the details are correct.
            # If None (Python's way of representing the absence of a value), no user
            # with matching credentials was found.
            if user:
                # Is the account active? It could have been disabled.
                if user.is_active:
                    # If the account is valid and active, we can log the user in.
                    # We'll send the user back to the homepage.
                    login(request, user)
                    return HttpResponseRedirect(reverse('members:index'))
                else:
                    # An inactive account was used - no logging in!
                    return HttpResponse("Your Funtograph account is disabled.")
            else:
                # Bad login details were provided. So we can't log the user in.
                print ("Invalid login details: {0}, {1}".format(username, password))
                return HttpResponse("Invalid login details supplied.")

        # The request is not a HTTP POST, so display the login form.
        # This scenario would most likely be a HTTP GET.
        else:
            # No context variables to pass to the template system, hence the
            # blank dictionary object...
            return HttpResponseRedirect(reverse('members:index'))


class MemberWelcomeView(TemplateView):

    template_name = 'members/welcome-new-member.html'

    def get(self, request, *args, **kwargs):
        # Todo: Open a new user and log them in
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