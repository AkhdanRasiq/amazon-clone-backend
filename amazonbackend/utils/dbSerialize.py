class dbSerialize:
  @staticmethod
  def serializeProduct(a_objProduct):
    return {
      "id"      : (a_objProduct.id),
      "title"   : (a_objProduct.title),
      "price"   : (a_objProduct.price),
      "rating"  : (a_objProduct.rating)
    }