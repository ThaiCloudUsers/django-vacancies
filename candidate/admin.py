from django.contrib import admin

# Register your models here.
from candidate.models import Candidate

class CandidateAdmin(admin.ModelAdmin):
    pass

admin.site.register(Candidate, CandidateAdmin)
