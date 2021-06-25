import numpy as np
from scipy.fft import fft, fftfreq

import pandas as pd
import csv
import matplotlib.pyplot as plt

import scipy
from pylab import *

df_multi_rest=pd.read_csv('dataset_arith_rest_csv/Subject00_2.csv', sep=',',header=None)
# df2_multi_arith=pd.read_csv('f3_cz_arith.csv', sep=',',header=None)

df_rest_fp1=df_multi_rest.iloc[ : , 0:1 ]

print (df_rest_fp1)

# df_arith_fp1=df2_multi_arith.iloc[ : , 1 ]
data_size = 30000
data_step = 15000
data_slices = round(data_size/data_step)

slices_rest_fp1=np.zeros((data_step,data_slices))

#Slice dataset to get more samples
cont = 0
line = 1
while cont < data_slices:
	slices_rest_fp1[ : , cont]= df_rest_fp1[ line : (line+data_step) ]
	line = line + data_step
	cont = cont + 1
print (slices_rest_fp1)
print (slices_rest_fp1.shape)
##

Y_fp1_rest=np.zeros(( round(data_step/2 + 1) ,data_slices))
cont = 0
while cont < data_slices:
	Y_fp1_rest [ : , cont]= rfftn( slices_rest_fp1[ : , cont] )
	ps_fp1_rest = np.abs(Y_fp1_rest)**2
	cont = cont + 1
print (Y_fp1_rest)
print ("Y_fp1_rest.shape = ", Y_fp1_rest.shape)
print (ps_fp1_rest)
print (ps_fp1_rest.shape)
##

Energy_rest_fp1 = np.zeros((5,data_slices))
N_=len(ps_fp1_rest)

i=0
#PSD FP1
freq_before_alfa = round(N_ * 0.5 / 500)
freq_alfa_start = round(N_ * 7 / 500)
freq_alfa_stop = round(N_ * 12 / 500)
freq_low_beta_stop = round(N_ * 20/ 500)
freq_high_beta_stop = round(N_ * 30 / 500)
freq_gamma = round(N_ * 60 / 500)

before_alfa_range = np.arange(freq_before_alfa, freq_alfa_start, 1)
alfa_range = np.arange(freq_alfa_start, freq_alfa_stop, 1)
low_beta_range = np.arange(freq_alfa_stop, freq_low_beta_stop, 1)
high_beta_range = np.arange(freq_low_beta_stop, freq_high_beta_stop, 1)
gamma_range = np.arange(freq_high_beta_stop, freq_gamma, 1)

cont = 0
while cont < data_slices:
	Energy_rest_fp1[ 0 , cont] = ps_fp1_rest[before_alfa_range, cont].sum()
	Energy_rest_fp1[ 1 , cont] = ps_fp1_rest[alfa_range, cont].sum() 
	Energy_rest_fp1[ 2 , cont] = ps_fp1_rest[low_beta_range, cont].sum() 
	Energy_rest_fp1[ 3 , cont] = ps_fp1_rest[high_beta_range, cont].sum() 
	Energy_rest_fp1[ 4 , cont] = ps_fp1_rest[gamma_range, cont].sum() 
	cont = cont + 1

print ("ENERGY: ")
print(Energy_rest_fp1)
print(Energy_rest_fp1.shape)
Energy_rest_fp1 = Energy_rest_fp1.transpose()
np.savetxt("arith_energy_fp1_2_slices.csv", Energy_rest_fp1, delimiter=" ")

# print ("ENERGY: ")
# print(Energy_rest_fp1[ 0 , 0]) 
# print(Energy_rest_fp1[ 1 , 0]) 
# print(Energy_rest_fp1[ 2 , 0] )
# print(Energy_rest_fp1[ 3 , 0]) 
# print(Energy_rest_fp1[ 4 , 0] )



# print("========PSD FP1 threshold========")
# print("arith_before_alfa = ",arith_before_alfa)
# print("rest_before_beta= ",rest_before_alfa)
# print("arith_alfa = ",arith_alfa)
# print("rest_alfa = ",rest_alfa)
# print("arith_low_beta = ",arith_low_beta)
# print("rest_low_beta = ",rest_low_beta)
# print("arith_high_beta = ",arith_high_beta)
# print("rest_high_beta = ",rest_high_beta)
# print("arith_after_beta = ",arith_after_beta)
# print("rest_after_beta = ",rest_after_beta)
# print("=============================")
