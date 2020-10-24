from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Profile

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
  
    image = models.ImageField(upload_to='images/')
    like = models.IntegerField(default=0)
    
                              
    def __str__(self):
        return self.title

    # returns url for post
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Likes(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
    post =  models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_like')
    
class Comment(models.Model):
    comment = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    created_on = models.DateTimeField(auto_now_add=True)
    

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()
        
    @classmethod
    def get_comments(cls,id):
        comments = cls.objects.filter(post__id=id)
        return comments 
       
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.author)