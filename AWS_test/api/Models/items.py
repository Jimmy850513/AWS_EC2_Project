from django.db import models

class Item(models.Model):
    id = models.AutoField(primary_key=True,help_text='商品ID')
    name = models.CharField(max_length=200,null=False,help_text='商品名稱')
    price = models.IntegerField(null=False,help_text='價格')
    status = models.CharField(max_length=20,help_text='商品目前的狀態',null=True)
    Item_image = models.CharField(max_length=300,null=True)
    description = models.TextField(null=False,help_text='商品描述')
    created_at = models.DateTimeField(auto_now_add=True,help_text='商品創建時間')
    updated_at = models.DateTimeField(auto_now=True,help_text='商品更新時間',null=True)

    class Meta:
        db_table = 'Items'


