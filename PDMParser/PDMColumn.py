#!/usr/bin/python
# -*- coding: utf-8 -*- #

from PubMethod import PubItem,nsmapdict
import os
from lxml import etree

class PDMColumn(PubItem):
    def __init__(self , name , code , dataType , length ,comment = None , defaultvalue = None,mandatory=False):
        """
        :param objectId:
        :param name:
        :param code:
        :param creationDate:
        :param creator:
        :param dataType:
        :param length:
        :param comment:       字段注释
        :param defaultvalue:  默认值
        :param mandatory: 是否可为空 , 1表示不可为空 , 0表示可为空
        """
        super(PDMColumn,self).__init__(name,code,comment)
        self.dataType = dataType
        self.length = length
        self.defaultvalue = defaultvalue
        self.mandatory = '1' if mandatory else '0'
        self.id=self.getidno()

    def toxmlelement(self):
        xmlelement=etree.Element('{object}Column',nsmap=nsmapdict,Id=self.id)
        super(PDMColumn,self).setdefaultelement(xmlelement)
        etree.SubElement(xmlelement, "{attribute}DataType").text = '{0}({1} char)'.format(self.dataType,self.length)
        etree.SubElement(xmlelement, "{attribute}Length").text = self.length
        if self.defaultvalue:
            etree.SubElement(xmlelement, "{attribute}DefaultValue").text = self.defaultvalue
        if self.mandatory=='1':
            etree.SubElement(xmlelement, "{attribute}Column.Mandatory").text = self.mandatory
        return xmlelement

    def output(self):
        ele = self.toxmlelement()
        eletree=etree.ElementTree(ele)
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        eletree.write('1234.xml',encoding='utf-8',pretty_print=True)

if __name__ == '__main__':
    test = PDMColumn(u'测试字段',u'testcol',u'varchar2',u'60')
    test.output()