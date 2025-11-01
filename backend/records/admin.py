from django.contrib import admin
from .models import *

# admin.site.register(Fees)  # Commented out (model commented in models.py)
admin.site.register(Mark)  # Changed from Marks to Mark
# admin.site.register(Backlogs)  # Commented out (model commented in models.py)
admin.site.register(Attendance)