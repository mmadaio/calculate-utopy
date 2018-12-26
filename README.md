# calculate-utopy
A set of scripts for calculating stochastic likelihood of increase ("utopy") for real-valued time-series. Based on Sinha (2016)[https://www.researchgate.net/profile/Tanmay_Sinha/publication/309735539_Cognitive_Correlates_of_Rapport_Dynamics_in_Longitudinal_Peer_Tutoring/links/5919b7450f7e9b1db6527dea/Cognitive-Correlates-of-Rapport-Dynamics-in-Longitudinal-Peer-Tutoring.pdf] and used in several papers on analyzing dynamics of peer rapport in collaborative learning settings (Madaio et al., 2017)[https://idp.springer.com/authorize/casa?redirect_uri=https://link.springer.com/article/10.1007/s11412-017-9266-6&casa_token=06yQNsN5T9kAAAAA:V7HKFN33HAvKp9qdcS39M38S0CqTD7QHZ7SRdB1aGyyIkvZ_AxkzSLrkt_p1YlEC3N8-sn24JSHLeuT0lQ], (Madaio et al., 2018)[http://www.justinecassell.com/publications/ICLS_2018.pdf].


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