# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class SoloCapsulasPipeLine(object):
    def process_item(self,item,spider):
        titulo = item['titulo']
        if('capsula' not in titulo):
            raise DropItem('No tiene capsula')
        else:
            return item

class TransformarTituloAMinusculas(object):
    def process_item(self,item,spider):
        titulo = item['titulo']
        item['titulo'] = titulo.lower()
        return item

class ItemFybecaPipeline(object):
    def process_item(self, item, spider):
        return item
