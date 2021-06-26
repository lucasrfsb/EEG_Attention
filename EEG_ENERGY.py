import numpy as np
from scipy.fft import fft, fftfreq

import pandas as pd
import csv
import matplotlib.pyplot as plt

import scipy
from pylab import *


# df_multi_rest=pd.read_csv('dataset_arith_rest_csv/test_csv.csv', sep=',',header=None)
# df2_multi_arith=pd.read_csv('f3_cz_arith.csv', sep=',',header=None)



def energy_one_sample (sample):


	sample_step = 15000
	fft_size = round(sample_step/2 + 1)


	# data_slices = round(data_size/data_step)

	line_cont = 0
	peace_cont = 0 #column
	peaces = 1 

	# print ("df multi rest \n",df_multi_rest)
	# print ("\ndf multi rest shape ", df_multi_rest.shape)

	np_rest = np.array(df_multi)
	# print("np shape shape",df_multi_rest.shape)

	##FFT

	temp = zeros (( sample_step,1 ))
	Y_rest=  np.zeros(( fft_size , 1 ))
	freq_data = np.zeros (( fft_size , 6 ))

	lines = (sample - 1) * sample_step + 1
	cont = 0

	while cont < 6:
		temp  = np_rest[ lines : (lines + sample_step ) , cont ]
		# print (np_rest[ lines : (lines + data_step - 1), cont  ])
		Y_rest = rfftn(temp)
		ps_rest = np.abs(Y_rest)**2
		freq_data [ 0:fft_size , cont ] = ps_rest
		cont = cont + 1
	##

	# print(temp.shape)
	# print(Y_rest.shape)
	# print ("freq data",freq_data)
	# print (" freq_data shape", freq_data.shape)
	# print(freq_data)

	#ENERGY

	Energy_rest = np.zeros((5,6))
	N_=len(ps_rest)

	i=0

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
	while cont < 6:
		Energy_rest[ 0 , cont] = freq_data[before_alfa_range, cont].sum()
		Energy_rest[ 1 , cont] = freq_data[alfa_range, cont].sum() 
		Energy_rest[ 2 , cont] = freq_data[low_beta_range, cont].sum() 
		Energy_rest[ 3 , cont] = freq_data[high_beta_range, cont].sum() 
		Energy_rest[ 4 , cont] = freq_data[gamma_range, cont].sum() 
		cont = cont + 1

	Energy_rest= Energy_rest.flatten('F')

	print ("ENERGY: ")
	print(Energy_rest)
	print(Energy_rest.shape)

#MAIN


df_multi=pd.read_csv('dataset_arith_rest_csv/Subject00_1.csv', sep=',',header=None)
df_multi=df_multi.iloc[ : , 0:6 ]

rest_sample = 1
rest_sample_max = 6

while rest_sample <= rest_sample_max:
	energy_one_sample (rest_sample)
	rest_sample = rest_sample + 1

df_multi=pd.read_csv('dataset_arith_rest_csv/Subject00_2.csv', sep=',',header=None)
df_multi=df_multi.iloc[ : , 0:6 ]

arith_sample = 1
arith_sample_max = 2

while arith_sample <= arith_sample_max:
	energy_one_sample (arith_sample)
	arith_sample = arith_sample + 1

##