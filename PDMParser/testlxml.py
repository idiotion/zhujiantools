#!/usr/bin/python
# -*- coding: utf-8 -*- #

from lxml import etree, objectify
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

E = objectify.ElementMaker(annotate=False)
anno_tree = E.annotation(
    E.folder('VOC2014_instance'),
    E.filename("test.jpg"),
    E.source(
        E.database('COCO'),
        E.annotation('COCO'),
        E.image('COCO'),
        E.url("http://test.jpg")
    ),
    E.size(
        E.width(800),
        E.height(600),
        E.depth(3)
    ),
    E.segmented(0),
)

etree.ElementTree(anno_tree).write("text.xml", pretty_print=False)

E2 = objectify.ElementMaker(annotate=False)
anno_tree2 = E2.object(
    E.name("person"),
    E.bndbox(
        E.xmin(100),
        E.ymin(200),
        E.xmax(300),
        E.ymax(400)
    ),
    E.difficult(0)
)
anno_tree.append(anno_tree2)

annotation = etree.Element("annotation")
etree.SubElement(annotation, "folder").text = "VOC2014_instance12"
etree.SubElement(annotation, "filename").text = "test.jpg"
source = etree.SubElement(annotation, "source")
etree.SubElement(source, "database").text = "COCO"
etree.SubElement(source, "annotation").text = "COCO"
etree.SubElement(source, "image").text = "COCO"
etree.SubElement(source, "url").text = "http://test1.jpg"
size = etree.SubElement(annotation, "size")
etree.SubElement(size, "width").text ='800'  # 必须用string
etree.SubElement(size, "height").text = '600'
etree.SubElement(size, "depth").text = '3'
etree.SubElement(annotation, "segmented").text = '0'
key_object = etree.SubElement(annotation, "object")
etree.SubElement(key_object, "name").text = 'person'
bndbox = etree.SubElement(key_object, "bndbox")
etree.SubElement(bndbox, "xmin").text = str(100)
etree.SubElement(bndbox, "ymin").text = str(200)
etree.SubElement(bndbox, "xmax").text = str(300)
etree.SubElement(bndbox, "ymax").text = str(400)
etree.SubElement(key_object, "difficult").text = '0'
doc = etree.ElementTree(annotation)
doc.write(open("text.xml", "w"), pretty_print=True)