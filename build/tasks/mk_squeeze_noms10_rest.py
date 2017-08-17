import os

from scan import Scan


sc=Scan('job_mksqueeze_noms10.madx','squeeze_noms10',
        bbb=[170,320,360,370,480])

sc.mk_cases()
sc.exe_condor()
