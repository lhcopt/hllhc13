b5=list(range(6000,1000,-200)+range(1000,490,-10))
b8=range(10000,3000,-500)
b2=range(0,100,100/len(b8))
b8+=[3000]*(len(b5)-len(b8))
b2+=[100]*(len(b5)-len(b2))
bbb=zip(b5,b8,b2)


for b5,b8,b2 in bbb:
    print "exec,mkoptics(%s,%s,%s);"%(b5,b8,b2)




