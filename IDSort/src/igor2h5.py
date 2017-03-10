# Copyright 2017 Diamond Light Source
# 
# Licensed under the Apache License, Version 2.0 (the "License"); 
# you may not use this file except in compliance with the License. 
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, 
# software distributed under the License is distributed on an 
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, 
# either express or implied. See the License for the specific 
# language governing permissions and limitations under the License.



'''
Created on 14 Mar 2014

A small script to help change data files collected in Igor on the measurement bench 
into hdf5 file which can be compared with in the shimming steps.

@author: gdy32713
'''
import numpy as np
import h5py
from scipy import signal

'''nperiods=109
nskip=8
n_stp = 20
n_s_stp = 2501

Energy = 3.0  #ideally needs to be tunable. Is a machine parameter. Would need a new Machine Class
Const = (0.03/Energy)*1e-2  # appears to be defining 10^5eV...(Includes random 1e4 B factor)
c=2.9911124e8 #The speed of light. For now.
Mass =0.511e-3
Gamma=Energy/Mass

f=h5py.File('/home/gdy32713/DAWN_stable/optid/Opt-ID/IDSort/src/v2/2015test.h5','r')

Bfields=f['id_Bfield_perfect']

trajectories=f['id_trajectory_perfect']

detrended_trajectories=signal.detrend(trajectories[:,:,:,:],axis=2)
a=np.gradient(detrended_trajectories[0,0,:,0])
b=np.gradient(detrended_trajectories[0,0,:,1])
w=np.vstack((a,b))
w=np.square(np.transpose(w))


trap_w = np.roll(w,1,0)
trap_w[0,:] = 0.0
trap_w= (trap_w+w)*1e-3*1/2
    
ph=np.cumsum(trap_w[:,0]+trap_w[:,1])/(2.0*c)

ph2=(1*1e-3/(2.0*c*Gamma**2))*np.arange(n_s_stp)+ph
    
    
v1=(n_stp/2)*np.arange(2*nperiods-1*nskip)+n_s_stp/2-nperiods*n_stp/2+(nskip-1)*n_stp/4
v2=ph2[v1[0]:v1[-1]+n_stp/2:n_stp/2]
            
            
    #'linear fit'
A=np.vstack([v1,np.ones(len(v1))]).T
    
m,intercept=np.linalg.lstsq(A, v2)[0]
Omega0=2*np.pi/(m*n_stp)
    
v2=ph[v1[0]:v1[-1]+n_stp/2:n_stp/2]
    
        
    #'fit function'
A=np.vstack([v1,np.ones(len(v1))]).T
    
m,intercept=np.linalg.lstsq(A, v2)[0]

phfit=intercept+m*v1
    
    
ph=v2-phfit
pherr=np.sum(ph**2)*Omega0**2
pherrnew=ph*Omega0*360.0/(2.0*np.pi)
    
pherr=np.sqrt(pherr/(4*nperiods+1-2*nskip))*360.0/(2.0*np.pi)





fw=h5py.File('000shim6phasetest.h5','w')
fw.create_dataset('detrended trajectories',data=detrended_trajectories)
fw.create_dataset('diff',data=a)
fw.create_dataset('w', data=w)
fw.create_dataset('ph', data=ph)
fw.create_dataset('ph2', data=ph2)
fw.create_dataset('v1', data=v1)
fw.create_dataset('v2', data=v2)
fw.create_dataset('pherr', data=pherr)
fw.create_dataset('pherrnew', data=pherrnew)

fw.close()
'''
#Input Files in the format "Bx0C,Bz0C,Bs0C", copied out of Igor
'''
x0z0=np.genfromtxt('/home/gdy32713/shimming/I02J/X0Z0.bfield')
x1z0=np.genfromtxt('/home/gdy32713/shimming/I02J/X1Z0.bfield')
x2z0=np.genfromtxt('/home/gdy32713/shimming/I02J/X2Z0.bfield')
x3z0=np.genfromtxt('/home/gdy32713/shimming/I02J/X3Z0.bfield')
x4z0=np.genfromtxt('/home/gdy32713/shimming/I02J/X4Z0.bfield')
x0z1=np.genfromtxt('/home/gdy32713/shimming/I02J/X0Z1.bfield')
x1z1=np.genfromtxt('/home/gdy32713/shimming/I02J/X1Z1.bfield')
x2z1=np.genfromtxt('/home/gdy32713/shimming/I02J/X2Z1.bfield')
x3z1=np.genfromtxt('/home/gdy32713/shimming/I02J/X3Z1.bfield')
x4z1=np.genfromtxt('/home/gdy32713/shimming/I02J/X4Z1.bfield')
'''

all_data=np.zeros((1,1,2221,3))
all_data[0,0,:,:]=np.genfromtxt('/home/tow31676/id_shim_j02/shim16/X0Z0.bfield')
#all_data[1,0,:,:]=np.genfromtxt('/home/tow31676/id_shim_j02/shim4/X1Z0.bfield')
#all_data[2,0,:,:]=np.genfromtxt('/home/tow31676/id_shim_j02/shim4/X2Z0.bfield')
#all_data[3,0,:,:]=np.genfromtxt('/home/tow31676/id_shim_j02/shim4/X3Z0.bfield')
#all_data[4,0,:,:]=np.genfromtxt('/home/tow31676/id_shim_j02/shim4/X4Z0.bfield')
#all_data[0,1,:,:]=np.genfromtxt('/home/tow31676/id_shim_j02/shim4/X0Z1.bfield')
#all_data[1,1,:,:]=np.genfromtxt('/home/tow31676/id_shim_j02/shim4/X1Z1.bfield')
#all_data[2,1,:,:]=np.genfromtxt('/home/tow31676/id_shim_j02/shim4/X2Z1.bfield')
#all_data[3,1,:,:]=np.genfromtxt('/home/tow31676/id_shim_j02/shim4/X3Z1.bfield')
#all_data[4,1,:,:]=np.genfromtxt('/home/tow31676/id_shim_j02/shim4/X4Z1.bfield')
filname='/home/tow31676/id_shim_j02/shim16/shim16.meas.h5'
f=h5py.File(filname,'w')
f.create_dataset('id_Bfield',data=all_data)
f.close()