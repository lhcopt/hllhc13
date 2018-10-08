import os

from scan import Scan


b5=range(6000,30500,500)
b8=[10000]*8+list(range(10000,30500,500))
bbb=zip(b5,b8)


sc=Scan('job_mkvdm.madx','vdm',
        b5=b5,b8=b8)

sc.mk_cases()
#sc.exe_local(4)
sc.exe_condor(runtime=30*60,out='result.tgz')
