#Tries to estimate tier of broadcast
#Note: for matches like the World Championship match, where only two people play, this doesn't work.
hrt=int(input("Highest rated player="))
lrt=int(input("Lowest rated player="))
tp=int(input("Number of titled players(GM/IM/FM/CM/WGM/WIM/WFM/WCM)="))
if tp==0:
    print("Normal tier.")
else:
    GM=int(input("Number of GM/WGMs="))
    if GM>=5:
        print("Best tier.")
    else:    
        IM=int(input("Number of IM/WIMs="))
        IMcutoff=(5-GM)*2
        if IM>=IMcutoff:
            print("High Tier.")
        else:
            FM=int(input("Number of FM/WFMs="))
            FMcutoff=(IMcutoff-IM)*2
            if FM>=FMcutoff:
                print("High tier.")
            else:
                CM=tp-(GM+IM+FM)
                CMcutoff=(FMcutoff-FM)*2
                if CM>=CMcutoff:
                    print("High tier.")
                elif tp>0:
                    print("Normal tier.")
                else:
                    medianrt=(hrt+lrt)/2
                    if medianrt>=1700:
                        print("Normal tier.")
                    else:
                        print("No point making the broadcast, but if you want to do it anyways, make it at normal tier.")
