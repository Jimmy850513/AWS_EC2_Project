from django.shortcuts import render
from django.views.generic import TemplateView
from ..Models.items import Item

class Items_All_Views(TemplateView):
    template_name = 'items.html'
    
    def get(self,request,*args,**kwargs):
        try:
            Item_data = Item.objects.all()
        except Exception as e:
            print(e)    
        template_dict = dict(
            item_data=Item_data
        )
        return render(request,self.template_name,template_dict)

    def post(self,request,*args,**kwargs):
        template_dict = dict()
        return render(request,self.template_name,template_dict)
    
