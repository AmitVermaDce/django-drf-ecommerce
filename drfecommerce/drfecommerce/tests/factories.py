import factory
from drfecommerce.product.models import Brand, Category, Product

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
        
    name = factory.Sequence(lambda n: "Category %d" %n)
    # name = "test_cat"
    
    
class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand
        
    name = factory.Sequence(lambda n: "Brand %d" %n)
    # name = "test_brand"
    
    
class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
        
    name = "test_product"
    description = "test_description"
    is_digital = True    
    category = factory.SubFactory(CategoryFactory)
    brand = factory.SubFactory(BrandFactory)
    