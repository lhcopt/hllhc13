import os

from scan import Scan


b5=list(range(6000,1000,-200)+range(1000,490,-10))
b8=range(10000,1500,-500)
b2=range(0,100,100/len(b8))
b8+=[1500]*(len(b5)-len(b8))
b2+=[100]*(len(b5)-len(b2))
bbb=zip(b5,b8,b2)


sc=Scan('job_mkpresqueeze2.madx','presqueeze2a_lhcb',
        b5=b5,b2=b2,b8=b8)

sc.mk_cases()
#sc.exe_local(4)
sc.exe_condor(runtime=30*60,out='result.tgz')
