#!/usr/bin/python
# -*- coding: utf-8 -*- #

from PubMethod import PubItem,nsmapdict
import os
from lxml import etree
import PDMColumn
import PDMKey
import PDMIndex

class PDMTable(PubItem):
    def __init__(self,name ,code ,comment=None ,totalSavingCurrency=None):
        super(PDMTable,self).__init__(name,code,comment)
        self.totalSavingCurrency = totalSavingCurrency
        self.comment = comment
        self.columnlist=[]
        self.keylist=[]
        self.indexlist=[]
        self.id=self.getidno()

    def addcolumn(self,name,code,dataType,length,comment=None,defaultvalue=None,mandatory=False):
        """
        表增加字段
        :param name:      字段中文名
        :param code:      字段英文名
        :param dataType:  字段类型
        :param length:    长度
        :param comment:   字段注释
        :param defaultvalue: 默认段
        :param mandatory:  是否不可为空 , True | False
        :return: 返回PDMColumn.PDMColumn对象
        """
        column=PDMColumn.PDMColumn(name,code,dataType,length,comment,defaultvalue,mandatory)
        self.columnlist.append(column)

    def getcolumnidbyname(self,columncodelist,primarykey=False):
        columncodelist = [x.upper() for x in columncodelist]
        columnid=[]
        for colcode in columncodelist:
            colid=None
            for col in self.columnlist:
                if colcode == col.code.upper():
                    if col.mandatory=='0':
                        raise Exception('表[{0}]主键字段{1}必须非空!'.format(self.name.encode('utf-8'),colcode.encode('utf-8')))
                    colid=col.id
            if colid is None:
                raise Exception('表[{0}]中不存在字段[{1}]'.format(self.name.encode('utf-8'), colcode.encode('utf-8')))
            columnid.append(colid)
        return columnid

    #一个表只支持一个key
    def addindex(self,name,code,columnidlist=[] ,comment=None,indextype='N'):
        if indextype not in ('N','P','U'):
            raise Exception("非法的索引类型[{0}],只支持('N','P','U')".format(indextype.decode('utf-8')))
        if indextype=='P':
            if self.keylist:
                raise Exception('[{0}]增加key出错,目前一个表只支持一个key!'.format(self.name.encode('utf-8')))
            index = PDMKey.PDMKey(name, code, columnidlist, comment)
            self.keylist.append(index)
        else:
            unique= True if indextype=='U' else False
            index=PDMIndex.PDMIndex(name,code,columnidlist,comment,unique)
            self.indexlist.append(index)

    def toxmlelement(self):
        """表,字段,主键,索引已经支持!"""
        xmlelement=etree.Element('{object}Table',nsmap=nsmapdict,Id=self.id)
        super(PDMTable, self).setdefaultelement(xmlelement)
        etree.SubElement(xmlelement, "{attribute}TotalSavingCurrency").text = self.totalSavingCurrency

        if len(self.columnlist)>0:
            columnelement=etree.SubElement(xmlelement, "{collection}Columns")
            for col in self.columnlist:
                columnelement.append(col.toxmlelement())

        if len(self.indexlist)>0:
            indexelement=etree.SubElement(xmlelement, "{collection}Indexes")
            for index in self.indexlist:
                indexelement.append(index.toxmlelement())

        if len(self.keylist)>0:
            keyelement=etree.SubElement(xmlelement, "{collection}Keys")
            for key in self.keylist:
                keyelement.append(key.toxmlelement())
                primarykey=etree.SubElement(xmlelement, "{collection}PrimaryKey")
                etree.SubElement(primarykey,"{object}Key",Ref=key.id)
        return xmlelement

    def output(self):
        ele = self.toxmlelement()
        eletree=etree.ElementTree(ele)
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        eletree.write('1234.xml',encoding='utf-8',pretty_print=True)

if __name__ == '__main__':
    test = PDMTable(u'测试表名21122',u'testtable222222',u'测试表名TTT')
    test.addcolumn( u'测试字段11', u'testcol111', u'varchar2', u'60',mandatory=True)
    test.addcolumn(u'测试字段22', u'testcol123', u'varchar2', u'60',mandatory=True)
    colid=test.getcolumnidbyname([u'testcol111',u'testcol123'],True)
    test.addindex(u'测试索引', u'testkey', colid, u'测试索引,无效字段',u'P')
    test.addindex(u'测试索引12', u'testindex', colid, u'测试索引,无效字段', u'U')
    test.output()