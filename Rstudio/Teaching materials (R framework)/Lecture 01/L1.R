#R as an Object-Oriented Language
#To understand computations in R, two guiding principles are useful:

#     Everything that exists is an object.
#     Everything that happens is a function call.

#Help
#It’s essential to know how to use help functions in R:
help.start()         #Opens the help system in HTML format.
help(mean)           #Provides help for the specific function
?mean:             #An alternative way to get help for mean
help("for"): #Retrieves help on reserved words and special characters (e.g., TRUE, FALSE, NA)
help.search("mean"): #Searches for the string “mean” throughout the documentation.
??mean: #Another way to search for “mean” in the documentation.

  
  
  Workspace
getwd():              #Retrieves the current working directory.
setwd():              #Changes the working directory.
  #Example for Windows: setwd("c:/CorsoR")
ls():                 #Lists the objects present in the workspace.
rm():                 #Deletes one or more specified objects from the workspace.
rm(list=ls()):        #Removes all objects from the workspace. DANGEROUS COMMAND!

# case sensitive
  