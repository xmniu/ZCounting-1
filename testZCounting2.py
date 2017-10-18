import ROOT
import os,sys
from ROOT import TGraphAsymmErrors
from ROOT import TGraphErrors
from ROOT import TColor
from array import array
from ROOT import *
from operator import truediv
import random
import math
import pandas

inFile="testCSV2.csv"
chunkSize=200
eosDir="/eos/cms/store/group/comm_luminosity/ZCounting/DQMFiles2017/cmsweb.cern.ch/dqm/offline/data/browse/ROOT/OfflineData/Run2017/SingleMuon/"

HLTeffB=array('d')
HLTeffE=array('d')
SITeffB=array('d')
SITeffE=array('d')
StaeffB=array('d')
StaeffE=array('d')
crossX=array('d')
crossX2=array('d')


Zyield=array('d')
Zrate=array('d')
Zrate2=array('d')
lumiDel=array('d')
instDel=array('d')
beginTime=[]
endTime=[]
fillarray=array('d')
windowarray=array('d')


ROOT.gROOT.Macro( os.path.expanduser( '~/.rootlogon.C' ) )
ROOT.gROOT.LoadMacro("calculateDataEfficiency_v3.C")
ROOT.gROOT.LoadMacro("calculateZEfficiency.C")
ROOT.gROOT.SetBatch(True)

#lumiFile=open("./run302031.csv")
#lumiLines=lumiFile.readlines()
#data=pandas.read_csv("./run302031.csv",sep=',',low_memory=False, skiprows=[0,len(lumiLines)-5,len(lumiLines)-4,len(lumiLines)-3,len(lumiLines)-2,len(lumiLines)-1,len(lumiLines)])

lumiFile=open(inFile)
lumiLines=lumiFile.readlines()
data=pandas.read_csv(inFile, sep=',',low_memory=False, skiprows=[0,len(lumiLines)-5,len(lumiLines)-4,len(lumiLines)-3,len(lumiLines)-2,len(lumiLines)-1,len(lumiLines)])

print data.axes

# TAKE INPUT CSV FILE AND STRUCTURE PER-RUN BASIS, THEN CREATE LIST OF LUMI AND LS`s PER RUN
LSlist=data.groupby('#run:fill')['ls'].apply(list)
recLumiList=data.groupby('#run:fill')['recorded(/pb)'].apply(list)
delLumiList=data.groupby('#run:fill')['delivered(/pb)'].apply(list)
avgpuList=data.groupby('#run:fill')['avgpu'].apply(list)
timeList=data.groupby('#run:fill')['time'].apply(list)
for i in range(0,len(LSlist)):
	LSlist[i]=[int(x.split(':')[0]) for x in LSlist[i]]
fillRunlist=data.drop_duplicates('#run:fill')['#run:fill'].tolist()

print fillRunlist
print "length LS list: "+str(len(LSlist))
print "length Run list: "+str(len(fillRunlist))

nMeasurements=0

for run_i in range(0,len(fillRunlist)):
    nMeasurements=nMeasurements+1
    run=int(fillRunlist[run_i].split(':')[0])
    fill=int(fillRunlist[run_i].split(':')[1])
    print run
    print fill

    if run<300122 or run>304062:
	continue

    if run<302030:
	era="C"
    if run>=302030 and run<303434:
	era="D"
    if run>=303434:
	era="E"
    

    LSchunks 	 = [LSlist[run_i][x:x+chunkSize] for x in range(0, len(LSlist[run_i]), chunkSize)]
    Del_chunks   = [delLumiList[run_i][x:x+chunkSize] for x in range(0, len(delLumiList[run_i]), chunkSize)] 
    Rec_chunks   = [recLumiList[run_i][x:x+chunkSize] for x in range(0, len(recLumiList[run_i]), chunkSize)]
    Avgpu_chunks = [avgpuList[run_i][x:x+chunkSize] for x in range(0, len(avgpuList[run_i]), chunkSize)]
    time_chunks  = [timeList[run_i][x:x+chunkSize] for x in range(0, len(timeList[run_i]), chunkSize)]

    for chunk_i in range(0,len(LSchunks)):
	recLumi_i   = sum(Rec_chunks[chunk_i])
	delLumi_i   = sum(Del_chunks[chunk_i])	
	avgPileup_i = sum(Avgpu_chunks[chunk_i])
	avgPileup_i = avgPileup_i/len(Avgpu_chunks[chunk_i])
	deadtime_i  = recLumi_i/delLumi_i
	print time_chunks[chunk_i]

	datestamp_low=time_chunks[chunk_i][0].split(" ")
	date_low=ROOT.TDatime(2017,int(datestamp_low[0].split("/")[0]),int(datestamp_low[0].split("/")[1]),int(datestamp_low[1].split(":")[0]),int(datestamp_low[1].split(":")[1]),int(datestamp_low[1].split(":")[2]))

        datestamp_up=time_chunks[chunk_i][-1].split(" ")
	date_up=ROOT.TDatime(2017,int(datestamp_up[0].split("/")[0]),int(datestamp_up[0].split("/")[1]),int(datestamp_up[1].split(":")[0]),int(datestamp_up[1].split(":")[1]),int(datestamp_up[1].split(":")[2]))


	print time_chunks[chunk_i]
	print (date_up.Convert()-date_low.Convert())+23
    	print date_up.Convert()
	print date_low.Convert()
	print LSchunks[chunk_i]
	print recLumi_i
	print delLumi_i
	print avgPileup_i
	print "opening file: "+eosDir+"000"+str(run)[:-2]+"xx/DQM_V0001_R000"+str(run)+"__SingleMuon__Run2017"+era+"-PromptReco-v1__DQMIO.root"

    	HLTeffB_i=ROOT.calculateDataEfficiency_v3(0,eosDir+"000"+str(run)[:-2]+"xx/DQM_V0001_R000"+str(run)+"__SingleMuon__Run2017"+era+"-PromptReco-v1__DQMIO.root",".",str(run),chunk_i,LSchunks[chunk_i][0],LSchunks[chunk_i][-1],avgPileup_i,"HLT",0,0,0,0,0)
    	HLTeffE_i=ROOT.calculateDataEfficiency_v3(0,eosDir+"000"+str(run)[:-2]+"xx/DQM_V0001_R000"+str(run)+"__SingleMuon__Run2017"+era+"-PromptReco-v1__DQMIO.root",".",str(run),chunk_i,LSchunks[chunk_i][0],LSchunks[chunk_i][-1],avgPileup_i,"HLT",1,0,0,0,0)
	SITeffB_i=ROOT.calculateDataEfficiency_v3(0,eosDir+"000"+str(run)[:-2]+"xx/DQM_V0001_R000"+str(run)+"__SingleMuon__Run2017"+era+"-PromptReco-v1__DQMIO.root",".",str(run),chunk_i,LSchunks[chunk_i][0],LSchunks[chunk_i][-1],avgPileup_i,"SIT",0,1,1,1,1)
	SITeffE_i=ROOT.calculateDataEfficiency_v3(0,eosDir+"000"+str(run)[:-2]+"xx/DQM_V0001_R000"+str(run)+"__SingleMuon__Run2017"+era+"-PromptReco-v1__DQMIO.root",".",str(run),chunk_i,LSchunks[chunk_i][0],LSchunks[chunk_i][-1],avgPileup_i,"SIT",1,1,1,1,1)
	StaeffB_i=ROOT.calculateDataEfficiency_v3(0,eosDir+"000"+str(run)[:-2]+"xx/DQM_V0001_R000"+str(run)+"__SingleMuon__Run2017"+era+"-PromptReco-v1__DQMIO.root",".",str(run),chunk_i,LSchunks[chunk_i][0],LSchunks[chunk_i][-1],avgPileup_i,"Sta",0,1,2,1,2)
	StaeffE_i=ROOT.calculateDataEfficiency_v3(0,eosDir+"000"+str(run)[:-2]+"xx/DQM_V0001_R000"+str(run)+"__SingleMuon__Run2017"+era+"-PromptReco-v1__DQMIO.root",".",str(run),chunk_i,LSchunks[chunk_i][0],LSchunks[chunk_i][-1],avgPileup_i,"Sta",1,1,2,1,2)
	Zyield_i=ROOT.calculateDataEfficiency_v3(1,eosDir+"000"+str(run)[:-2]+"xx/DQM_V0001_R000"+str(run)+"__SingleMuon__Run2017"+era+"-PromptReco-v1__DQMIO.root",".",str(run),chunk_i,LSchunks[chunk_i][0],LSchunks[chunk_i][-1],avgPileup_i,"HLT",0,0,0,0,0)

	crossX.append(Zyield_i/(StaeffB_i**2 * SITeffB_i**2 * (1-(1-HLTeffB_i)*(1-HLTeffB_i))*recLumi_i))
	effTot_i=(StaeffB_i**2 * SITeffB_i**2 * (1-(1-HLTeffB_i)*(1-HLTeffB_i)))
	timeWindow_i=(date_up.Convert()-date_low.Convert())+23 #in seconds
	zRate_i = Zyield_i/(effTot_i*deadtime_i*timeWindow_i)

        ZMCEff=ROOT.calculateZEfficiency(0,avgPileup_i,HLTeffB_i,HLTeffE_i,SITeffB_i,SITeffE_i,StaeffB_i,StaeffE_i)
        ZXSec  = Zyield_i*(1-0.01)/(ZMCEff*recLumi_i)
        ZRate  = Zyield_i*(1-0.01)/(ZMCEff*timeWindow_i)
#       ZMCEffBB = ROOT.calculateZEfficiency(1,avgPileup_i,HLTeffB_i,HLTeffE_i,SITeffB_i,SITeffE_i,StaeffB_i,StaeffE_i)
#       ZMCEffBE = ROOT.calculateZEfficiency(2,avgPileup_i,HLTeffB_i,HLTeffE_i,SITeffB_i,SITeffE_i,StaeffB_i,StaeffE_i)
#       ZMCEffEE = ROOT.calculateZEfficiency(3,avgPileup_i,HLTeffB_i,HLTeffE_i,SITeffB_i,SITeffE_i,StaeffB_i,StaeffE_i)
	
	print Zyield
	print effTot_i
	print deadtime_i
	print timeWindow_i
	print zRate_i
	print "===Compare==="
	print ZMCEff
	print ZXSec
	print ZRate
	#Fill output Arrays

	lumiDel.append(delLumi_i)
	Zrate.append(zRate_i)
	Zrate2.append(ZRate)
	crossX2.append(ZXSec)
	Zyield.append(Zyield_i)
	StaeffB.append(StaeffB_i)
	StaeffE.append(StaeffE_i)
	SITeffB.append(SITeffB_i)
	SITeffE.append(SITeffE_i)
    	HLTeffB.append(HLTeffB_i)
    	HLTeffE.append(HLTeffE_i)
	beginTime.append(time_chunks[chunk_i][0])
	endTime.append(time_chunks[chunk_i][-1])
	fillarray.append(fill)
	lumiDel.append(delLumi_i)
	instDel.append(delLumi_i/timeWindow_i)
	windowarray.append(timeWindow_i)
		#5427, 16/10/19 07:06:35, 16/10/19 07:22:54, 6.80618, 0.0105032, 10.024, 6495.66
	
	print crossX


with open('csvfile.csv','wb') as file:
	for c in range(0,nMeasurements):
#		file.write(str(int(fillarray[c]))+","+str(beginTime[c])+","+str(endTime[c])+","+str(Zrate[c])+","+str(instDel[c])+","+str(lumiDel[c])+","+str(Zyield[c]))
		file.write(str(int(fillarray[c]))+","+str(beginTime[c])+","+str(endTime[c])+","+str(ZRate[c])+","+str(instDel[c])+","+str(lumiDel[c])+","+str(Zyield[c]))
        	file.write('\n')

print "crossX: "+str(crossX)
print "Zyield: "+str(Zyield)
print "Zrate: "+str(Zrate)
print "lumiDel: "+str(lumiDel)
print "instDel: "+str(instDel)
print "fill: "+str(fillarray)
print "beginTime: "+str(beginTime)
print "endTime: "+str(endTime)
print "HLTeff: "+str(HLTeff)
print "SITeff: "+str(SITeff)
print "Staeff: "+str(Staeff)
print "timeWindow: "+str(windowarray)
