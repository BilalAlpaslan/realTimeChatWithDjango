from django.db import models


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.SlugField()

    def __str__(self):return self.slug



class Message(models.Model):
	id = models.AutoField(primary_key=True)
	room = models.ForeignKey(Room,on_delete = models.CASCADE,related_name="message")
	author = models.ForeignKey("auth.User",on_delete = models.CASCADE,related_name="message")
	content = models.CharField(max_length = 1500,verbose_name = "Yorum")
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.content
	class Meta:
		ordering = ['date']

