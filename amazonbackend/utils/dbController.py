import logging
from apis.models import ProductModel

class dbController:
  @staticmethod
  def getAllProduct():
    try:
      return ProductModel.objects.all()
    except Exception as e:
      logging.error(e)
      return False
  
  @staticmethod
  def getProductById(a_iProductId):
    try:
      return ProductModel.objects.get(pk=a_iProductId)
    except Exception as e:
      logging.error(e)
      return False
