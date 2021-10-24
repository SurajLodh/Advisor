from AdvisorCall.models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse, response
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status


class AdvisorViewSet(viewsets.ModelViewSet):   
    queryset = Advisor.objects.all()
    serializer_class = AdvisorSerializer
    permission_classes = [IsAdminUser]

    def create(self, request):
        serializer = AdvisorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data created !'}
            return JsonResponse(res, safe=True)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def User_create(request):
    if request.method == 'POST':
        Json_data = request.body
        stream = io.BytesIO(Json_data)
        pythondata = JSONParser().parse(stream)
        serializer = UserSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data created !'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(Json_data, content_type='application/json')

        Json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(Json_data, content_type='application/json')

def User_All(request):
    stu = User.objects.all()
    serializer = UserSerializer(stu, many=True)

    return JsonResponse(serializer.data, safe=False)