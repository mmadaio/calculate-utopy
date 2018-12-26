# calculate-utopy
A set of scripts for calculating stochastic likelihood of increase ("utopy") for real-valued time-series. Based on Sinha (2016)[https://www.researchgate.net/profile/Tanmay_Sinha/publication/309735539_Cognitive_Correlates_of_Rapport_Dynamics_in_Longitudinal_Peer_Tutoring/links/5919b7450f7e9b1db6527dea/Cognitive-Correlates-of-Rapport-Dynamics-in-Longitudinal-Peer-Tutoring.pdf]


# Process

1. The TPM_calculator.R takes a set of time-series of integer values and generates a transition probability matrix for each time-series.
	#### Input expected: 
	1. Folder of csv files, each with a single row, with each cell being a new value for the time series.
	#### Output generated: 
	1. Line-plots as png
	2. Transition graphs as png
	3. Transition probability matrices (TPM) as csv

2. The Utopy_calculator.py takes a set of transition probability matrices and computes a utopy score for each matrix, compiling them into a single output file.
	#### Input expected: 
	1. Folder of csv files, each a transition probability matrix, with the first row and first column being the values (here, rapport: from 1-7, though not every file contains all 7 values)
	#### Output generated: 
	1. Single output csv file containing the utopy score for each unit of aggregation specified, here: Dyad > Session > Period.