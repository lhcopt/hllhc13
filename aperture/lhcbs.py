# 50A MQM 4.5K
# 50L MQM 1.9K
# 53  Q1 1.9 K
# 63  Q2-3, Q4-Q5
# 69  D2
# 74  D1 DFBX

from collections import namedtuple

from numpy import *

_bs=namedtuple('BeamScreen','name,b_id,cb_od,cb_tol,bs_tk,bs_ro,bs_go,bs_ri,bs_gi,length'.split(','))

class BeamScreen(_bs):
  def mk_bs_tol(self):
     return (self.bs_ro-(self.bs_tk*2)-self.bs_ri)/2,\
            (self.bs_go-(self.bs_tk*2)-self.bs_gi)/2


d="""\
'50A' 50 53 0.35 1.0+0.075 48.5 38.9 44.0 34.3 314
'50L' 50 53 0.35 0.6+0.075 48.5 38.9 45.1 35.3 365
'53' 53 57 0.50 0.6+0.075 51.3 41.7 47.7 37.9 71
'63' 62.98 66.5 0.38 0.6+0.075 61.4 51.8 57.8 48.0 513
'69' 69.08 73 0.74 0.6+0.075 67.1 57.5 62.6 52.8 273
'74' 74 78 0.78  0.6+0.075 72.0 62.3 67.4 57.6 68"""

bslist=[BeamScreen(*map(eval,dd.split())) for dd in d.splitlines()]

bs50A=BeamScreen(name='50A', b_id=50, cb_od=53, cb_tol=0.35, bs_tk=1.075, bs_ro=48.5, bs_go=38.9, bs_ri=44.0, bs_gi=34.3, length=314),
bs50L=BeamScreen(name='50L', b_id=50, cb_od=53, cb_tol=0.35, bs_tk=0.675, bs_ro=48.5, bs_go=38.9, bs_ri=45.1, bs_gi=35.3, length=365),
bs53=BeamScreen(name='53', b_id=53, cb_od=57, cb_tol=0.5, bs_tk=0.675, bs_ro=51.3, bs_go=41.7, bs_ri=47.7, bs_gi=37.9, length=71),
bs63=BeamScreen(name='63', b_id=62.98, cb_od=66.5, cb_tol=0.38, bs_tk=0.675, bs_ro=61.4, bs_go=51.8, bs_ri=57.8, bs_gi=48.0, length=513),
bs69=BeamScreen(name='69', b_id=69.08, cb_od=73, cb_tol=0.74, bs_tk=0.675, bs_ro=67.1, bs_go=57.5, bs_ri=62.6, bs_gi=52.8, length=273),
bs74=BeamScreen(name='74', b_id=74, cb_od=78, cb_tol=0.78, bs_tk=0.675, bs_ro=72.0, bs_go=62.3, bs_ri=67.4, bs_gi=57.6, length=68)


for bs in bslist:
    print bs.name,bs.mk_bs_tol()

