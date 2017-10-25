#!/usr/bin/python
# -*- coding: utf-8 -*- #

from PubMethod import PubItem,nsmapdict
import os
from lxml import etree

class PDMSymbol(PubItem):
    def __init__(self,name,code,symboltype,childid,comment=None):
        super(PDMSymbol,self).__init__(name,code,comment)
        self.symboltype=symboltype
        self.childid=childid
        self.IconMode=u'-1'
        self.Rect=u'((-7413,102), (6592,4101))'
        self.LineColor=u'12615680'
        self.FillColor=u'16570034'
        self.ShadowColor=u'12632256'
        self.FontList=u"""STRN 0 新宋体,8,N
DISPNAME 0 新宋体,8,N
OWNRDISPNAME 0 新宋体,8,N
Columns 0 新宋体,8,N
TablePkColumns 0 新宋体,8,U
TableFkColumns 0 新宋体,8,N
Keys 0 新宋体,8,N
Indexes 0 新宋体,8,N
Triggers 0 新宋体,8,N
LABL 0 新宋体,8,N"""
        self.BrushStyle='6'
        self.GradientFillMode='65'
        self.GradientEndColor='16777215'
        self.id = self.getidno()

    def toxmlelement(self):
        if self.symboltype not in (u'Package',u'Table'):
            raise Exception('标签类型[{0}]异常!'.format(self.symboltype.encode('utf-8')))
        xmlelement=etree.Element('{object}%sSymbol' % self.symboltype,nsmap=nsmapdict,Id=self.id)
        etree.SubElement(xmlelement, "{attribute}CreationDate").text = self.creationDate
        etree.SubElement(xmlelement, "{attribute}ModificationDate").text = self.modificationDate
        etree.SubElement(xmlelement,"{attribute}IconMode").text=self.IconMode
        etree.SubElement(xmlelement, "{attribute}Rect").text = self.Rect
        etree.SubElement(xmlelement, "{attribute}LineColor").text = self.LineColor
        etree.SubElement(xmlelement, "{attribute}FillColor").text = self.FillColor
        etree.SubElement(xmlelement, "{attribute}ShadowColor").text = self.ShadowColor
        etree.SubElement(xmlelement, "{attribute}FontList").text = self.FontList
        etree.SubElement(xmlelement, "{attribute}BrushStyle").text = self.BrushStyle
        etree.SubElement(xmlelement, "{attribute}GradientFillMode").text = self.GradientFillMode
        etree.SubElement(xmlelement, "{attribute}GradientEndColor").text = self.GradientEndColor
        cobject=etree.SubElement(xmlelement, "{collection}Object")
        etree.SubElement(cobject,"{object}%s" % self.symboltype,Ref=self.childid)
        return xmlelement

    def output(self):
        ele = self.toxmlelement()
        eletree=etree.ElementTree(ele)
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        eletree.write('1234.xml',encoding='utf-8',pretty_print=True)

if __name__ == '__main__':
    test = PDMSymbol(u'测试索引',u'testkey',u'232390390')
    test.output()