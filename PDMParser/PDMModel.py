#!/usr/bin/python
# -*- coding: utf-8 -*- #

from PubMethod import PubItem,nsmapdict
import os,time
from lxml import etree
from PDMPhysicalDiagram import PDMPhysicalDiagram
from PDMPackage import PDMPackage

class PDMModel(PubItem):
    def __init__(self, name ,code):
        super(PDMModel,self).__init__(name,code)
        #默认赋值
        self.PackageOptionsText="""[FolderOptions]

[FolderOptions\Physical Objects]
GenerationCheckModel=Yes
GenerationPath=
GenerationOptions=
GenerationTasks=
GenerationTargets=
GenerationSelections=
RevPkey=Yes
RevFkey=Yes
RevAkey=Yes
RevCheck=Yes
RevIndx=Yes
RevOpts=Yes
RevViewAsTabl=No
RevViewOpts=Yes
RevSystAsTabl=Yes
RevTablPerm=No
RevViewPerm=No
RevProcPerm=No
RevDbpkPerm=No
RevSqncPerm=No
RevAdtPerm=No
RevUserPriv=No
RevUserOpts=No
RevGrpePriv=No
RevRolePriv=No
RevDtbsOpts=Yes
RevDtbsPerm=No
RevViewIndx=Yes
RevJidxOpts=Yes
RevStats=No
RevTspcPerm=No
RevCaseSensitive=No
GenTrgrStdMsg=Yes
GenTrgrMsgTab=
GenTrgrMsgNo=
GenTrgrMsgTxt=
TrgrPreserve=No
TrgrIns=Yes
TrgrUpd=Yes
TrgrDel=Yes
TrgrC2Ins=Yes
TrgrC2Upd=Yes
TrgrC3=Yes
TrgrC4=Yes
TrgrC5=Yes
TrgrC6=Yes
TrgrC7=Yes
TrgrC8=Yes
TrgrC9=Yes
TrgrC10=Yes
TrgrC11=Yes
TrgrC1=Yes
TrgrC12Ins=Yes
TrgrC12Upd=Yes
TrgrC13=Yes
UpdateTableStatistics=Yes
UpdateColumnStatistics=Yes

[FolderOptions\Physical Objects\Database Generation]
GenScriptName=crebas
GenScriptName0=
GenScriptName1=
GenScriptName2=
GenScriptName3=
GenScriptName4=
GenScriptName5=
GenScriptName6=
GenScriptName7=
GenScriptName8=
GenScriptName9=
GenPathName=
GenSingleFile=Yes
GenODBC=No
GenCheckModel=Yes
GenScriptPrev=Yes
GenArchiveModel=No
GenUseSync=No
GenSyncChoice=0
GenSyncArch=
GenSyncRmg=0

[FolderOptions\Physical Objects\Database Generation\Format]
GenScriptTitle=Yes
GenScriptNamLabl=No
GenScriptQDtbs=Yes
GenScriptQOwnr=Yes
GenScriptCase=0
GenScriptEncoding=ANSI
GenScriptNAcct=No
IdentifierDelimiter=&quot;

[FolderOptions\Physical Objects\Database Generation\Database]
Create=Yes
Open=Yes
Close=Yes
Drop=Yes
Permission=No

[FolderOptions\Physical Objects\Database Generation\Database\Create]
Physical Options=Yes
Header=Yes
Footer=Yes

[FolderOptions\Physical Objects\Database Generation\Tablespace]
Create=Yes
Drop=Yes
Comment=Yes
Permission=No

[FolderOptions\Physical Objects\Database Generation\Tablespace\Create]
Header=Yes
Footer=Yes

[FolderOptions\Physical Objects\Database Generation\Storage]
Create=Yes
Drop=Yes
Comment=Yes

[FolderOptions\Physical Objects\Database Generation\\User]
Create=Yes
Drop=Yes
Comment=Yes
Privilege=No

[FolderOptions\Physical Objects\Database Generation\\User\Create]
Physical Options=No

[FolderOptions\Physical Objects\Database Generation\Group]
Create=Yes
Drop=Yes
Comment=Yes
Privilege=No

[FolderOptions\Physical Objects\Database Generation\Role]
Create=Yes
Drop=Yes
Privilege=No

[FolderOptions\Physical Objects\Database Generation\\UserDefinedDataType]
Create=Yes
Comment=Yes
Drop=Yes

[FolderOptions\Physical Objects\Database Generation\\UserDefinedDataType\Create]
Default value=Yes
Check=Yes

[FolderOptions\Physical Objects\Database Generation\AbstractDataType]
Create=Yes
Header=Yes
Footer=Yes
Drop=Yes
Comment=Yes
Install JAVA class=Yes
Remove JAVA class=Yes
Permission=No

[FolderOptions\Physical Objects\Database Generation\Rule]
Create=Yes
Drop=Yes
Comment=Yes

[FolderOptions\Physical Objects\Database Generation\Default]
Create=Yes
Comment=Yes
Drop=Yes

[FolderOptions\Physical Objects\Database Generation\Sequence]
Create=Yes
Drop=Yes
Comment=Yes
Permission=No

[FolderOptions\Physical Objects\Database Generation\Table&amp;&amp;Column]

[FolderOptions\Physical Objects\Database Generation\Table&amp;&amp;Column\Table]
Create=Yes
Drop=Yes
Comment=Yes
Permission=No

[FolderOptions\Physical Objects\Database Generation\Table&amp;&amp;Column\Table\Create]
Check=Yes
Physical Options=Yes
Header=Yes
Footer=Yes

[FolderOptions\Physical Objects\Database Generation\Table&amp;&amp;Column\Table\Create\Check]
Constraint declaration=No

[FolderOptions\Physical Objects\Database Generation\Table&amp;&amp;Column\Column]
User datatype=Yes
Default value=Yes
Check=Yes
Physical Options=Yes
Comment=Yes

[FolderOptions\Physical Objects\Database Generation\Table&amp;&amp;Column\Column\Check]
Constraint declaration=No

[FolderOptions\Physical Objects\Database Generation\Table&amp;&amp;Column\Key]

[FolderOptions\Physical Objects\Database Generation\Table&amp;&amp;Column\Key\Primary key]
Create=Yes
Drop=Yes
Comment=Yes

[FolderOptions\Physical Objects\Database Generation\Table&amp;&amp;Column\Key\Primary key\Create]
Constraint declaration=No
Physical Options=Yes

[FolderOptions\Physical Objects\Database Generation\Table&amp;&amp;Column\Key\Alternate key]
Create=Yes
Drop=Yes
Comment=Yes

[FolderOptions\Physical Objects\Database Generation\Table&amp;&amp;Column\Key\Alternate key\Create]
Constraint declaration=No
Physical Options=Yes

[FolderOptions\Physical Objects\Database Generation\Table&amp;&amp;Column\Foreign key]
Create=Yes
Drop=Yes
Comment=Yes

[FolderOptions\Physical Objects\Database Generation\Table&amp;&amp;Column\Foreign key\Create]
Constraint declaration=Yes

[FolderOptions\Physical Objects\Database Generation\Table&amp;&amp;Column\Index]
Create=Yes
Drop=Yes
Comment=Yes

[FolderOptions\Physical Objects\Database Generation\Table&amp;&amp;Column\Index\Create]
Constraint declaration=Yes
Physical Options=Yes

[FolderOptions\Physical Objects\Database Generation\Table&amp;&amp;Column\Index\Filter]
Primary key=Yes
Foreign key=Yes
Alternate key=Yes
Cluster=Yes
Other=Yes

[FolderOptions\Physical Objects\Database Generation\Table&amp;&amp;Column\Trigger]
Create=Yes
Drop=Yes
Comment=Yes

[FolderOptions\Physical Objects\Database Generation\Table&amp;&amp;Column\Trigger\Filter]
For insert=Yes
For update=Yes
For delete=Yes
For other=Yes

[FolderOptions\Physical Objects\Database Generation\View]
Create=Yes
Drop=Yes
Comment=Yes
Permission=No

[FolderOptions\Physical Objects\Database Generation\View\Create]
Force Column list=No
Physical Options=Yes
Header=Yes
Footer=Yes

[FolderOptions\Physical Objects\Database Generation\View\ViewColumn]
Comment=Yes

[FolderOptions\Physical Objects\Database Generation\View\ViewIndex]
Create=Yes
Drop=Yes
Comment=Yes

[FolderOptions\Physical Objects\Database Generation\View\ViewIndex\Create]
Physical Options=Yes

[FolderOptions\Physical Objects\Database Generation\View\ViewIndex\Filter]
Cluster=Yes
Other=Yes

[FolderOptions\Physical Objects\Database Generation\View\Trigger]
Create=Yes
Drop=Yes
Comment=Yes

[FolderOptions\Physical Objects\Database Generation\View\Trigger\Filter]
For insert=Yes
For update=Yes
For delete=Yes
For other=Yes

[FolderOptions\Physical Objects\Database Generation\DBMSTrigger]
Create=Yes
Drop=Yes
Comment=Yes

[FolderOptions\Physical Objects\Database Generation\Synonym]
Create=Yes
Drop=Yes

[FolderOptions\Physical Objects\Database Generation\Synonym\Filter]
Table=Yes
View=Yes
Proc=Yes
Synonym=Yes
Database Package=Yes
Sequence=Yes

[FolderOptions\Physical Objects\Database Generation\JoinIndex]
Create=Yes
Drop=Yes
Comment=Yes

[FolderOptions\Physical Objects\Database Generation\JoinIndex\Create]
Physical Options=Yes
Header=Yes
Footer=Yes

[FolderOptions\Physical Objects\Database Generation\Procedure]
Create=Yes
Drop=Yes
Comment=Yes
Permission=No

[FolderOptions\Physical Objects\Database Generation\Procedure\Create]
Header=Yes
Footer=Yes

[FolderOptions\Physical Objects\Database Generation\DatabasePackage]
Create=Yes
Drop=Yes
Permission=No

[FolderOptions\Physical Objects\Database Generation\WebService]
Create=Yes
Drop=Yes
Comment=Yes

[FolderOptions\Physical Objects\Database Generation\Dimension]
Create=Yes
Drop=Yes

[FolderOptions\Physical Objects\Database Generation\Synchronization]
GenBackupTabl=1
GenKeepBackTabl=1
GenTmpTablDrop=No
GenKeepTablOpts=No

[FolderOptions\Physical Objects\Test Data]
GenDataPathName=
GenDataSinglefile=Yes
GenDataScriptName=testdata
GenDataScriptName0=
GenDataScriptName1=
GenDataScriptName2=
GenDataScriptName3=
GenDataScriptName4=
GenDataScriptName5=
GenDataScriptName6=
GenDataScriptName7=
GenDataScriptName8=
GenDataScriptName9=
GenDataOdbc=0
GenDataDelOld=No
GenDataTitle=No
GenDataDefNumRows=20
GenDataCommit=0
GenDataPacket=0
GenDataOwner=No
GenDataProfNumb=
GenDataProfChar=
GenDataProfDate=
GenDataCSVSeparator=,
GenDataFileFormat=CSV
GenDataUseWizard=No

[FolderOptions\Pdm]
IndxIQName=%COLUMN%_%INDEXTYPE%
IndxPK=Yes
IndxFK=Yes
IndxAK=Yes
IndxPKName=%TABLE%_PK
IndxFKName=%REFR%_FK
IndxAKName=%AKEY%_AK
IndxPreserve=No
IndxThreshold=0
IndxStats=No
RefrPreserve=No
JidxPreserve=No
RbldMultiFact=Yes
RbldMultiDim=Yes
RbldMultiJidx=Yes
CubePreserve=No
TablStProcPreserve=No
ProcDepPreserve=Yes
TrgrDepPreserve=Yes
CubeScriptPath=
CubeScriptCase=0
CubeScriptEncoding=ANSI
CubeScriptNacct=No
CubeScriptHeader=No
CubeScriptExt=csv
CubeScriptExt0=txt
CubeScriptExt1=
CubeScriptExt2=
CubeScriptSep=,
CubeScriptDeli=&quot;
EstimationYears=0
DfltDomnName=D_%.U:VALUE%
DfltColnName=D_%.U:VALUE%
DfltReuse=Yes
DfltDrop=Yes""".decode('utf-8')
        self.ModelOptionsText="""[ModelOptions]

[ModelOptions\Physical Objects]
CaseSensitive=No
DisplayName=Yes
EnableTrans=No
UseTerm=No
EnableRequirements=No
EnableFullShortcut=Yes
DefaultDttp=
IgnoreOwner=No
RebuildTrigger=Yes
RefrUnique=No
RefrAutoMigrate=Yes
RefrMigrateReuse=Yes
RefrMigrateDomain=Yes
RefrMigrateCheck=Yes
RefrMigrateRule=Yes
RefrMigrateExtd=No
RefrMigrDefaultLink=No
RefrDfltImpl=D
RefrPrgtColn=No
RefrMigrateToEnd=No
RebuildTriggerDep=No
ColnFKName=%.3:PARENT%_%COLUMN%
ColnFKNameUse=No
DomnCopyDttp=Yes
DomnCopyChck=No
DomnCopyRule=No
DomnCopyMand=No
DomnCopyExtd=No
DomnCopyProf=No
Notation=0
DomnDefaultMandatory=No
ColnDefaultMandatory=No
TablDefaultOwner=
ViewDefaultOwner=
TrgrDefaultOwnerTabl=
TrgrDefaultOwnerView=
IdxDefaultOwnerTabl=
IdxDefaultOwnerView=
JdxDefaultOwner=
DBPackDefaultOwner=
SeqDefaultOwner=
ProcDefaultOwner=
DBMSTrgrDefaultOwner=
Currency=USD
RefrDeleteConstraint=1
RefrUpdateConstraint=1
RefrParentMandatory=No
RefrParentChangeAllow=Yes
RefrCheckOnCommit=No

[ModelOptions\Physical Objects\NamingOptionsTemplates]

[ModelOptions\Physical Objects\ClssNamingOptions]

[ModelOptions\Physical Objects\ClssNamingOptions\PDMPCKG]

[ModelOptions\Physical Objects\ClssNamingOptions\PDMPCKG\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\PDMPCKG\Code]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\PDMDOMN]

[ModelOptions\Physical Objects\ClssNamingOptions\PDMDOMN\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\PDMDOMN\Code]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\TABL]

[ModelOptions\Physical Objects\ClssNamingOptions\TABL\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\TABL\Code]
Template=
MaxLen=30
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\COLN]

[ModelOptions\Physical Objects\ClssNamingOptions\COLN\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\COLN\Code]
Template=
MaxLen=30
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\INDX]

[ModelOptions\Physical Objects\ClssNamingOptions\INDX\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\INDX\Code]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\REFR]

[ModelOptions\Physical Objects\ClssNamingOptions\REFR\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\REFR\Code]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\VREF]

[ModelOptions\Physical Objects\ClssNamingOptions\VREF\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\VREF\Code]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\VIEW]

[ModelOptions\Physical Objects\ClssNamingOptions\VIEW\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\VIEW\Code]
Template=
MaxLen=30
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\VIEWC]

[ModelOptions\Physical Objects\ClssNamingOptions\VIEWC\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\VIEWC\Code]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\WEBSERV]

[ModelOptions\Physical Objects\ClssNamingOptions\WEBSERV\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\WEBSERV\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;/-_.!~*&#39;()&quot;
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\WEBOP]

[ModelOptions\Physical Objects\ClssNamingOptions\WEBOP\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\WEBOP\Code]
Template=
MaxLen=254
Case=M
ValidChar=&#39;a&#39;-&#39;z&#39;,&#39;A&#39;-&#39;Z&#39;,&#39;0&#39;-&#39;9&#39;,&quot;/-_.!~*&#39;()&quot;
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\WPARAM]

[ModelOptions\Physical Objects\ClssNamingOptions\WPARAM\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\WPARAM\Code]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\FACT]

[ModelOptions\Physical Objects\ClssNamingOptions\FACT\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\FACT\Code]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\DIMN]

[ModelOptions\Physical Objects\ClssNamingOptions\DIMN\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\DIMN\Code]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\MEAS]

[ModelOptions\Physical Objects\ClssNamingOptions\MEAS\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\MEAS\Code]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\DATTR]

[ModelOptions\Physical Objects\ClssNamingOptions\DATTR\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\DATTR\Code]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\FILO]

[ModelOptions\Physical Objects\ClssNamingOptions\FILO\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\FILO\Code]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\FRMEOBJ]

[ModelOptions\Physical Objects\ClssNamingOptions\FRMEOBJ\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\FRMEOBJ\Code]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\FRMELNK]

[ModelOptions\Physical Objects\ClssNamingOptions\FRMELNK\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\FRMELNK\Code]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\DefaultClass]

[ModelOptions\Physical Objects\ClssNamingOptions\DefaultClass\Name]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Physical Objects\ClssNamingOptions\DefaultClass\Code]
Template=
MaxLen=254
Case=M
ValidChar=
InvldChar=
AllValid=Yes
NoAccent=No
DefaultChar=
Script=
ConvTable=
ConvTablePath=%_HOME%\Resource Files\Conversion Tables

[ModelOptions\Connection]

[ModelOptions\Pdm]

[ModelOptions\Generate]

[ModelOptions\Generate\Xsm]
GenRootElement=Yes
GenComplexType=No
GenAttribute=Yes
CheckModel=Yes
SaveLinks=Yes
ORMapping=No
NameToCode=No

[ModelOptions\Generate\Pdm]
RRMapping=No

[ModelOptions\Generate\Cdm]
CheckModel=Yes
SaveLinks=Yes
NameToCode=No
Notation=2

[ModelOptions\Generate\Oom]
CheckModel=Yes
SaveLinks=Yes
ORMapping=No
NameToCode=Yes
ClassPrefix=

[ModelOptions\Generate\Ldm]
CheckModel=Yes
SaveLinks=Yes
NameToCode=No

[ModelOptions\Default Opts]

[ModelOptions\Default Opts\TABL]
PhysOpts=

[ModelOptions\Default Opts\COLN]
PhysOpts=

[ModelOptions\Default Opts\INDX]
PhysOpts=

[ModelOptions\Default Opts\AKEY]
PhysOpts=

[ModelOptions\Default Opts\PKEY]
PhysOpts=

[ModelOptions\Default Opts\STOR]
PhysOpts=

[ModelOptions\Default Opts\TSPC]
PhysOpts=

[ModelOptions\Default Opts\SQNC]
PhysOpts=

[ModelOptions\Default Opts\DTBS]
PhysOpts=

[ModelOptions\Default Opts\\USER]
PhysOpts=

[ModelOptions\Default Opts\JIDX]
PhysOpts=

[ModelOptions\Default Opts\FRMEOBJ&lt;&lt;Cluster&gt;&gt;]
PhysOpts=

[ModelOptions\Default Opts\FRMEOBJ&lt;&lt;MaterializedViewLog&gt;&gt;]
PhysOpts=

[ModelOptions\Default Opts\FRMESOB&lt;&lt;Cluster&gt;&gt;]
PhysOpts=

[ModelOptions\Default Opts\FRMESOB&lt;&lt;MaterializedViewLog&gt;&gt;]
PhysOpts=

[ModelOptions\Default Opts\FRMESOB&lt;&lt;ClusterIndex&gt;&gt;]
PhysOpts=""".decode('utf-8')
        self.declaretion="""<?xml version="1.0" encoding="UTF-8"?>""".decode('utf-8')
        self.doctype="""<?PowerDesigner AppLocale="UTF16" ID="{54CF2886-9AF8-45C9-8BCB-BE5B27F028B3}" Label="" LastModificationDate="1508915103" Name="ModelTemplate" Objects="99" Symbols="9" Target="ORACLE Version 11g" Type="{CDE44E21-9669-11D1-9914-006097355D9B}" signature="PDM_DATA_MODEL_XML" version="16.5.0.3982"?>
<!-- do not edit this file -->
""".decode('utf-8')
        #概览(一级面板)
        self.firstphysicaldiag = PDMPhysicalDiagram(u'概览', u'overview')
        self.packagelist=[]
        self.id = self.getidno()

    def addpackage(self,name,code,comment=None):
        """
        增加Package , 同时在一级面板中增加该包
        :param name: 包名称
        :param code: 包编码
        :param comment: 包注释
        :return: 返回对象PDMPackage对象
        """
        package=PDMPackage(name,code,comment)
        self.firstphysicaldiag.addsymbol(name,code,'Package',package.id,comment)
        self.packagelist.append(package)
        return package

    def toxmlelement(self):
        """
        模型对象转为XML
        外层 / Model / o:Object / c:Children / o:Model

        / a:ObjectID
        / c:DBMS / o:Shortcut / a:ObjectID
        / c:PhysicalDiagrams / o:PhysicalDiagram / a:ObjectID
                                                 / c:Symbols / o:PackageSymbol / a:ObjectID
                                                                               / c:Object / o:Packge
        / c:Packges / o:Packge / a:ObjectID
                               / c:PhysicalDiagrams / o:PhysicalDiagram / a:ObjectID
                               / c:DefaultDiagram / o:PhysicalDiagram
                               / c:Tables / o:Table / a:ObjectID
                                                    / c:Columns / o:Column / a:ObjectID
        / c:DefaultDiagram / o:PhysicalDiagram
        / c:DefaultGroups / o:Group / a:ObjectID
        / c:TargetModels / o:TargetModel / a:ObjectID
                                         / c:SessionShortcuts / o:Shortcut
        :return: etree.Element对象
        """
        #初始层级   Model / o:Object / c:Children / o:Model
        root=etree.Element('Model',nsmap=nsmapdict)
        rootobject=etree.SubElement(root,'{object}RootObject',Id='o1')
        children=etree.SubElement(rootobject,'{collection}Children')
        model = etree.SubElement(children, '{object}Model',Id='o2')

        # o:Model 增加基本属性
        super(PDMModel,self).setdefaultelement(model)
        etree.SubElement(model, '{attribute}PackageOptionsText').text = self.PackageOptionsText
        etree.SubElement(model, '{attribute}ModelOptionsText').text = self.ModelOptionsText

        # o:Model 增加数据库说明
        dbms=etree.SubElement(model,'{collection}DBMS')
        shortcut=etree.SubElement(dbms, '{object}Shortcut', Id=u'o3')
        etree.SubElement(shortcut, '{attribute}ObjectID').text = u'799FC735-C3DE-4C11-B26B-033A995F0F11'
        etree.SubElement(shortcut, '{attribute}Name').text = u'ORACLE Version 11g'
        etree.SubElement(shortcut, '{attribute}Code').text = u'ORA11GR1'
        etree.SubElement(shortcut, '{attribute}CreationDate').text = str(time.time())
        etree.SubElement(shortcut, '{attribute}Creator').text = u'ZhuJian'
        etree.SubElement(shortcut, '{attribute}ModificationDate').text = str(time.time())
        etree.SubElement(shortcut, '{attribute}Modifier').text = u'ZhuJian'
        etree.SubElement(shortcut, '{attribute}TargetStereotype')
        etree.SubElement(shortcut, '{attribute}TargetID').text = u'BAE632F3-AC04-4059-9893-259ABA89351C'
        etree.SubElement(shortcut, '{attribute}TargetClassID').text = u'4BA9F647-DAB1-11D1-9944-006097355D9B'

        # o:Model 增加图板模块
        physicalDiagrams = etree.SubElement(model, '{collection}PhysicalDiagrams')
        physicalDiagrams.append(self.firstphysicaldiag.toxmlelement())

        # o:Model 增加包模块
        packages=etree.SubElement(model,'{collection}Packages')
        for pck in self.packagelist:
            packages.append(pck.toxmlelement())

        # o:Model 增加默认图板 , 指向 概览
        defaultdiag=etree.SubElement(model,'{collection}DefaultDiagram')
        etree.SubElement(defaultdiag,'{object}PhysicalDiagram',Ref=self.firstphysicaldiag.symbollist[0].id)

        # o:Model 增加默认组
        DefaultGroups=etree.SubElement(model,'{collection}DefaultGroups')
        group=PubItem(u'PUBLIC',u'PUBLIC')
        xmlgroup=etree.SubElement(DefaultGroups,'{object}Group',id=self.getidno())
        group.setdefaultelement(xmlgroup)

        # o:Model 增加目标数据库,与前文DBMS对应 , TargetModelID & TargetModelClassID
        TargetModels = etree.SubElement(model, '{collection}TargetModels')
        TargetModel = PubItem(u'ORACLE Version 11g', u'ORA11GR1')
        xmlTargetModel = etree.SubElement(TargetModels, '{object}TargetModel', id=self.getidno())
        TargetModel.setdefaultelement(xmlTargetModel)
        etree.SubElement(xmlTargetModel, '{attribute}TargetModelURL').text = u'file:///%_DBMS%/ora11g.xdb'
        etree.SubElement(xmlTargetModel, '{attribute}TargetModelID').text = u'BAE632F3-AC04-4059-9893-259ABA89351C'
        etree.SubElement(xmlTargetModel, '{attribute}TargetModelClassID').text = u'4BA9F647-DAB1-11D1-9944-006097355D9B'
        etree.SubElement(xmlTargetModel, '{attribute}TargetModelLastModificationDate').text = u'1355934917'

        # o:Model Shortcuts , 指向 DBMS.Shortcuts.Id
        SessionShortcuts = etree.SubElement(xmlTargetModel, '{collection}SessionShortcuts')
        etree.SubElement(SessionShortcuts,'{object}Shortcut', Ref=u'o3')

        #返回完整xml对象
        return root

    def output(self):
        ele = self.toxmlelement()
        eletree=etree.ElementTree(ele)
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        eletree.write(self.name+'.pdm',method='xml',encoding='utf-8',xml_declaration=self.declaretion,doctype=self.doctype,pretty_print=True)

if __name__ == '__main__':
    model=PDMModel(u'测试模型',u'testmodel')
    package=model.addpackage(u'测试包',u'testpck')
    test = package.addtable(u'测试表', u'testtable')
    test.addcolumn(u'测试字段11', u'testcol111', u'varchar2', u'60', mandatory=True)
    test.addcolumn(u'测试字段22', u'testcol123', u'varchar2', u'60', mandatory=True)
    colid = test.getcolumnidbyname([u'testcol111', u'testcol123'], True)
    test.addindex(u'测试索引', u'testkey', colid, u'测试索引,无效字段', u'P')
    test.addindex(u'测试索引12', u'testindex', colid, u'测试索引,无效字段', u'U')
    model.output()