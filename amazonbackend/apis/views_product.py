import json
from rest_framework import permissions, views
from rest_framework.decorators import permission_classes
from rest_framework.response import Response

from utils.dbController import dbController
from utils.dbSerialize import dbSerialize

class ProductViews(views.APIView):
  permission_classes = (permissions.AllowAny, )

  def get(self, request):
    idProduct = request.GET.get('idProduct')

    """Send All Products Data"""

    if not idProduct:
      productList = dbController.getAllProduct()
      if not productList:
        return Response([], status=200)

      payload = []
      for productData in productList:
        payload.append(dbSerialize.serializeProduct(productData))
      return Response(payload, status=200)
    
    else:
      """Send Product by ProductID"""

      objProduct = dbController.getProductById(idProduct)
      if not objProduct:
        return Response("Product you are seeking is not exist in Database", status=404)
      
      payload = dbSerialize.serializeProduct(objProduct)
      return Response(payload, status=200)
  
