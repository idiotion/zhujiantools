#!/usr/bin/python
# -*- coding: utf-8 -*- #

from PubMethod import PubItem,nsmapdict
import os
from lxml import etree
import PDMSymbol

class PDMPhysicalDiagram(PubItem):
    def __init__(self,name,code,comment=None):
        super(PDMPhysicalDiagram,self).__init__(name,code,comment)
        self.DisplayPreferences=u"""[DisplayPreferences]

[DisplayPreferences\PDM]

[DisplayPreferences\General]
Adjust to text=Yes
Snap Grid=No
Constrain Labels=Yes
Display Grid=No
Show Page Delimiter=Yes
Show Links intersections=No
Activate automatic link routing=No
Grid size=0
Graphic unit=2
Window color=255, 255, 255
Background image=
Background mode=8
Watermark image=
Watermark mode=8
Show watermark on screen=No
Gradient mode=0
Gradient end color=255, 255, 255
Show Swimlane=No
SwimlaneVert=Yes
TreeVert=No
CompDark=0

[DisplayPreferences\Object]
Show Icon=No
Mode=2
Trunc Length=40
Word Length=40
Word Text=!&quot;#$%&amp;&#39;)*+,-./:;=&gt;?@\]^_`|}~
Shortcut IntIcon=Yes
Shortcut IntLoct=Yes
Shortcut IntFullPath=No
Shortcut IntLastPackage=Yes
Shortcut ExtIcon=Yes
Shortcut ExtLoct=No
Shortcut ExtFullPath=No
Shortcut ExtLastPackage=Yes
Shortcut ExtIncludeModl=Yes
EObjShowStrn=Yes
ExtendedObject.Comment=No
ExtendedObject.IconPicture=No
ExtendedObject.TextStyle=No
ExtendedObject_SymbolLayout=&lt;Form&gt;[CRLF] &lt;StandardAttribute Name=&quot;Stereotype&quot; Attribute=&quot;Stereotype&quot; Prefix=&quot;&amp;lt;&amp;lt;&quot; Suffix=&quot;&amp;gt;&amp;gt;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;StandardAttribute Name=&quot;Object Name&quot; Attribute=&quot;DisplayName&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;Yes&quot; /&gt;[CRLF] &lt;Separator Name=&quot;Separator&quot; /&gt;[CRLF] &lt;StandardAttribute Name=&quot;Comment&quot; Attribute=&quot;Comment&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;LEFT&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;StandardAttribute Name=&quot;Icon&quot; Attribute=&quot;IconPicture&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;Yes&quot; /&gt;[CRLF] &lt;StandardAttribute Name=&quot;Force top align&quot; Attribute=&quot;TextStyle&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;Yes&quot; /&gt;[CRLF]&lt;/Form&gt;
ELnkShowStrn=Yes
ELnkShowName=Yes
ExtendedLink_SymbolLayout=&lt;Form&gt;[CRLF] &lt;Form Name=&quot;Center&quot; &gt;[CRLF]  &lt;StandardAttribute Name=&quot;Stereotype&quot; Attribute=&quot;Stereotype&quot; Prefix=&quot;&amp;lt;&amp;lt;&quot; Suffix=&quot;&amp;gt;&amp;gt;&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF]  &lt;StandardAttribute Name=&quot;Name&quot; Attribute=&quot;DisplayName&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;/Form&gt;[CRLF] &lt;Form Name=&quot;Source&quot; &gt;[CRLF] &lt;/Form&gt;[CRLF] &lt;Form Name=&quot;Destination&quot; &gt;[CRLF] &lt;/Form&gt;[CRLF]&lt;/Form&gt;
FileObject.Stereotype=No
FileObject.DisplayName=Yes
FileObject.LocationOrName=No
FileObject.IconPicture=No
FileObject.TextStyle=No
FileObject.IconMode=Yes
FileObject_SymbolLayout=&lt;Form&gt;[CRLF] &lt;StandardAttribute Name=&quot;Stereotype&quot; Attribute=&quot;Stereotype&quot; Prefix=&quot;&amp;lt;&amp;lt;&quot; Suffix=&quot;&amp;gt;&amp;gt;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;ExclusiveChoice Name=&quot;Exclusive Choice&quot; Mandatory=&quot;Yes&quot; Display=&quot;HorizontalRadios&quot; &gt;[CRLF]  &lt;StandardAttribute Name=&quot;Name&quot; Attribute=&quot;DisplayName&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF]  &lt;StandardAttribute Name=&quot;Location&quot; Attribute=&quot;LocationOrName&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;/ExclusiveChoice&gt;[CRLF] &lt;StandardAttribute Name=&quot;Icon&quot; Attribute=&quot;IconPicture&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;Yes&quot; /&gt;[CRLF] &lt;StandardAttribute Name=&quot;Force top align&quot; Attribute=&quot;TextStyle&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;Yes&quot; /&gt;[CRLF]&lt;/Form&gt;
Package.Stereotype=Yes
Package.Comment=No
Package.IconPicture=No
Package.TextStyle=No
Package_SymbolLayout=&lt;Form&gt;[CRLF] &lt;StandardAttribute Name=&quot;Stereotype&quot; Attribute=&quot;Stereotype&quot; Prefix=&quot;&amp;lt;&amp;lt;&quot; Suffix=&quot;&amp;gt;&amp;gt;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;StandardAttribute Name=&quot;Name&quot; Attribute=&quot;DisplayName&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;Yes&quot; /&gt;[CRLF] &lt;Separator Name=&quot;Separator&quot; /&gt;[CRLF] &lt;StandardAttribute Name=&quot;Comment&quot; Attribute=&quot;Comment&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;LEFT&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;StandardAttribute Name=&quot;Icon&quot; Attribute=&quot;IconPicture&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;Yes&quot; /&gt;[CRLF] &lt;StandardAttribute Name=&quot;Force top align&quot; Attribute=&quot;TextStyle&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;Yes&quot; /&gt;[CRLF]&lt;/Form&gt;
Display Model Version=Yes
Table.Stereotype=Yes
Table.DisplayName=Yes
Table.OwnerDisplayName=No
Table.Columns=Yes
Table.Columns._Filter=&quot;All Columns&quot; PDMCOLNALL
Table.Columns._Columns=Stereotype DataType KeyIndicator
Table.Columns._Limit=-5
Table.Keys=No
Table.Keys._Columns=Stereotype Indicator
Table.Indexes=No
Table.Indexes._Columns=Stereotype
Table.Triggers=No
Table.Triggers._Columns=Stereotype
Table.Comment=No
Table.IconPicture=No
Table.TextStyle=No
Table_SymbolLayout=&lt;Form&gt;[CRLF] &lt;StandardAttribute Name=&quot;Stereotype&quot; Attribute=&quot;Stereotype&quot; Prefix=&quot;&amp;lt;&amp;lt;&quot; Suffix=&quot;&amp;gt;&amp;gt;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;ExclusiveChoice Name=&quot;Exclusive Choice&quot; Mandatory=&quot;Yes&quot; Display=&quot;HorizontalRadios&quot; &gt;[CRLF]  &lt;StandardAttribute Name=&quot;Name&quot; Attribute=&quot;DisplayName&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF]  &lt;StandardAttribute Name=&quot;Owner and Name&quot; Attribute=&quot;OwnerDisplayName&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;/ExclusiveChoice&gt;[CRLF] &lt;Separator Name=&quot;Separator&quot; /&gt;[CRLF] &lt;StandardCollection Name=&quot;Columns&quot; Collection=&quot;Columns&quot; Columns=&quot;Stereotype No\r\nDisplayName Yes\r\nDataType No\r\nSymbolDataType No &amp;quot;Domain or Data type&amp;quot;\r\nDomain No\r\nKeyIndicator No\r\nIndexIndicator No\r\nNullStatus No&quot; Filters=&quot;&amp;quot;All Columns&amp;quot;  PDMCOLNALL &amp;quot;&amp;quot;\r\n&amp;quot;PK Columns&amp;quot;  PDMCOLNPK &amp;quot;\&amp;quot;PRIM \&amp;quot;TRUE\&amp;quot; TRUE\&amp;quot;&amp;quot;\r\n&amp;quot;Key Columns&amp;quot;  PDMCOLNKEY &amp;quot;\&amp;quot;KEYS \&amp;quot;TRUE\&amp;quot; TRUE\&amp;quot;&amp;quot;&quot; HasLimit=&quot;Yes&quot; HideEmpty=&quot;No&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;StandardCollection Name=&quot;Keys&quot; Collection=&quot;Keys&quot; Columns=&quot;Stereotype No\r\nDisplayName Yes\r\nIndicator No&quot; HasLimit=&quot;No&quot; HideEmpty=&quot;No&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;StandardCollection Name=&quot;Indexes&quot; Collection=&quot;Indexes&quot; Columns=&quot;Stereotype No\r\nDisplayName Yes\r\nIndicator No&quot; HasLimit=&quot;No&quot; HideEmpty=&quot;No&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;StandardCollection Name=&quot;Triggers&quot; Collection=&quot;Triggers&quot; Columns=&quot;Stereotype No\r\nDisplayName Yes&quot; HasLimit=&quot;No&quot; HideEmpty=&quot;No&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;StandardAttribute Name=&quot;Comment&quot; Attribute=&quot;Comment&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;LEFT&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;StandardAttribute Name=&quot;Icon&quot; Attribute=&quot;IconPicture&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;Yes&quot; /&gt;[CRLF] &lt;StandardAttribute Name=&quot;Force top align&quot; Attribute=&quot;TextStyle&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;Yes&quot; /&gt;[CRLF]&lt;/Form&gt;
View.Stereotype=Yes
View.DisplayName=Yes
View.OwnerDisplayName=No
View.Columns=Yes
View.Columns._Columns=DisplayName
View.Columns._Limit=-5
View.TemporaryVTables=Yes
View.Indexes=No
View.Comment=No
View.IconPicture=No
View.TextStyle=No
View_SymbolLayout=&lt;Form&gt;[CRLF] &lt;StandardAttribute Name=&quot;Stereotype&quot; Attribute=&quot;Stereotype&quot; Prefix=&quot;&amp;lt;&amp;lt;&quot; Suffix=&quot;&amp;gt;&amp;gt;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;ExclusiveChoice Name=&quot;Exclusive Choice&quot; Mandatory=&quot;Yes&quot; Display=&quot;HorizontalRadios&quot; &gt;[CRLF]  &lt;StandardAttribute Name=&quot;Name&quot; Attribute=&quot;DisplayName&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF]  &lt;StandardAttribute Name=&quot;Owner and Name&quot; Attribute=&quot;OwnerDisplayName&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;/ExclusiveChoice&gt;[CRLF] &lt;Separator Name=&quot;Separator&quot; /&gt;[CRLF] &lt;StandardCollection Name=&quot;Columns&quot; Collection=&quot;Columns&quot; Columns=&quot;DisplayName No\r\nExpression No\r\nDataType No\r\nSymbolDataType No &amp;quot;Domain or Data type&amp;quot;\r\nIndexIndicator No&quot; HasLimit=&quot;Yes&quot; HideEmpty=&quot;No&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;StandardCollection Name=&quot;Tables&quot; Collection=&quot;TemporaryVTables&quot; Columns=&quot;Name Yes&quot; HasLimit=&quot;No&quot; HideEmpty=&quot;No&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;StandardCollection Name=&quot;Indexes&quot; Collection=&quot;Indexes&quot; Columns=&quot;DisplayName Yes&quot; HasLimit=&quot;No&quot; HideEmpty=&quot;No&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;StandardAttribute Name=&quot;Comment&quot; Attribute=&quot;Comment&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;LEFT&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;StandardAttribute Name=&quot;Icon&quot; Attribute=&quot;IconPicture&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;Yes&quot; /&gt;[CRLF] &lt;StandardAttribute Name=&quot;Force top align&quot; Attribute=&quot;TextStyle&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;Yes&quot; /&gt;[CRLF]&lt;/Form&gt;
Procedure.Stereotype=No
Procedure.DisplayName=Yes
Procedure.OwnerDisplayName=No
Procedure.Comment=No
Procedure.IconPicture=No
Procedure.TextStyle=No
Procedure_SymbolLayout=&lt;Form&gt;[CRLF] &lt;StandardAttribute Name=&quot;Stereotype&quot; Attribute=&quot;Stereotype&quot; Prefix=&quot;&amp;lt;&amp;lt;&quot; Suffix=&quot;&amp;gt;&amp;gt;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;ExclusiveChoice Name=&quot;Exclusive Choice&quot; Mandatory=&quot;Yes&quot; Display=&quot;HorizontalRadios&quot; &gt;[CRLF]  &lt;StandardAttribute Name=&quot;Name&quot; Attribute=&quot;DisplayName&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF]  &lt;StandardAttribute Name=&quot;Owner and Name&quot; Attribute=&quot;OwnerDisplayName&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;/ExclusiveChoice&gt;[CRLF] &lt;Separator Name=&quot;Separator&quot; /&gt;[CRLF] &lt;StandardAttribute Name=&quot;Comment&quot; Attribute=&quot;Comment&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;LEFT&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;StandardAttribute Name=&quot;Icon&quot; Attribute=&quot;IconPicture&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;Yes&quot; /&gt;[CRLF] &lt;StandardAttribute Name=&quot;Force top align&quot; Attribute=&quot;TextStyle&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Alignment=&quot;CNTR&quot; Caption=&quot;&quot; Mandatory=&quot;Yes&quot; /&gt;[CRLF]&lt;/Form&gt;
Reference.Cardinality=No
Reference.ImplementationType=No
Reference.ChildRole=Yes
Reference.Stereotype=Yes
Reference.DisplayName=No
Reference.ForeignKeyConstraintName=No
Reference.JoinExpression=No
Reference.Integrity=No
Reference.ParentRole=Yes
Reference_SymbolLayout=&lt;Form&gt;[CRLF] &lt;Form Name=&quot;Source&quot; &gt;[CRLF]  &lt;StandardAttribute Name=&quot;Cardinality&quot; Attribute=&quot;Cardinality&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF]  &lt;StandardAttribute Name=&quot;Implementation&quot; Attribute=&quot;ImplementationType&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF]  &lt;StandardAttribute Name=&quot;Child Role&quot; Attribute=&quot;ChildRole&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;/Form&gt;[CRLF] &lt;Form Name=&quot;Center&quot; &gt;[CRLF]  &lt;StandardAttribute Name=&quot;Stereotype&quot; Attribute=&quot;Stereotype&quot; Prefix=&quot;&amp;lt;&amp;lt;&quot; Suffix=&quot;&amp;gt;&amp;gt;&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF]  &lt;ExclusiveChoice Name=&quot;Exclusive Choice&quot; Mandatory=&quot;No&quot; Display=&quot;HorizontalRadios&quot; &gt;[CRLF]   &lt;StandardAttribute Name=&quot;Name&quot; Attribute=&quot;DisplayName&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF]   &lt;StandardAttribute Name=&quot;Cons&amp;amp;traint Name&quot; Attribute=&quot;ForeignKeyConstraintName&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Caption=&quot;Cons&amp;amp;traint Name&quot; Mandatory=&quot;No&quot; /&gt;[CRLF]   &lt;StandardAttribute Name=&quot;Join&quot; Attribute=&quot;JoinExpression&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Caption=&quot;Join&quot; Mandatory=&quot;No&quot; /&gt;[CRLF]  &lt;/ExclusiveChoice&gt;[CRLF]  &lt;StandardAttribute Name=&quot;Referential integrity&quot; Attribute=&quot;Integrity&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Caption=&quot;Referential integrity&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;/Form&gt;[CRLF] &lt;Form Name=&quot;Destination&quot; &gt;[CRLF]  &lt;StandardAttribute Name=&quot;Parent Role&quot; Attribute=&quot;ParentRole&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;/Form&gt;[CRLF]&lt;/Form&gt;
ViewReference.ChildRole=Yes
ViewReference.Stereotype=Yes
ViewReference.DisplayName=No
ViewReference.JoinExpression=No
ViewReference.ParentRole=Yes
ViewReference_SymbolLayout=&lt;Form&gt;[CRLF] &lt;Form Name=&quot;Source&quot; &gt;[CRLF]  &lt;StandardAttribute Name=&quot;Child Role&quot; Attribute=&quot;ChildRole&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;/Form&gt;[CRLF] &lt;Form Name=&quot;Center&quot; &gt;[CRLF]  &lt;StandardAttribute Name=&quot;Stereotype&quot; Attribute=&quot;Stereotype&quot; Prefix=&quot;&amp;lt;&amp;lt;&quot; Suffix=&quot;&amp;gt;&amp;gt;&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF]  &lt;ExclusiveChoice Name=&quot;Exclusive Choice&quot; Mandatory=&quot;No&quot; Display=&quot;HorizontalRadios&quot; &gt;[CRLF]   &lt;StandardAttribute Name=&quot;Name&quot; Attribute=&quot;DisplayName&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF]   &lt;StandardAttribute Name=&quot;Join Expression&quot; Attribute=&quot;JoinExpression&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF]  &lt;/ExclusiveChoice&gt;[CRLF] &lt;/Form&gt;[CRLF] &lt;Form Name=&quot;Destination&quot; &gt;[CRLF]  &lt;StandardAttribute Name=&quot;Parent Role&quot; Attribute=&quot;ParentRole&quot; Prefix=&quot;&quot; Suffix=&quot;&quot; Caption=&quot;&quot; Mandatory=&quot;No&quot; /&gt;[CRLF] &lt;/Form&gt;[CRLF]&lt;/Form&gt;

[DisplayPreferences\Symbol]

[DisplayPreferences\Symbol\FRMEOBJ]
STRNFont=新宋体,8,N
STRNFont color=0, 0, 0
DISPNAMEFont=新宋体,8,N
DISPNAMEFont color=0, 0, 0
LABLFont=新宋体,8,N
LABLFont color=0, 0, 0
AutoAdjustToText=Yes
Keep aspect=No
Keep center=No
Keep size=No
Width=6000
Height=2000
Brush color=255 255 255
Fill Color=Yes
Brush style=6
Brush bitmap mode=12
Brush gradient mode=64
Brush gradient color=192 192 192
Brush background image=
Custom shape=
Custom text mode=0
Pen=1 0 255 128 128
Shadow color=192 192 192
Shadow=0

[DisplayPreferences\Symbol\FRMELNK]
CENTERFont=新宋体,8,N
CENTERFont color=0, 0, 0
Line style=1
AutoAdjustToText=Yes
Keep aspect=No
Keep center=No
Keep size=No
Brush color=255 255 255
Fill Color=Yes
Brush style=1
Brush bitmap mode=12
Brush gradient mode=0
Brush gradient color=118 118 118
Brush background image=
Custom shape=
Custom text mode=0
Pen=1 0 128 128 255
Shadow color=192 192 192
Shadow=0

[DisplayPreferences\Symbol\FILO]
OBJSTRNFont=新宋体,8,N
OBJSTRNFont color=0, 0, 0
DISPNAMEFont=新宋体,8,N
DISPNAMEFont color=0, 0, 0
LCNMFont=新宋体,8,N
LCNMFont color=0, 0, 0
AutoAdjustToText=Yes
Keep aspect=No
Keep center=No
Keep size=No
Width=4800
Height=3600
Brush color=255 255 255
Fill Color=Yes
Brush style=1
Brush bitmap mode=12
Brush gradient mode=0
Brush gradient color=118 118 118
Brush background image=
Custom shape=
Custom text mode=0
Pen=1 0 0 0 255
Shadow color=192 192 192
Shadow=0

[DisplayPreferences\Symbol\PDMPCKG]
STRNFont=新宋体,8,N
STRNFont color=0, 0, 0
DISPNAMEFont=新宋体,8,N
DISPNAMEFont color=0, 0, 0
LABLFont=新宋体,8,N
LABLFont color=0, 0, 0
AutoAdjustToText=Yes
Keep aspect=No
Keep center=No
Keep size=No
Width=4800
Height=4000
Brush color=255 255 192
Fill Color=Yes
Brush style=6
Brush bitmap mode=12
Brush gradient mode=65
Brush gradient color=255 255 255
Brush background image=
Custom shape=
Custom text mode=0
Pen=1 0 178 178 178
Shadow color=192 192 192
Shadow=0

[DisplayPreferences\Symbol\TABL]
STRNFont=新宋体,8,N
STRNFont color=0, 0, 0
DISPNAMEFont=新宋体,8,N
DISPNAMEFont color=0, 0, 0
OWNRDISPNAMEFont=新宋体,8,N
OWNRDISPNAMEFont color=0, 0, 0
ColumnsFont=新宋体,8,N
ColumnsFont color=0, 0, 0
TablePkColumnsFont=新宋体,8,U
TablePkColumnsFont color=0, 0, 0
TableFkColumnsFont=新宋体,8,N
TableFkColumnsFont color=0, 0, 0
KeysFont=新宋体,8,N
KeysFont color=0, 0, 0
IndexesFont=新宋体,8,N
IndexesFont color=0, 0, 0
TriggersFont=新宋体,8,N
TriggersFont color=0, 0, 0
LABLFont=新宋体,8,N
LABLFont color=0, 0, 0
AutoAdjustToText=Yes
Keep aspect=No
Keep center=No
Keep size=No
Width=4800
Height=4000
Brush color=178 214 252
Fill Color=Yes
Brush style=6
Brush bitmap mode=12
Brush gradient mode=65
Brush gradient color=255 255 255
Brush background image=
Custom shape=
Custom text mode=0
Pen=1 0 0 128 192
Shadow color=192 192 192
Shadow=0

[DisplayPreferences\Symbol\VIEW]
STRNFont=新宋体,8,N
STRNFont color=0, 0, 0
DISPNAMEFont=新宋体,8,N
DISPNAMEFont color=0, 0, 0
OWNRDISPNAMEFont=新宋体,8,N
OWNRDISPNAMEFont color=0, 0, 0
ColumnsFont=新宋体,8,N
ColumnsFont color=0, 0, 0
TablePkColumnsFont=新宋体,8,U
TablePkColumnsFont color=0, 0, 0
TableFkColumnsFont=新宋体,8,N
TableFkColumnsFont color=0, 0, 0
TemporaryVTablesFont=新宋体,8,N
TemporaryVTablesFont color=0, 0, 0
IndexesFont=新宋体,8,N
IndexesFont color=0, 0, 0
LABLFont=新宋体,8,N
LABLFont color=0, 0, 0
AutoAdjustToText=Yes
Keep aspect=No
Keep center=No
Keep size=No
Width=4800
Height=4000
Brush color=208 208 255
Fill Color=Yes
Brush style=6
Brush bitmap mode=12
Brush gradient mode=65
Brush gradient color=255 255 255
Brush background image=
Custom shape=
Custom text mode=0
Pen=1 0 128 128 192
Shadow color=192 192 192
Shadow=0

[DisplayPreferences\Symbol\PROC]
STRNFont=新宋体,8,N
STRNFont color=0, 0, 0
DISPNAMEFont=新宋体,8,N
DISPNAMEFont color=0, 0, 0
OWNRDISPNAMEFont=新宋体,8,N
OWNRDISPNAMEFont color=0, 0, 0
LABLFont=新宋体,8,N
LABLFont color=0, 0, 0
AutoAdjustToText=Yes
Keep aspect=No
Keep center=No
Keep size=No
Width=4000
Height=1000
Brush color=255 255 192
Fill Color=Yes
Brush style=6
Brush bitmap mode=12
Brush gradient mode=65
Brush gradient color=255 255 255
Brush background image=
Custom shape=
Custom text mode=0
Pen=1 0 128 108 0
Shadow color=192 192 192
Shadow=0

[DisplayPreferences\Symbol\REFR]
SOURCEFont=新宋体,8,N
SOURCEFont color=0, 0, 0
CENTERFont=新宋体,8,N
CENTERFont color=0, 0, 0
DESTINATIONFont=新宋体,8,N
DESTINATIONFont color=0, 0, 0
Line style=1
AutoAdjustToText=Yes
Keep aspect=No
Keep center=No
Keep size=No
Brush color=255 255 255
Fill Color=Yes
Brush style=1
Brush bitmap mode=12
Brush gradient mode=0
Brush gradient color=118 118 118
Brush background image=
Custom shape=
Custom text mode=0
Pen=1 0 0 128 192
Shadow color=192 192 192
Shadow=0

[DisplayPreferences\Symbol\VREF]
SOURCEFont=新宋体,8,N
SOURCEFont color=0, 0, 0
CENTERFont=新宋体,8,N
CENTERFont color=0, 0, 0
DESTINATIONFont=新宋体,8,N
DESTINATIONFont color=0, 0, 0
Line style=1
AutoAdjustToText=Yes
Keep aspect=No
Keep center=No
Keep size=No
Brush color=255 255 255
Fill Color=Yes
Brush style=1
Brush bitmap mode=12
Brush gradient mode=0
Brush gradient color=118 118 118
Brush background image=
Custom shape=
Custom text mode=0
Pen=1 0 128 128 192
Shadow color=192 192 192
Shadow=0

[DisplayPreferences\Symbol\\USRDEPD]
OBJXSTRFont=新宋体,8,N
OBJXSTRFont color=0, 0, 0
Line style=1
AutoAdjustToText=Yes
Keep aspect=No
Keep center=No
Keep size=No
Brush color=255 255 255
Fill Color=Yes
Brush style=1
Brush bitmap mode=12
Brush gradient mode=0
Brush gradient color=118 118 118
Brush background image=
Custom shape=
Custom text mode=0
Pen=2 0 128 128 255
Shadow color=192 192 192
Shadow=0

[DisplayPreferences\Symbol\Free Symbol]
Free TextFont=新宋体,8,N
Free TextFont color=0, 0, 0
Line style=0
AutoAdjustToText=Yes
Keep aspect=No
Keep center=No
Keep size=No
Brush color=255 255 255
Fill Color=Yes
Brush style=1
Brush bitmap mode=12
Brush gradient mode=0
Brush gradient color=118 118 118
Brush background image=
Custom shape=
Custom text mode=0
Pen=1 0 0 0 255
Shadow color=192 192 192
Shadow=0"""
        self.PaperSize=u'(8268, 11693)'
        self.PageMargins=u'((315,354), (433,354))'
        self.PageOrientation=u'1'
        self.PaperSource=u'7'
        self.symbollist=[]
        self.id=self.getidno()

    def addsymbol(self,name,code,symboltype,childid,comment=None):
        symbol=PDMSymbol.PDMSymbol(name,code,symboltype,childid,comment)
        self.symbollist.append(symbol)

    def toxmlelement(self):
        if not self.symbollist:
            return
        xmlelement=etree.Element('{object}PhysicalDiagram',nsmap=nsmapdict,Id=self.id)
        super(PDMPhysicalDiagram, self).setdefaultelement(xmlelement)
        etree.SubElement(xmlelement,"{attribute}DisplayPreferences").text=self.DisplayPreferences
        etree.SubElement(xmlelement, "{attribute}PaperSize").text = self.PaperSize
        etree.SubElement(xmlelement, "{attribute}PageMargins").text = self.PageMargins
        etree.SubElement(xmlelement, "{attribute}PageOrientation").text = self.PageOrientation
        etree.SubElement(xmlelement, "{attribute}PaperSource").text = self.PaperSource
        symbols=etree.SubElement(xmlelement, "{collection}Symbols")
        for symbol in self.symbollist:
            symbols.append(symbol.toxmlelement())
        return xmlelement

    def output(self):
        ele = self.toxmlelement()
        eletree=etree.ElementTree(ele)
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        eletree.write('1234.xml',encoding='utf-8',pretty_print=True)

if __name__ == '__main__':
    test = PDMPhysicalDiagram(u'测试板面',u'testdiagram')
    test.addtablesymbol(u'测试标签',u'testsymbol',test.getidno())
    test.output()