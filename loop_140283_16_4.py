#!/usr/bin/env python
####################################################
#
# Author: M Joyce
#
####################################################
import subprocess
import sys
import numpy as np
import glob

def ffmt(n):
	return "%1.5f"%n

# ## needs to have <<FEATURES>>
run_full_grid = False 
if run_full_grid:
	masses = np.arange(0.7,0.9,0.01)
	max_ages = [15]*len(masses)
	Y_in = [0.245]
	Z_in= [0.00004,0.00005,0.00006,0.00007,0.00008,0.00009]
	alpha = [1.4,1.6,1.8,2.0]
else:
	masses =[0.79]
	max_ages = [14]
	Z_in =[0.0002]
	Y_in =  [0.245]
	alpha = [1.6]



## for option (3), define variables 
template_inlist_name = 'inlist_HD_r4' ## name of your template inlist

## don't worry too much about this definition, just make sure it matches the value assigned in "inlist"
new_inlist_name = 'inlist_temp' ## blank parameter; doesn't matter

                
import time

for i in range(len(alpha)):
	a = alpha[i]
   	for j in range(len(masses)):
		m = masses[j]
		max_age =max_ages[j] 
		for v in range(len(Z_in)):
            		z = Z_in[v]
            		for w in range(len(Y_in)):
                		y= Y_in[w]
                               	subprocess.call(r"cp " + template_inlist_name+ " "          + new_inlist_name, shell=True)
                		subprocess.call(r"sed -i 's/<<MASS>>/"+         ffmt(m)+"/g' "      + new_inlist_name, shell=True)
                		subprocess.call(r"sed -i 's/<<METALLICITY>>/"+         ffmt(z)+"/g' "      + new_inlist_name, shell=True)
                		subprocess.call(r"sed -i 's/<<ALPHA>>/" +ffmt(a) +"/g' " +new_inlist_name, shell=True)
                		subprocess.call(r"sed -i 's/<<HELIUM>>/" +ffmt(y) +"/g' " +new_inlist_name, shell=True)
				subprocess.call(r"sed -i 's/<<MAX_AGE>>/" +ffmt(max_age) +"/g' " +new_inlist_name, shell=True)
                		subprocess.call("\
						export MESA_DIR=/avatar/janett/MESA/mesa-r12778; \
                                    		export MESASDK_ROOT=/avatar/janett/MESA/mesasdk; \
                               			source $MESASDK_ROOT/bin/mesasdk_init.sh; \
   				        	./rn", shell=True)
