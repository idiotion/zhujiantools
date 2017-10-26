#!/usr/bin/python
# -*- coding: utf-8 -*- #

from PubMethod import PubItem,nsmapdict
import os
from lxml import etree
from PDMTable import PDMTable
from PDMPhysicalDiagram import PDMPhysicalDiagram

class PDMPackage(PubItem):
    def __init__(self,name , code ,comment=None):
        super(PDMPackage,self).__init__(name,code,comment)
        self.physicalDiagram=PDMPhysicalDiagram(name,code)
        self.tablelist=[]
        self.id=self.getidno()

    def addtable(self ,name, code,comment=None ,totalSavingCurrency=None):
        """
        在Package中增加实体表
        :param name:    中文表名
        :param code:    英文表名
        :param comment: 表注释
        :param totalSavingCurrency:
        :return: 返回PDMTable对象
        """
        table=PDMTable(name,code,comment,totalSavingCurrency)
        self.physicalDiagram.addsymbol(name,code,u'Table',table.id)
        self.tablelist.append(table)
        return table

    def toxmlelement(self):
        """
        将包转为etree.Element对象
        :return: etree.Element对象
        """
        # 增加 o:Package
        xmlelement=etree.Element('{object}Package',nsmap=nsmapdict,Id=self.id)
        # 默认字段 , id,date等
        super(PDMPackage, self).setdefaultelement(xmlelement)
        # 增加包面板
        physicaldiag=etree.SubElement(xmlelement, "{collection}PhysicalDiagrams")
        physicaldiag.append(self.physicalDiagram.toxmlelement())
        # 指定包默认模板
        defaultdiag=etree.SubElement(xmlelement, "{collection}DefaultDiagram")
        etree.SubElement(defaultdiag, "{object}PhysicalDiagram" ,Ref=self.physicalDiagram.id)
        # c:Tables , 转换包中所有表
        if self.tablelist:
            tables=etree.SubElement(xmlelement, "{collection}Tables")
            for t in self.tablelist:
                tables.append(t.toxmlelement())
        return xmlelement

    def output(self):
        ele = self.toxmlelement()
        eletree=etree.ElementTree(ele)
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        eletree.write('1234.xml',encoding='utf-8',pretty_print=True)

if __name__ == '__main__':
    package = PDMPackage(u'测试包',u'testpackage',u'测试包')
    test = package.addtable(u'测试表',u'testtable')
    test.addcolumn(u'测试字段11', u'testcol111', u'varchar2', u'60', mandatory=True)
    test.addcolumn(u'测试字段22', u'testcol123', u'varchar2', u'60', mandatory=True)
    colid = test.getcolumnidbyname([u'testcol111', u'testcol123'], True)
    test.addindex(u'测试索引', u'testkey', colid, u'测试索引,无效字段', True)
    test.addindex(u'测试索引12', u'testindex', colid, u'测试索引,无效字段', False)
    package.output()