import os
import sys

for i in range(9999):
    f=open("./hero/"+str(i+1),'r')
    rf = f.read()
    print(rf)
    exec("rfd = dict("+rf+")")
    print(rfd['attributes'])
    
    if len(rfd['attributes']) == 4:
        trait_type0 = str(rfd['attributes'][0]).replace(' ', '').replace("'", '"')
        trait_type1 = str(rfd['attributes'][1]).replace(' ', '').replace("'", '"')
        trait_type2 = str(rfd['attributes'][2]).replace(' ', '').replace("'", '"')
        trait_type3 = str(rfd['attributes'][3]).replace(' ', '').replace("'", '"')
        
        f=open("./hero/"+str(i+1),'w')
        f.write('{"name":"GalacticApe Hero #'+str(i+1)+'","image":"https://raw.githubusercontent.com/galacticapeheroNFT/galacticapeheroNFT/main/galacticapeshero/hero/'+str(i+1)+'.png","attributes":['+trait_type0+','+trait_type1+','+trait_type2+','+trait_type3+']}')


    if len(rfd['attributes']) == 5:
        trait_type0 = str(rfd['attributes'][0]).replace(' ', '').replace("'", '"')
        trait_type1 = str(rfd['attributes'][1]).replace(' ', '').replace("'", '"')
        trait_type2 = str(rfd['attributes'][2]).replace(' ', '').replace("'", '"')
        trait_type3 = str(rfd['attributes'][3]).replace(' ', '').replace("'", '"')
        trait_type4 = str(rfd['attributes'][4]).replace(' ', '').replace("'", '"')
        
        f=open("./hero/"+str(i+1),'w')
        f.write('{"name":"GalacticApe Hero #'+str(i+1)+'","image":"https://raw.githubusercontent.com/galacticapeheroNFT/galacticapeheroNFT/main/galacticapeshero/hero/'+str(i+1)+'.png","attributes":['+trait_type0+','+trait_type1+','+trait_type2+','+trait_type3+','+trait_type4+']}')


    elif len(rfd['attributes']) == 6:
        trait_type0 = str(rfd['attributes'][0]).replace(' ', '').replace("'", '"')
        trait_type1 = str(rfd['attributes'][1]).replace(' ', '').replace("'", '"')
        trait_type2 = str(rfd['attributes'][2]).replace(' ', '').replace("'", '"')
        trait_type3 = str(rfd['attributes'][3]).replace(' ', '').replace("'", '"')
        trait_type4 = str(rfd['attributes'][4]).replace(' ', '').replace("'", '"')
        trait_type5 = str(rfd['attributes'][5]).replace(' ', '').replace("'", '"')

        f=open("./hero/"+str(i+1),'w')
        f.write('{"name":"GalacticApe Hero #'+str(i+1)+'","image":"https://raw.githubusercontent.com/galacticapeheroNFT/galacticapeheroNFT/main/galacticapeshero/hero/'+str(i+1)+'.png","attributes":['+trait_type0+','+trait_type1+','+trait_type2+','+trait_type3+','+trait_type4+','+trait_type5+']}')

    elif len(rfd['attributes']) == 7:
        trait_type0 = str(rfd['attributes'][0]).replace(' ', '').replace("'", '"')
        trait_type1 = str(rfd['attributes'][1]).replace(' ', '').replace("'", '"')
        trait_type2 = str(rfd['attributes'][2]).replace(' ', '').replace("'", '"')
        trait_type3 = str(rfd['attributes'][3]).replace(' ', '').replace("'", '"')
        trait_type4 = str(rfd['attributes'][4]).replace(' ', '').replace("'", '"')
        trait_type5 = str(rfd['attributes'][5]).replace(' ', '').replace("'", '"')
        trait_type6 = str(rfd['attributes'][6]).replace(' ', '').replace("'", '"')

        f=open("./hero/"+str(i+1),'w')
        f.write('{"name":"GalacticApe Hero #'+str(i+1)+'","image":"https://raw.githubusercontent.com/galacticapeheroNFT/galacticapeheroNFT/main/galacticapeshero/hero/'+str(i+1)+'.png","attributes":['+trait_type0+','+trait_type1+','+trait_type2+','+trait_type3+','+trait_type4+','+trait_type5+','+trait_type6+']}')

