install.packages("clickstream")
library(clickstream)

getwd()
setwd("~/R Projects/RAPT/utopy/input/session_level")




temp = list.files(pattern="*.csv")   # Finds all .csv's in that folder

for (i in 1:length(temp)){  # for each csv
  print(temp[i])
  cls <- readClickstreams(file = temp[i], sep = ",", header = TRUE)  # reads it as a time-series 
  name <- gsub(".csv", "", temp[i])
  name1 = paste("~/RAPT/utopy/TPM_output/", name, sep="")  # pre-pends transition probability matrix (TPM) output filepath
  name2 = paste("~/RAPT/utopy/graph_output/", name, sep="") # pre-pends graph output folder filepath
  r= t(cls)
  rapport = (r[1])
  rapport = as.integer(unlist(rapport))
  line_plot = paste(name2, "_line-plot.png", sep="")  # Plots time-series as line plot
  png(line_plot,width=800,height=350)
  plot(rapport, type="o",ylim=c(1,7))
  dev.off()
  
  
  ## Fit Markov Chain  
 
   # summary(cls)
  mc <- fitMarkovChain(cls)
  #summary(mc)
  #print(mc)
  mc_table <- mc@transitions[[1]]
  # print(mc_table)
  
  mc_plot = paste(name2, "_graph.png", sep="")  # Plots the transition probability graphs
  png(mc_plot,width=800,height=350)
  plot(mc)
  dev.off()
  new <- paste(name1, "_TPM.csv", sep="") # Writes each TPM as a new csv to the TPM output folder
  write.table(as.data.frame(mc_table),file=new, col.names = NA, sep=",")
}
