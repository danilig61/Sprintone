import os
from django.conf import settings
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Pass, Photo
from .serializers import PassSerializer, PhotoSerializer
from django.db import transaction
from django.http import JsonResponse
from rest_framework.views import APIView

class PassListCreateView(APIView):
    def post(self, request):
        db_host = os.environ.get('FSTR_DB_HOST', 'localhost')
        db_port = os.environ.get('FSTR_DB_PORT', '5432')
        db_login = os.environ.get('FSTR_DB_LOGIN', 'myuser')
        db_password = os.environ.get('FSTR_DB_PASS', 'mypassword')

        data = request.data

        pass_obj = Pass.objects.create(name=data.get('name'), elevation=data.get('elevation'), status='new')

        with transaction.atomic():
            pass_obj.save()

        return JsonResponse({'message': 'Data submitted successfully'})

    def post(self, request):
        data = request.data

        pass_serializer = PassSerializer(data=data)
        if pass_serializer.is_valid():
            pass_obj = pass_serializer.save(status='new')
        else:
            return JsonResponse({'error': 'Invalid pass data'})

        photos_data = data.get('photos', [])
        for photo_data in photos_data:
            photo_data['pass'] = pass_obj.id
            photo_serializer = PhotoSerializer(data=photo_data)
            if photo_serializer.is_valid():
                photo_serializer.save()
            else:
                return JsonResponse({'error': 'Invalid photo data'})

        user_data = data.get('user', {})
        pass_obj.user_name = user_data.get('name')
        pass_obj.user_email = user_data.get('email')
        pass_obj.user_phone = user_data.get('phone')
        pass_obj.save()

        return JsonResponse({'message': 'Data submitted successfully'})

