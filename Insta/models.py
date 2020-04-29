from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from imagekit.models import ProcessedImageField


# about User
class InstaUser(AbstractUser):
    #继承
    profile_pic = ProcessedImageField(
        upload_to='static/images/profiles', #存的位置
        format='JPEG',
        options={'quality':100},
        blank= True,
        null=True
        )

    def get_connections(self):
        connections = UserConnection.objects.filter(creator=self)
        return connections

    def get_followers(self):
        followers = UserConnection.objects.filter(following=self)
        return followers

    def is_followed_by(self, user):
        followers = UserConnection.objects.filter(following=self)
        return followers.filter(creator=user).exists()
    
    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])

    def __str__(self):
        return self.username


class UserConnection(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)

    creator = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name="friendship_creator_set")
    following = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name="friend_set")

    def __str__(self):
        return self.creator.username + ' follows ' + self.following.username

# Create your models here.
class Post(models.Model): #继承models里的Model

    author = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name= 'my_posts'
    )

    title = models.TextField(blank= True, null=True)
    # image = models.ImageField() 功能不够强大
    # we need third-party class
    # then we need to install a third-party 
    image = ProcessedImageField(
        upload_to='static/images/posts', #存的位置
        format='JPEG',
        options={'quality':100},
        blank= True,
        null=True
        )
    
    def __str__(self):
        return self.title

    def get_like_count (self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse ("post_detail", args=[ str(self.id) ])
    
    def get_comment_count(self):
        return self.comments.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments',)
    user = models.ForeignKey(InstaUser, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.comment


class Like(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete = models.CASCADE,
        # 对一个posts的所有likes
        related_name= 'likes'
        )
    user = models.ForeignKey(
        InstaUser,
        on_delete = models.CASCADE,
        related_name ='likes'
    )
    #定义关系 post 和 user 只能like一次
    class Meta:
        unique_together= ("post", "user")

    def __str__(self):
        return 'like: ' + self.user.username + ' likes ' + self.post.title

# 建立user connection
