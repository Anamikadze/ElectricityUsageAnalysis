Distributional Analysis Using Pandas


## Input Data

File **households.csv** is the earlier file giving data on 1000 households. As before, it has five columns, `id`, `type`, `inc`, `a` and `b`, and there is one row for each household. The `type` variable wasn't used before but it will be important in this exercise. It ranges from 1 to 4 and indicates the demographic type of the household. Here we'll think of it as indicating the region of the country where the household resides. In other studies it could be used to indicate other characteristics, such as the race, gender, or age of the household's head, the size of the household, whether the household lives in an urban or rural area, and so on. In those cases there would be many more than four types.

File **quantities.csv** gives the quantities demanded by each household under the base case and tax policy simulations. It has three columns, one for the household's ID and one each for the household's demands under the base and policy cases: `id`, `qd1` and `qd2`. In case you're curious, it was produced by running the earlier `ind_demand()` function for each equilibrium price and then writing out the output. However, you do not need to do that for this exercise: you should use the provided **quantities.csv** without recalculating it.

## Deliverables

A script called **etr.py** that calculates the effective tax rate (ETR) for each household and then reports the median ETR for the groups indicated below. Then update **results.md** replacing the *TBD* placeholders with your answers to the questions in the file. Please try not to alter the other Markdown in the results.md file: it makes it easier to tell the difference between the questions and answers.

