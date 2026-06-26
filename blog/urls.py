from . import views
from django.urls import include, path

path("about/", include("about.urls"), name="about-urls"),


urlpatterns = [
    
    
     
    #this code is used to display the home page of the blog, which is a list of posts. 
    # The PostList view is a class-based view that inherits from Django's generic ListView. 
    # It retrieves all posts from the database and passes them to the index.html template for rendering.
    path('', views.PostList.as_view(), name='home'),
    
    # This code binds the URL pattern for the post detail page to the post_detail view function. 
    # The post_detail view function retrieves a single post based on the slug provided in the URL
    # and passes it to the post_detail.html template for rendering.
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    
    
]