## 	This project extracts frequency energy of a EEG experiment
## 	In this experiment each subject is asked to rest for 3 minutes and then make arithmetic subtractions for 1 minute
##  Sample rate is 500 Hz			
##  Rest data size then is 90k samples
##  Arithmetic data size then is 30k samples 

import numpy as np
from scipy.fft import fft, fftfreq

import pandas as pd
import csv

import scipy
from pylab import *


data_columns = 20 # number of electrodes selected
subjects = 35 # number of subjects in the experiment

freq_bands = 5 # Five bands segmentation was selecteed 
sample_size = 15000 # 15k sample size was chosen, in this situation equivalent to 30 seconds

rest_sample_max = 6 # 90k samples/sample_size
arith_sample_max = 2 # 30k samples/sample_size

proc_data_rest = np.zeros(( subjects*rest_sample_max,data_columns*freq_bands +1 )) # energy vector for rest data
proc_data_arith = np.zeros(( subjects*arith_sample_max,data_columns*freq_bands +1 )) # energy vector for arithmetic data

def energy_one_sample (sample, data_type, subject):

	
	fft_size = round(sample_size/2 + 1) # Fourier transform size

	line_cont = 0
	peace_cont = 0 #column
	peaces = 1 

	np_rest = np.array(df_multi)

	##FFT

	temp = zeros (( sample_size,1 ))
	Y_rest=  np.zeros(( fft_size , 1 )) 
	freq_data = np.zeros (( fft_size , data_columns ))

	lines = (sample - 1) * sample_size + 1
	cont = 0

	while cont < data_columns:  # column by column make fft, save in temp array, calculate energy and save in freq_data
		temp  = np_rest[ lines : (lines + sample_size ) , cont ]
		# print (np_rest[ lines : (lines + data_step - 1), cont  ])
		Y_rest = rfftn(temp)
		ps_rest = np.abs(Y_rest)**2
		freq_data [ 0:fft_size , cont ] = ps_rest
		cont = cont + 1

	##

	#ENERGY

	Energy_rest = np.zeros((freq_bands,data_columns))
	N_=len(ps_rest)

    ## Frequency intervals
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
	while cont < data_columns:  ## Energy_rest will be the final energy vector, each column will be correspondig to electrode and frequency
		Energy_rest[ 0 , cont] = freq_data[before_alfa_range, cont].sum()
		Energy_rest[ 1 , cont] = freq_data[alfa_range, cont].sum() 
		Energy_rest[ 2 , cont] = freq_data[low_beta_range, cont].sum() 
		Energy_rest[ 3 , cont] = freq_data[high_beta_range, cont].sum() 
		Energy_rest[ 4 , cont] = freq_data[gamma_range, cont].sum() 
		cont = cont + 1

	Energy_rest = Energy_rest.flatten('F')

	print(Energy_rest.shape)
	print(proc_data_rest.shape)

	if data_type == 1:
		Energy_rest = np.append( Energy_rest, [0] )
		proc_data_rest [ (sample - 1) + subject * rest_sample_max , 0:(data_columns*5 +1) ] = Energy_rest 
	else:
		Energy_rest = np.append( Energy_rest, [1] )
		proc_data_arith [ (sample - 1) + subject * arith_sample_max , 0:(data_columns*5 +1) ] = Energy_rest	

	print ("ENERGY: ")
	print(Energy_rest)
	print(Energy_rest.shape)

	##


#MAIN

SAMPLE_ = 0

rest_sample = 1
data_type = 1
subject = 0

files_rest = ['Subject00_1.csv' , 'Subject09_1.csv' , 'Subject18_1.csv' , 'Subject27_1.csv',
'Subject01_1.csv' , 'Subject10_1.csv' , 'Subject19_1.csv' , 'Subject28_1.csv',
'Subject02_1.csv' , 'Subject11_1.csv' , 'Subject20_1.csv' , 'Subject29_1.csv',
'Subject03_1.csv' , 'Subject12_1.csv' , 'Subject21_1.csv' , 'Subject30_1.csv',
'Subject04_1.csv' , 'Subject13_1.csv' , 'Subject22_1.csv' , 
'Subject05_1.csv' , 'Subject14_1.csv' , 'Subject23_1.csv' , 'Subject32_1.csv',
'Subject06_1.csv' , 'Subject15_1.csv' , 'Subject24_1.csv' , 'Subject33_1.csv',
'Subject07_1.csv' , 'Subject16_1.csv' , 'Subject25_1.csv' , 'Subject34_1.csv',
'Subject08_1.csv' , 'Subject17_1.csv' , 'Subject26_1.csv' , 'Subject35_1.csv']

for file in files_rest:

	df_multi=pd.read_csv(file, sep=',',header=None)
	df_multi=df_multi.iloc[ : , :-1 ]

	while rest_sample <= rest_sample_max:
		energy_one_sample (rest_sample, data_type, subject)
		rest_sample = rest_sample + 1
		SAMPLE_ = SAMPLE_ + 1
		print("SAMPLE: ", SAMPLE_)
	subject = subject + 1
	rest_sample = 1
		

arith_sample = 1
data_type = 2
subject = 0

files_arith = ['Subject00_2.csv' , 'Subject09_2.csv' , 'Subject18_2.csv' , 'Subject27_2.csv',
'Subject01_2.csv' , 'Subject10_2.csv' , 'Subject19_2.csv' , 'Subject28_2.csv',
'Subject02_2.csv' , 'Subject11_2.csv' , 'Subject20_2.csv' , 'Subject29_2.csv',
'Subject03_2.csv' , 'Subject12_2.csv' , 'Subject21_2.csv' , 'Subject30_2.csv',
'Subject04_2.csv' , 'Subject13_2.csv' , 'Subject22_2.csv' , 
'Subject05_2.csv' , 'Subject14_2.csv' , 'Subject23_2.csv' , 'Subject32_2.csv',
'Subject06_2.csv' , 'Subject15_2.csv' , 'Subject24_2.csv' , 'Subject33_2.csv',
'Subject07_2.csv' , 'Subject16_2.csv' , 'Subject25_2.csv' , 'Subject34_2.csv',
'Subject08_2.csv' , 'Subject17_2.csv' , 'Subject26_2.csv' , 'Subject35_2.csv']

SAMPLE_ = 0 #debug variable

for file in files_arith:

	df_multi=pd.read_csv(file, sep=',',header=None)
	df_multi=df_multi.iloc[ : , :-1 ]

	while arith_sample <= arith_sample_max:
		energy_one_sample (arith_sample, data_type, subject)
		arith_sample = arith_sample + 1
		SAMPLE_ = SAMPLE_ + 1
		print("SAMPLE: ", SAMPLE_)
	subject = subject + 1
	arith_sample = 1

##

## DEBUG

print ("\n PROC DATA REST", proc_data_rest)
print (proc_data_rest.shape)
print ("\n PROC DATA ARITH", proc_data_arith)
print (proc_data_arith.shape)

proc_data = np.concatenate ((proc_data_rest, proc_data_arith))
print ("\nPROC DATA ", proc_data)
print (proc_data.shape)

np.savetxt("frequency_parameters_20_elec.csv", proc_data, delimiter=",") ## save final freqyency parameters in csv file 

##
