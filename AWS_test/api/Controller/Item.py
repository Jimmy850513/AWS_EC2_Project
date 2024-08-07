from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from ..Models.items import Item
import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.utils.text import get_valid_filename
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

class Item_Create(TemplateView):
    template_name = 'item_create.html'
    def get(self,request,*args,**kwargs):
        template_dict = dict()
        return render(request,self.template_name,template_dict)

    def post(self,request,*args,**kwargs):
        data_form = request.POST
        file_form = request.FILES.get('upload_file')
        if file_form:
            #確認檔名
            clean_file_name = get_valid_filename(file_form.name)
            #建立檔案的相對路徑,建構上傳路徑
            upload_path = os.path.join('images', clean_file_name)
            #使用settings裡面的Media_ROOT路徑跟你的上傳路徑合起來變成絕對路徑
            full_upload_path = os.path.join(settings.MEDIA_ROOT, upload_path)
            """
            使用 Django 的 default_storage 系统将上传的文件 file_form 保存到 upload_path 路径。
            default_storage.save(upload_path, file_form) 将文件保存到指定路径，并返回保存后的文件路径
            """
            path = default_storage.save(upload_path, file_form)
            #构建文件的相对 URL
            file_url = os.path.join(settings.MEDIA_URL, upload_path)
        else:
            file_url = ''
        try:
            Item.objects.create(name=data_form['item_name'],price=data_form['price'],
                                description=data_form['description'],Item_image=file_url)
            msg='儲存成功'
        except Exception as e:
            print(e)
            msg=f'儲存失敗,失敗原因{e}'
        template_dict = dict(
            msg=msg,
            data_form=data_form
        )
        return render(request,self.template_name,template_dict)