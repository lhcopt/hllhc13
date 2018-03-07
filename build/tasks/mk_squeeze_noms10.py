import os

from scan import Scan


sc=Scan('job_mksqueeze_noms10.madx','squeeze_noms10',
        bbb=list(range(1000,140,-10)))

sc.mk_cases()
#sc.exe_condor()
