from rest_framework import permissions, views
from rest_framework.decorators import permission_classes
from rest_framework.response import Response

class LiveChecker(views.APIView):
  permission_classes = (permissions.AllowAny, )

  def get(self, request, format=None):
    return Response("Server Is Active!", status=200)
    