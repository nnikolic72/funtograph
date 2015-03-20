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
                new_photo_author = new_photo_member
            except ObjectDoesNotExist:
                new_photo_owner = None
                new_photo_author = None

            l_title = photo_upload_form.cleaned_data[u'title']
            l_photo = photo_upload_form.cleaned_data[u'photo']
            l_cloudinary_photo = l_photo
            l_owner = new_photo_owner
            l_author = new_photo_author
            l_format = l_cloudinary_photo.format
            l_full_url = l_cloudinary_photo.url
            l_phash = l_cloudinary_photo.metadata[u'phash']
            l_resource_type = l_cloudinary_photo.metadata[u'resource_type']
            try:
                l_dominant_color = l_cloudinary_photo.metadata[u'predominant'][u'google'][0][0]
            except:
                l_dominant_color = None

            try:
                l_photo_creation_date = l_cloudinary_photo.metadata[u'image_metadata'][u'CreateDate']
            except:
                l_photo_creation_date = None

            try:
                l_creator_tool = l_cloudinary_photo.metadata[u'image_metadata'][u'Software']
            except:
                l_creator_tool = None

            try:
                l_lens_model = l_cloudinary_photo.metadata[u'image_metadata'][u'LensModel']
            except:
                l_lens_model = None

            try:
                l_camera_make = l_cloudinary_photo.metadata[u'image_metadata'][u'Make']
            except:
                l_camera_make = None

            try:
                l_camera_model = l_cloudinary_photo.metadata[u'image_metadata'][u'Model']
            except:
                l_camera_model = None

            if l_resource_type == u'image':
                if new_photo_owner:
                    if 'photo' in request.FILES:
                        new_photo = Photo(title=photo_upload_form.cleaned_data[u'title'],
                                          photo=photo_upload_form.cleaned_data[u'photo'],
                                          author=new_photo_author,
                                          format=l_format,
                                          full_url=l_full_url,
                                          phash=l_phash,
                                          dominant_color=l_dominant_color,
                                          photo_creation_date=l_photo_creation_date,
                                          creator_tool=l_creator_tool,
                                          lens_model=l_lens_model,
                                          camera_make=l_camera_make,
                                          camera_model=l_camera_model

                                          )
                        new_photo.save()
                        new_photo.owner.add(new_photo_owner)

                        for new_category in photo_upload_form.cleaned_data[u'categories']:
                            new_photo.categories.add(new_category)
                        for new_attribute in photo_upload_form.cleaned_data[u'attributes']:
                            new_photo.attributes.add(new_attribute)

                        new_photo.save()

                    return HttpResponseRedirect(
                        reverse('photos:photographer',
                                kwargs={'p_photographer_name': new_photo_owner.name}
                        )
                    )
            else:
                # resource is not an image!
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
                    return HttpResponseRedirect(reverse('members:login'))
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
                return HttpResponseRedirect(reverse('members:login'))


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


class PhotoIDView(TemplateView):
    template_name = 'photos/photo_id.html'

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
        if request.user.is_authenticated():
            photo_id = kwargs['p_photo_id']

            try:
                photo = Photo.objects.get(id=photo_id)
            except ObjectDoesNotExist:
                photo = None

            if photo:

                photo_author = photo.author
                photo_owners = photo.owner

                return render(request,
                              self.template_name,
                              dict(
                                  photo=photo,
                                  photo_author=photo_author,
                                  photo_owners=photo_owners
                                  )
                )

            else:
                # photo with this ID not found
                return HttpResponseRedirect(reverse('members:dashboard'))
        else:
            # not authenticated
            return HttpResponseRedirect(reverse('members:login'))