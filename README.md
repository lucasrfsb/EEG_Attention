# EEG_Attention

## This project goal is to make a attention identification using EEG signals during arithmetic tasks vs rest situation

## Energy of Fourier Transform of each electrode was acquired and splited in 5 frequency bands

## After that Machine Learning techniques were used to make the attention identification

## 94% of accuracy was achived

## project in dev branch

Dataset available in : EEG During Mental Arithmetic Tasks https://physionet.org/content/eegmat/1.0.0/ 

EEG_ENERGY.py is the Fourier Transform and energy acquirer

Exports energy of electrodes to csv -> frequency_parameters.csv

Manually added parameters labels in frequency_parameters.csv

After that two classifiers are applied using those parameters: Support Vector Machine and Random Forest

Attention identification with Machine Learning algorithms in Attention_ML_Model_20_electrodes.ipynb 
