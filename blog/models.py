from django.contrib.auth.models import User

from django.db import models


STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

# This model is for the blog posts. It has a title, slug, author, content, created_on, updated_on, status, 
# and excerpt fields. The title and slug fields are unique, which means that no two posts can have the same 
# title or slug. The author field is a foreign key to the User model, which means that each post is 
# associated with a specific user. The content field is a text field that can contain any amount of text.
# The created_on and updated_on fields are DateTimeFields that automatically set the date and time when 
# the post is created or updated. The status field is an integer field that can be either 0 (Draft) or 1 
# (Published). The excerpt field is a text field that can be left blank.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts"
    
)
    class Meta:
        ordering = ["created_on", "author"]
           
    def __str__(self):
        return f"The title of this post is {self.title} written by {self.author}."      
        
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    
  
    
    

# This model is for comments on the blog posts. It has a foreign key to the Post model, which means that each
# comment is associated with a specific post. The author of the comment is also a foreign key to the User model, 
# which means that each comment is associated with a specific user. The body of the comment is a text field, 
# and there is a boolean field to indicate whether the comment has been approved or not. The created_on field is 
# a DateTimeField that automatically sets the date and time when the comment is created.
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    # This class is used to specify the ordering of the comments. In this case, the comments will be ordered by
    # the created_on field in ascending order.
    class Meta:
        ordering = ["created_on"]
        
    def __str__(self):
        return f"Comment {self.body} by {self.author}"   
