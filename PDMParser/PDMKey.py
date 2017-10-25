#!/usr/bin/python
# -*- coding: utf-8 -*- #

from PubMethod import PubItem,nsmapdict
import os
from lxml import etree

class PDMKey(PubItem):
    def __init__(self, name , code , columnidlist=[] ,comment=None):
        super(PDMKey,self).__init__(name,code,comment)
        self.columnidlist = columnidlist
        self.id=self.getidno()

    def toxmlelement(self):
        if not self.columnidlist:
            return
        xmlelement=etree.Element('{object}Key',nsmap=nsmapdict,Id=self.id)
        super(PDMKey, self).setdefaultelement(xmlelement)
        keycolumns=etree.SubElement(xmlelement, "{collection}Key.Columns")
        for col in self.columnidlist:
            etree.SubElement(keycolumns,'{object}Column',Ref=col)
        return xmlelement

    def output(self):
        ele = self.toxmlelement()
        eletree=etree.ElementTree(ele)
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        eletree.write('1234.xml',encoding='utf-8',pretty_print=True)

if __name__ == '__main__':
    test = PDMKey(u'测试索引',u'testkey',['o12','o13','o14'])
    test.output()