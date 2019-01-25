import urllib
import io
import numpy as np
import datetime 
import time
import pandas as pd
import datetime
import os
#class market(eu):
#    self.name=eu
#    self.stock=
#milan=market(milan)
#from indicies import eurstock
bvsp=[
'^BVSP',
'ABEV3.SA',
'ALLL3.SA',
'BBAS3.SA',
'BBDC4.SA',
'BBSE3.SA',
'BRFS3.SA',
'BRML3.SA',
'BRPR3.SA',
'BVMF3.SA',
'CCRO3.SA',
'CIEL3.SA',
'CMIG4.SA',
'CSAN3.SA',
'CSNA3.SA',
'ECOR3.SA',
'ELET3.SA',
'ESTC3.SA',
'GFSA3.SA',
'GGBR4.SA',
'GOLL4.SA',
'HYPE3.SA',
'ITSA4.SA',
'ITUB3.SA',
'JBSS3.SA',
'KROT3.SA',
'LAME4.SA',
'MRFG3.SA',
'MULT3.SA',
'PETR3.SA',
'PETR4.SA',
'QUAL3.SA',
'SUZB5.SA',
'TIMP3.SA',
'VALE3.SA',
'VALE5.SA',
'USIM5.SA',
'BRKM5.SA',
'EMBR3.SA',
'KLBN11.SA',
'UGPA3.SA'
]

#https://query1.finance.yahoo.com/v7/finance/quote?symbols=UNP&fields=ebitda,shortRatio,priceToSales
#https://query1.finance.yahoo.com/v7/finance/quote?symbols=TLS.AX,MUS.AX

url='https://query1.finance.yahoo.com/v8/finance/chart/cs.pa?&interval=30m&indicators=quote&includeTimestamps=true'


oslo=[
'ORK.OL',
'TEL.OL',
'MHG.OL',
'GJF.OL',
'SCHA.OL',
'DNB.OL',
'STB.OL',
'YAR.OL',
'REC.OL',
'NANO.OL',
'SALM.OL',


'BAKKA.OL',
'LSG.OL',
'NAS.OL',
'GSF.OL',
'STL.OL',
'NHY.OL',
'TGS.OL',
'SUBC.OL',
'BWLPG.OL',

#'ASKO.OL',
'AKERBP.OL',
'GOGL.OL',
'DNO.OL',
'PGS.OL'




]

gemany=['^GDAXI',
'ADS.DE',
'ALV.DE',
'BAS.DE',
'BAYN.DE',
'BEI.DE',
'BMW.DE',
'CBK.DE',
'DAI.DE',
'DB1.DE',
'DBK.DE',
'DPW.DE',
'DTE.DE',
'EOAN.DE',
#'FME.DE',
#'FRE.DE',
#'HEI.DE',
'HEN.DE',
'IFX.DE',
'LHA.DE',
#'LIN.DE',
'MRK.DE',
'MUV2.DE',
'PSM.DE',
'RWE.DE',
'SAP.DE',
'SIE.DE',
'TKA.DE',
'VNA.DE',
'VOW3.DE',
'CEC.DE',
'PAH3.DE',
'KGX.DE',
'DLG.DE',
'SDF.DE',
'1COV.DE',
'WAF.DE',
'OSR.DE',
'LXS.DE'


#'TEC.PA',
]
france=[
'FP.PA',
'BNP.PA',
'CS.PA',
'ORA.PA',
'ACA.PA',
'EDF.PA',
'ENGI.PA',
'GLE.PA',
'VIV.PA',
'KN.PA',
'CA.PA',
'SEV.PA',
'AF.PA',
'VK.PA',
'CGG.PA',
'SAN.PA',
'UG.PA',
'RNO.PA',
'AIR.PA',
'SGO.PA',
'STM.PA',
'CO.PA',
'FR.PA',
'EO.PA'
]
swiss=[

'ABBN.VX',
'ADEN.VX',
#'ATLN.VX',
'BAER.VX',
'CFR.VX',
'CSGN.VX',
'GEBN.VX',
'GIVN.VX',
'LHN.VX',
'NESN.VX',
'NOVN.VX',
'ROG.VX',
'SCMN.VX',
'SGSN.VX',
'SLHN.VX',
'SREN.VX',
#'SYNN.VX',
'UBSG.VX',
'UHR.VX',
'ZURN.VX',
'CLN.VX',
#'AMS.SW'


]
milan=[
'ENI.MI',
'ENEL.MI',
'ISP.MI',
'UCG.MI',
'FCA.MI',
'G.MI',
'ATL.MI',
'TEN.MI',
'STM.MI',
'CNHI.MI',
'SRG.MI'
]
netherlands=[
'MT.AS',
'RDSA.AS',
'PNL.AS',
'AGN.AS',
'PHIA.AS',
'INGA.AS',
'KPN.AS',
'ABN.AS',
'AD.AS',
'UNA.AS',
'ATC.AS',
'ATCB.AS'
]
uk=[
'LLOY.L',
'VOD.L',
'BP.L',
'BARC.L',
'MKS.L',
'GLEN.L',
'MRO.L',
'HSBA.L',
'PMO.L',
#'EVRH.L',
'TSCO.L',
#'BLT.L',
'CNA.L',
'TCG.L',
'RBS.L',
'LGEN.L',
'TW.L',
'TLW.L',
'GNC.L',
'STAN.L',
'KGF.L',
'AV.L'


]
BR=[
'BPOST.BR',
'EURN.BR',
'PROX.BR',
'KBC.BR',
'ABI.BR',
'UMI.BR',
'FAGR.BR',
'AGS.BR',
'SOLB.BR'

]
#urlstr = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1d/csv/'
#    z=str(data).split('\\n')
#    for eachLine in z:
#        splitLine=eachLine.split(',')
#        if len(splitLine)==6:
#            if 'values' not in eachLine:
#    
##                lineToWrite=eachLine+'\n'
##                print (splitLine)
#                stklist.append(splitLine)
#    beforeClose=float(stklist[-2][1])
#    afterClose=float(stklist[-1][1])
#    return float("%.3f"%(afterClose/beforeClose-1))
#https://query1.finance.yahoo.com/v7/finance/quote?symbols=BAS.DE
#for stock in eurstock:
#    print (stock,bvspAfterclose(stock))
def getminbar(symbol,min):#str'1','5'
    url='https://query1.finance.yahoo.com/v8/finance/chart/'+symbol+'?&interval='+min+'m&indicators=quote&includeTimestamps=true'

    try:
        
        urlid = urllib.urlopen(url)
    except:
        print np.nan
    
    
    data =urlid.read()
    global null
    null='k'
    data_dict=eval(data)
    close_list=data_dict['chart']['result'][0]['indicators']['quote'][0]['close']
    volume_list=data_dict['chart']['result'][0]['indicators']['quote'][0]['volume']
    meta=data_dict['chart']['result'][0]['meta']
    c_pre=meta['previousClose']
    timestamp=data_dict['chart']['result'][0]['timestamp']
    meta=data_dict['chart']['result'][0]['meta']
    dt_obj = datetime.datetime.fromtimestamp(timestamp[0]) 
    clcopy=[]
    for c in close_list:
        if c!='k':
            clcopy.append(c)
    return clcopy[-1],c_pre
def getdaybar(symbol,day):#str'1','5'
    url='https://query1.finance.yahoo.com/v8/finance/chart/'+symbol+'?&interval='+day+'d&indicators=quote&includeTimestamps=true'
    try:
        
        urlid = urllib.urlopen(url)
    except:
        print np.nan
    
      
    data =urlid.read()
    global null
    null=''
    data_dict=eval(data)
    close_list=data_dict['chart']['result'][0]['indicators']['quote'][0]['close']
    volume_list=data_dict['chart']['result'][0]['indicators']['quote'][0]['volume']
    meta=data_dict['chart']['result'][0]['meta']
#    c_pre=meta['previousClose']
    #
    timestamp=data_dict['chart']['result'][0]['timestamp']
    meta=data_dict['chart']['result'][0]['meta']
    dt_obj = datetime.datetime.fromtimestamp(timestamp[0])
    return [close_list[-1],dt_obj]
def chg(market):
    
    
    result1=[]
    result2=[]
    symbolresult=[]
    textData=[]
    print datetime.datetime.now()
    for stk in market:
        [before_c,yesterday_c]=(getminbar(stk,'5'))
#        before_c1=float(before_c)
#        yesterday_c1=float(yesterday_c)
        after_cList=getdaybar(stk,'1')
        after_c=after_cList[0]
        day1=str(after_cList[1])[0:10]
        
        chg=[after_c/float(before_c)-1,after_c/float(yesterday_c)-1]
        
#        print type(before_c),type(yesterday_c),type(after_c)
#        print before_c,yesterday_c,after_c
        print 'symbol:%s,before_c:%.3f,after_c:%.3f,yesterday_c:%.3f,chgOnclose:%.3f,chgToday:%.3f'%(stk,before_c,after_c,yesterday_c,chg[0],chg[1])
        data='symbol:%s,before_c:%.3f,after_c:%.3f,yesterday_c:%.3f,chgOnclose:%.3f,chgToday:%.3f'%(stk,before_c,after_c,yesterday_c,chg[0],chg[1])
        textData.append(data)
        result1.append(chg[0])
        result2.append(chg[1])
        symbolresult.append(stk)
        time.sleep(1)
        result=[result1,result2]
    os.chdir('d:\\data\\onClose')
    market1=market[-1][-2:]
    if market1=='SW':
	market1='VX'
    if not os.path.exists(market1):
        os.makedirs(market1)
        print '%s is not exits' % market1
    os.chdir(market1)
    if not os.path.exists(day1):
        os.makedirs(day1)
    os.chdir(day1)
    fo = open(str(day1) + '.txt', 'a+')
    fo.write(str(textData) + '\n')
    fo.close()
            



        
        
        
        
    return result

if __name__ == '__main__':
    #pass





    rde=chg(gemany)
    rpa=chg(france)
    rsw=chg(swiss)
    rmi=chg(milan)
    ras=chg(netherlands)
    ruk=chg(uk)
    rbr=chg(BR)
    
    