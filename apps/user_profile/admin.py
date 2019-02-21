from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from datetime import date

from .models import Profile, Transaction, Account
 


admin.site.unregister(User)
class ProfileInline(admin.StackedInline):
	model = Profile
	can_delete = False
	verbose_name_plural = 'Profile'
	fk_name = 'user'


@admin.register(User)
class CustomUserAdmin(UserAdmin):
	inlines = (ProfileInline, )

	def get_inline_instances(self, request, obj=None):
		if not obj:
			return list()
		return super(CustomUserAdmin, self).get_inline_instances(request, obj)


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
	list_display = ('user', 'balance', 'point')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
	list_display = ('from_user', 'to_user', 'amount', 'created')







# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
# 	list_display = ('address', 'dob', 'mobile', 'country', 'gender', 'profession', 'get_age')
# 	list_display_links = ('address', 'mobile')
# 	list_editable = ('dob', 'country')
# 	list_filter = ('gender',)
# 	search_fields = ('address', 'mobile', 'profession')
# 	# fields = ['mobile', 'address',( 'dob', 'gender', 'country', 'profession')]

# 	# fieldsets = (
# 	# 	(None, {
# 	# 		'fields': ('address', 'dob', 'mobile', 'country')	
# 	# 	}),
# 	# 	('Availability', {
# 	# 		'fields':('gender', 'profession')	
# 	# 	})
# 	# )

# 	def get_age(self, instance):
# 		age = date.today() - instance.dob
# 		return(age.days//365.25)

# 	get_age.short_description = 'Age'