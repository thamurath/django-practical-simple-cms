'''
Created on 01/06/2011

@author: feanaro
'''
from django.contrib import admin

from django_practical_cms.search.models import SearchKeyword

class SearchKeywordAdmin(admin.ModelAdmin):
    pass


admin.site.register(SearchKeyword, SearchKeywordAdmin)

from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

class SearchKeywordInline(admin.StackedInline):
    model = SearchKeyword
    
class FlatPageAdminWithKeywords(FlatPageAdmin):
    inlines = [SearchKeywordInline]
    
    
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdminWithKeywords)
