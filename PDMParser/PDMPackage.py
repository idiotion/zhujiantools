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
        table=PDMTable(name,code,comment,totalSavingCurrency)
        self.physicalDiagram.addsymbol(name,code,u'Table',table.id)
        self.tablelist.append(table)
        return table

    def toxmlelement(self):
        xmlelement=etree.Element('{object}Package',nsmap=nsmapdict,Id=self.id)
        super(PDMPackage, self).setdefaultelement(xmlelement)
        physicaldiag=etree.SubElement(xmlelement, "{collection}PhysicalDiagrams")
        physicaldiag.append(self.physicalDiagram.toxmlelement())
        defaultdiag=etree.SubElement(physicaldiag, "{collection}DefaultDiagram")
        etree.SubElement(defaultdiag, "{object}PhysicalDiagram" ,Ref=self.physicalDiagram.id)
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