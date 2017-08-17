#!/usr/bin/env python

import sys
from glob import glob

from numpy import *

from pyoptics import *


def check(t1,t2,i1,i2,name,check='rel',threshold=0):
    v1=t1(name)[i1]
    v2=t2(name)[i2]
    if check=='rel':
      tt=v2/v1-1
    elif check=='abs':
      tt=v2-v1
    if abs(tt)>threshold:
        print("%s %-15s: %8g %8g %-4s %12g"%(name,t1.name[i1],v1,v2,check,tt))

def check_all(tkfn,tnfn):
    print(tkfn,tnfn)
    tk=optics.open(tkfn)
    tn=optics.open(tnfn)
    tkidx=where((tk.l==0)&~(tk//'^D'))[0]
    tnidx=tn.idx_from_namelist(tk.name[tkidx])
    for ii,jj in zip(tkidx,tnidx):
        check(tk,tn,ii,jj,'s','abs',1e-9)
        check(tk,tn,ii,jj,'betx','rel',0.015)
        check(tk,tn,ii,jj,'bety','rel',0.015)
#        check(tk,tn,ii,jj,'x/sqrt(betx)','abs',0.0)
#        check(tk,tn,ii,jj,'y/sqrt(bety)','abs',0.0)
        check(tk,tn,ii,jj,'dx/sqrt(betx)','abs',1e-4)
        check(tk,tn,ii,jj,'dy/sqrt(bety)','abs',1e-4)



tkname='squeeze'
tnname=tkname+'_thin'

tknames=glob(tkname+'/*')
tnnames=glob(tnname+'/*')

for tkname,tnname in sorted(zip(tknames,tnnames)):
 for beam in '12':
  tkfn="%s/twiss_lhcb%s.tfs"%(tkname,beam)
  tnfn="%s/twiss_lhcb%s.tfs"%(tnname,beam)
  check_all(tkfn,tnfn)
