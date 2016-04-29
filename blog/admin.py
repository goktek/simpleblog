from django.contrib import admin
from blog.models import author, post, category

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display=('Aktif','Name','Surname')
    list_per_page=20
    list_filter=['Aktif','Name','Surname']
    search_fields=['Name','Surname']
    date_hierarchy='Joined'
    list_display_links=('Name','Surname')
   ### To restrict modify/add...etc uncomment below
   # def has_add_permission(self,request):
       # return False
    #def has_delete_permission(self,request):
        #return False

    ### Lets add our custom action to the drop down list
    #def SecilenleriAktiveEt(self, modeladmin,request,queryset):
       # for k in queryset:
            #k.save
            #return ""
    #actions=(SecilenleriAktiveEt,)
    #actions_on_bottom=True
    #actions_on_top= True


admin.site.register(author, AuthorAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display=('publish','postauthor','title','content','created')
    list_per_page=20
    #hangi alanlarin duzenleme linki olacagi:
    list_display_links=('title','content')
    
   ### To restrict based on user type
    #if not request.user.is_superuser:



admin.site.register(post, PostAdmin)
