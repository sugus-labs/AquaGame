from django.db import models
from django.forms import ModelForm

class Ball(models.Model):
	COLOUR_OPTIONS = (
		('W', 'white'), ('B', 'black'), ('P', 'purple'), ('R', 'red'), 
		('Y', 'yellow'), ('G', 'green'),('O', 'orange'), ('L', 'blue'),
		('I', 'pink'), ('A', 'gray'),
		)
	colour = models.CharField(max_length=1, choices=COLOUR_OPTIONS, default='W',
		help_text = "Select the colour of the ball from list.")
	liquid_contained = models.CharField(max_length=100,
		help_text = "Write the name of the liquid inside the ball.")
	liquid_contained_density = models.FloatField(
		help_text = "Write the density of the liquid inside the ball. The format must be '1.24' or '0.567'.")
	# example_image = models.ImageField(upload_to = 'admin_ball_images', 
	#	help_text = "This image helps you to recognize the ball in the water")
	# ball_weight = models.FloatField(
	#	help_text = "Write the weight of the ball without the liquid. The format must be '1.24' or '0.567'.")
	# ball_total_weight = models.FloatField(
	#	help_text = "Write the weight of the ball with the liquid. The format must be '1.24' or '0.567'.")
	# ball_diameter = models.FloatField(
	#	help_text = "Write the diameter of the ball. The format must be '1.24' or '0.567'.")
	date_refreshed = models.DateTimeField(auto_now=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return unicode(self.colour)

class Participant(models.Model):
	nick_name = models.CharField(max_length=100,
		help_text = "Write your nick or name in this field.")
	time_needed = models.CharField(max_length=10)
	date_created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return unicode(self.nick_name)

class BallForm(ModelForm):
	class Meta:
		model = Ball
		exclude = ('date_refreshed', 'date_created')
