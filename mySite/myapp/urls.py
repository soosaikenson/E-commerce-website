from django.urls import path   # This path function helps configure the path requested and the view utilized

from . import views  # importing the views.py from the same directory. Now all the designed views are available here


urlpatterns = [
    path('', views.home, name = "homepage"),
    path('about', views.about, name = "aboutpage" ),                            #url makes the path available  
    path('addProd', views.AddProduct.as_view(), name="addProduct"),             # addproduct is a post method
    path('products', views.ProductList.as_view(), name="products"),             # as_view() is a method for updateView
    path('prod_details/<int:id>', views.product_details, name="p_details"),      # int:id is a path convertor used for url configuration
    path('editprod/<int:pk>', views.EditProduct.as_view(), name="editProd"),
    path('delprod/<int:pk>', views.DeleteProduct.as_view(), name="del_product"),
    path('search', views.searchView, name="search"),
]


