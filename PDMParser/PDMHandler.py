#!/usr/bin/python
# -*- coding: utf-8 -*- #

from lxml import etree

class PDMHandler(object):
    """
    路径:Model > o:RootObject > c:Children > o:Model > c:Packages > o:Package > c:Tables > o:Table
    """
    def __init__(self,pdmfilename):
        self.pdmtree = etree.parse(pdmfilename)
        self.root = self.pdmtree.getroot()
        self.model = self.pdmtree.xpath('//o:Model',namespaces=self.root.nsmap)[0]

    def getallpackages(self):
        print self.model.nsmap
        packages = self.model.xpath('//c:Packages', namespaces=self.model.nsmap)[0]
        packagelist = packages.getchildren()
        packagelist[len(packagelist)-1].addnext()

    def addpackage(self):
        pass

    def output(self):
        model = self.pdmtree.xpath('//o:Model',namespaces=self.root.nsmap)[0]
        packages = model.xpath('//c:Packages',namespaces=model.nsmap)[0]
        # packagelist=packages.getchildren()
        # print model.nsmap
        # for pkg in packagelist:
        #     for ele in pkg.getchildren():
        #         if ele.tag == '{%s}Tables' % model.nsmap['c']:
        #             for tab in ele.getchildren():
        #                 print tab.tag , tab.get('Id')
        #                 for attr in tab.getchildren():
        #                     print attr.tag,attr.text


    def writefile(self):
        self.pdmtree.write('test.pdm',encoding='utf-8',method='xml')

if __name__ == '__main__':
    # pdmhandler=PDMHandler('HTCRM_CRM实时开户数据模型.pdm')
    pdmhandler = PDMHandler('ModelTemplate - 副本2.pdm')
    pdmhandler.getallpackages()
    # pdmhandler.writefile()