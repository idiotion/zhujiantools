#!/usr/bin/python
# -*- coding: utf-8 -*- #

import time
import inspect
from lxml import etree

#默认命名空间
nsmapdict={'a':'attribute','o':'object','c':'collection'}
idno=0

class PubItem(object):
    def __init__(self , name , code , comment=None):
        self.name = name
        self.code = code
        self.creationDate = str(int(time.time()))
        self.creator = u'ZhuJian'
        self.modificationDate = str(int(time.time()))
        self.modifier = u'ZhuJian'
        self.comment = comment

    def getidno(self):
        global idno
        idno += 1
        return 'o'+str(idno)
        # return '{0}{1}'.format(str(int(time.time())),str(idno))


    def setdefaultelement(self,xmlelement):
        etree.SubElement(xmlelement, "{attribute}ObjectId").text = self.getidno()
        if self.name:
            etree.SubElement(xmlelement, "{attribute}Name").text = self.name
        if self.code:
            etree.SubElement(xmlelement, "{attribute}Code").text = self.code
        if self.creationDate:
            etree.SubElement(xmlelement, "{attribute}CreationDate").text = self.creationDate
        if self.creator:
            etree.SubElement(xmlelement, "{attribute}Creator").text = self.creator
        if self.modificationDate:
            etree.SubElement(xmlelement, "{attribute}ModificationDate").text = self.modificationDate
        if self.modifier:
            etree.SubElement(xmlelement, "{attribute}Modifier").text = self.modifier
        if self.comment:
            etree.SubElement(xmlelement, "{attribute}Comment").text = self.comment

if __name__=='__main__':
    pass