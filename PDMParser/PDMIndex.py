#!/usr/bin/python
# -*- coding: utf-8 -*- #

from PubMethod import PubItem,nsmapdict
import os
from lxml import etree

class PDMIndex(PubItem):
    def __init__(self,name ,code ,columnidlist=[] ,comment=None):
        super(PDMIndex,self).__init__(name,code,comment)
        self.columnidlist = columnidlist
        self.id=self.getidno()

    def toxmlelement(self):
        if not self.columnidlist:
            return
        xmlelement=etree.Element('{object}Index',nsmap=nsmapdict,Id=self.id)
        super(PDMIndex, self).setdefaultelement(xmlelement)
        indexcolumns=etree.SubElement(xmlelement, "{collection}IndexColumns")
        for col in self.columnidlist:
            indexcolumnobjectid='objid{0}'.format(self.getidno())
            indexcolumn=PubItem(indexcolumnobjectid,None,None)
            indexelement=etree.SubElement(indexcolumns,'{object}IndexColumn',Id=self.id)
            indexcolumn.setdefaultelement(indexelement)
            columns=etree.SubElement(indexelement, "{collection}Column")
            etree.SubElement(columns,'{object}Column',Ref=col)
        return xmlelement

    def output(self):
        ele = self.toxmlelement()
        eletree=etree.ElementTree(ele)
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        eletree.write('1234.xml',encoding='utf-8',pretty_print=True)

if __name__ == '__main__':
    test = PDMIndex(u'测试索引',u'testkey',['o12','o13','o14'])
    test.output()