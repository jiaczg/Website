from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户')  #
    nickname = models.CharField(max_length=20, verbose_name='昵称')  # 用户昵称最长20个字符

    def __str__(self):
        return '<Profile: %s for %s>' % (self.nickname, self.user.username)

    class Meta:
        verbose_name = '用户昵称'
        verbose_name_plural  = verbose_name

def get_nickname(self):
    if Profile.objects.filter(user=self).exists():  # 判断profile是否有昵称
        profile = Profile.objects.get(user=self) # 获取对应的profile
        return profile.nickname  # 返回prpfile昵称
    else:
        return ''  # 返回空

def get_nickname_or_username(self):
    if Profile.objects.filter(user=self).exists(): # 判断profile是否有昵称
        profile = Profile.objects.get(user=self) # 获取对应的profile
        return profile.nickname  # 返回prpfile昵称
    else:
        return self.username  # 没有就返回username

def has_nickname(self):
	return Profile.objects.filter(user=self).exists() # 判断profile是否有昵称


# 动态绑定赋值给User，User实际上没有这个东西
# 自己创建绑定赋值过去，就可以了使用了
User.get_nickname = get_nickname
User.get_nickname_or_username = get_nickname_or_username
User.has_nickname = has_nickname
