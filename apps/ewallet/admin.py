from django.contrib import admin
from datetime import date

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('address', 'dob', 'mobile', 'country', 'gender', 'profession', 'get_age')
	list_display_links = ('address', 'mobile')
	list_editable = ('dob', 'country')
	list_filter = ('gender',)
	search_fields = ('address', 'mobile', 'profession')
	# fields = ['mobile', 'address',( 'dob', 'gender', 'country', 'profession')]

	# fieldsets = (
	# 	(None, {
	# 		'fields': ('address', 'dob', 'mobile', 'country')	
	# 	}),
	# 	('Availability', {
	# 		'fields':('gender', 'profession')	
	# 	})
	# )

	def get_age(self, instance):
		age = date.today() - instance.dob
		return(age.days//365.25)

	get_age.short_description = 'Age'

