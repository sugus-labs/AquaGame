from django.db import models

class Ball(models.Model):
	COLOUR_OPTIONS = (
		('W', 'White'), ('B', 'Black'), ('P', 'Purple'), ('R', 'Red'), 
		('Y', 'Yellow'), ('G', 'Green'),('O', 'Orange'), ('L', 'Blue'),
		('I', 'Pink'), ('A', 'Gray'),
		)
	colour = models.CharField(max_length=1, choices=COLOR_OPTIONS, default='W',
		help_text = "Select the colour of the ball from list.")
	liquid_contained = models.CharField(max_length=100,
		help_text = "Write the name of the liquid inside the ball.")
	liquid_contained_density = models.CharField(max_length=20,
		help_text = "Write the density of the liquid inside the ball. The format must be '1.24' or '0.567'.")
	date_refreshed = models.DateTimeField(auto_now=True)
	date_created = models.DateTimeField(auto_now_add=True)