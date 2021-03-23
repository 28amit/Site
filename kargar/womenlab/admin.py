from django.contrib import admin
from womenlab.models import Contact
from womenlab.models import Banner
from womenlab.models import FirstBanner
from womenlab.models import Course
from womenlab.models import Order

class AdminContact(admin.ModelAdmin):
	list_display = ['name','phone','comments']


class AdminBanner(admin.ModelAdmin):
	list_display = ['name','banner']


class AdminfBanner(admin.ModelAdmin):
	list_display = ['name','banner']

class AdminCourse(admin.ModelAdmin):
	list_display = ['name','image','price','description','Duration','time','module','slug']
	prepopulated_fields = {'slug':('name',)}

class AdminOrder(admin.ModelAdmin):
	list_display = ['course_name','name','phone','email','amount','payment_id','paid']
	
		
	
		
# Register your models here.
admin.site.register(Contact, AdminContact)
admin.site.register(Banner, AdminBanner)
admin.site.register(FirstBanner, AdminfBanner)
admin.site.register(Course, AdminCourse)
admin.site.register(Order, AdminOrder)

