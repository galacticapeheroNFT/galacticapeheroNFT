import os
import sys

for i in range(9999):
    f=open("./"+str(i+1),'r')
    rf = f.read()
    print(rf)
    exec("rfd = dict("+rf+")")
    print(rfd['attributes'])

    if len(rfd['attributes']) == 1:
        trait_type0 = str(rfd['attributes'][0])
        f=open("./"+str(i+1),'w')
        f.write('{"name":"GalacticApe Hero #'+str(i+1)+'","image":"https://raw.githubusercontent.com/galacticapeheroNFT/galacticapeheroNFT/main/galacticapeshero/hero/'+str(i+1)+'.png","attributes":['+trait_type0+']}')

    elif len(rfd['attributes']) == 2:
        trait_type0 = str(rfd['attributes'][0])
        trait_type1 = str(rfd['attributes'][1])
        f=open("./"+str(i+1),'w')
        f.write('{"name":"GalacticApe Hero #'+str(i+1)+'","image":"https://raw.githubusercontent.com/galacticapeheroNFT/galacticapeheroNFT/main/galacticapeshero/hero'+str(i+1)+'.png","attributes":['+trait_type0+','+trait_type1+']}')
        #f.write('{"name": "GalacticApe Hero #'+str(i+1)+'", "attributes": ['+trait_type0+','+trait_type1+'], "image": "https://raw.githubusercontent.com/galacticapeheroNFT/galacticapeheroNFT/main/galacticapeshero/ape/'+str(i+1)+'.png"}')


    elif len(rfd['attributes']) == 3:
        trait_type0 = str(rfd['attributes'][0])
        trait_type1 = str(rfd['attributes'][1])
        trait_type2 = str(rfd['attributes'][2])
        f=open("./"+str(i+1),'w')
        f.write('{"name":"GalacticApe Hero #'+str(i+1)+'","image":"https://raw.githubusercontent.com/galacticapeheroNFT/galacticapeheroNFT/main/galacticapeshero/hero/'+str(i+1)+'.png","attributes":['+trait_type0+','+trait_type1+','+trait_type2+']}')
        #f.write('{"name": "GalacticApe Hero #'+str(i+1)+'", "attributes": ['+trait_type0+','+trait_type1+','+trait_type2+'], "image": "https://raw.githubusercontent.com/galacticapeheroNFT/galacticapeheroNFT/main/galacticapeshero/ape/'+str(i+1)+'.png"}')


    elif len(rfd['attributes']) == 4:
        trait_type0 = str(rfd['attributes'][0])
        trait_type1 = str(rfd['attributes'][1])
        trait_type2 = str(rfd['attributes'][2])
        trait_type3 = str(rfd['attributes'][3])
        f=open("./"+str(i+1),'w')
        f.write('{"name":"GalacticApe Hero #'+str(i+1)+'","image":"https://raw.githubusercontent.com/galacticapeheroNFT/galacticapeheroNFT/main/galacticapeshero/hero/'+str(i+1)+'.png","attributes":['+trait_type0+','+trait_type1+','+trait_type2+','+trait_type3+']}')
        #f.write('{"name": "GalacticApe Hero #'+str(i+1)+'", "attributes": ['+trait_type0+','+trait_type1+','+trait_type2+','+trait_type3+'], "image": "https://raw.githubusercontent.com/galacticapeheroNFT/galacticapeheroNFT/main/galacticapeshero/ape/'+str(i+1)+'.png"}')


    elif len(rfd['attributes']) == 5:
        trait_type0 = str(rfd['attributes'][0])
        trait_type1 = str(rfd['attributes'][1])
        trait_type2 = str(rfd['attributes'][2])
        trait_type3 = str(rfd['attributes'][3])
        trait_type4 = str(rfd['attributes'][4])
        f=open("./"+str(i+1),'w')
        f.write('{"name":"GalacticApe Hero #'+str(i+1)+'","image":"https://raw.githubusercontent.com/galacticapeheroNFT/galacticapeheroNFT/main/galacticapeshero/hero/'+str(i+1)+'.png","attributes":['+trait_type0+','+trait_type1+','+trait_type2+','+trait_type3+','+trait_type4+']}')
        #f.write('{"name": "GalacticApe Hero #'+str(i+1)+'", "attributes": ['+trait_type0+','+trait_type1+','+trait_type2+','+trait_type3+','+trait_type4+'], "image": "https://raw.githubusercontent.com/galacticapeheroNFT/galacticapeheroNFT/main/galacticapeshero/ape/'+str(i+1)+'.png"}')

    elif len(rfd['attributes']) == 6:
        trait_type0 = str(rfd['attributes'][0])
        trait_type1 = str(rfd['attributes'][1])
        trait_type2 = str(rfd['attributes'][2])
        trait_type3 = str(rfd['attributes'][3])
        trait_type4 = str(rfd['attributes'][4])
        trait_type5 = str(rfd['attributes'][5])
        f=open("./"+str(i+1),'w')
        f.write('{"name":"GalacticApe Hero #'+str(i+1)+'","image":"https://raw.githubusercontent.com/galacticapeheroNFT/galacticapeheroNFT/main/galacticapeshero/hero/'+str(i+1)+'.png","attributes":['+trait_type0+','+trait_type1+','+trait_type2+','+trait_type3+','+trait_type4+','+trait_type5+']}')
        #f.write('{"name": "GalacticApe Hero #'+str(i+1)+'", "attributes": ['+trait_type0+','+trait_type1+','+trait_type2+','+trait_type3+','+trait_type4+','+trait_type5+'], "image": "https://raw.githubusercontent.com/galacticapeheroNFT/galacticapeheroNFT/main/galacticapeshero/ape/'+str(i+1)+'.png"}')

    elif len(rfd['attributes']) == 7:
        trait_type0 = str(rfd['attributes'][0])
        trait_type1 = str(rfd['attributes'][1])
        trait_type2 = str(rfd['attributes'][2])
        trait_type3 = str(rfd['attributes'][3])
        trait_type4 = str(rfd['attributes'][4])
        trait_type5 = str(rfd['attributes'][5])
        trait_type6 = str(rfd['attributes'][6])

        f=open("./"+str(i+1),'w')
        f.write('{"name":"GalacticApe Hero #'+str(i+1)+'","image":"https://raw.githubusercontent.com/galacticapeheroNFT/galacticapeheroNFT/main/galacticapeshero/hero/'+str(i+1)+'.png","attributes":['+trait_type0+','+trait_type1+','+trait_type2+','+trait_type3+','+trait_type4+','+trait_type5+','+trait_type6+']}')

        #f.write('{"name": "GalacticApe Hero #'+str(i+1)+'", "attributes": ['+trait_type0+','+trait_type1+','+trait_type2+','+trait_type3+','+trait_type4+','+trait_type5+','+trait_type6+'], "image": "https://raw.githubusercontent.com/galacticapeheroNFT/galacticapeheroNFT/main/galacticapeshero/ape/'+str(i+1)+'.png"}')
