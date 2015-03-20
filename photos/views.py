from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from django.core.exceptions import ObjectDoesNotExist

import cloudinary

from .forms import PhotoUploadForm
from .models import Photo
from characters.models import Photographer
from members.models import Member

# Create your views here.
class PhotosUploadView(TemplateView):
    template_name = 'photos/upload.html'

    def get(self, request, *args, **kwargs):
        """
        Handle get request

        :param request:
        :type request:
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """
        if request.user.is_authenticated():
            upload_form = PhotoUploadForm()
            return render(request,
                          'photos/upload.html',
                          dict(
                              upload_form=upload_form,

                              )
            )
        else:
            return HttpResponseRedirect(reverse('members:register'))

    def post(self, request, *args, **kwargs):
        """
        Handle photo upload form with POST method

        :param request:
        :type request:
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """

        photo_upload_form = PhotoUploadForm(data=request.POST, files=request.FILES)

        if photo_upload_form.is_valid():
            photo_upload_form.clean()
            owner_user_id = request.user.id
            try:
                new_photo_member = Member.objects.get(user__id=owner_user_id)
                new_photo_owner = Photographer.objects.get(member=new_photo_member)
                new_photo_author = new_photo_owner
            except ObjectDoesNotExist:
                new_photo_owner = None
                new_photo_author = None

            if new_photo_owner:
                if 'photo' in request.FILES:
                    new_photo = Photo(title=photo_upload_form.cleaned_data[u'title'],
                                      photo=photo_upload_form.cleaned_data[u'photo'],
                                      owner=new_photo_owner,
                                      author=new_photo_author
                                      )
                    new_photo.save()
                    for new_category in photo_upload_form.cleaned_data[u'categories']:
                        new_photo.categories.add(new_category)
                    for new_attribute in photo_upload_form.cleaned_data[u'attributes']:
                        new_photo.attributes.add(new_attribute)

                    new_photo.save()
                    # Todo: redirect to members photo page
                    return HttpResponseRedirect(
                        reverse('photos:photographer',
                                kwargs={'p_photographer_name': new_photo_owner.name}
                        )
                    )
        else:
            if request.user.is_authenticated():
                upload_form = PhotoUploadForm()
                return render(request,
                              'photos/upload.html',
                              dict(
                                  upload_form=upload_form,
                                  form_errors=photo_upload_form.errors
                                  )
                )
            else:
                return HttpResponseRedirect(reverse('photos:photographer_photos'))


class MembersPhotosView(TemplateView):
    template_name = 'photos/photographer_photos.html'

    def get(self, request, *args, **kwargs):
        """
        Handle request to list members photos
        :param request:
        :type request:
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """

        photographer_name = kwargs['p_photographer_name']

        if photographer_name:
            try:
                photographer = Photographer.objects.get(name=photographer_name)
            except ObjectDoesNotExist:
                photographer = None

            if photographer:
                photographer_photos = Photo.objects.filter(owner=photographer)

                return render(request,
                              'photos/photographer_photos.html',
                              dict(
                                  photographer_photos=photographer_photos,
                                  photographer=photographer
                                  )
                )
            else:
                return HttpResponseRedirect(reverse('members:dashboard'))

        else:
            return HttpResponseRedirect(reverse('members:dashboard'))
