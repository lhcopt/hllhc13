import os

from scan import Scan


sc=Scan('job_mksqueeze_lhcb.madx','squeeze2_lhcb',

        bbb=list(range(1000,140,-10)))

sc.mk_cases()
sc.exe_condor(runtime=30*60,out='result.tgz')
