from django.db import models

class User(models.Model):
		name = models.TextField()
		email = 'ZZZ'
		register_date = 'XXX'
		last_signin = 'XXX'

class Room(models.Model):
		title = 'z'
		location_xy = 'x'
		address = 'y'
		image_url = 'q'
		thumbnail = 'w'


