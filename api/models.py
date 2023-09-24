import random
import string
from django.db import models

def generate_unique_code():
	length = 6

	while True:
		code = ''.join(random.choices(string.ascii_uppercase, k=length))
		if Resume.objects.filter(code=code).count() == 0:
			break;

	return code


class Resume(models.Model):
	code = models.CharField(max_length=8, default=generate_unique_code, unique=True)
	host = models.CharField(max_length=10, default="unknown")

	title = models.CharField(max_length=15, unique=True, null=False)
	content = models.TextField()
	type = models.CharField(max_length=10, null=False)
	visible = models.BooleanField(default=True)

	created_at = models.DateTimeField(auto_now_add=True)