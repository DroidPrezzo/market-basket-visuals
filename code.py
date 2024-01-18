# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 


# BAR PLOT
# dataset = pandas.DataFrame(antecedents.2, consequents.2.2, lift, support, confidence)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:

# import statements
import matplotlib.pyplot as plt
# Create a new column for the rule
dataset['Rule'] = dataset['antecedents.2'] + ' -> ' + dataset['consequents.2.2']

# Plot the bar chart
fig, ax = plt.subplots(figsize=(20, 8))
dataset.plot(x='Rule', y=['support', 'confidence', 'lift'], kind='barh', ax=ax)

#specify plot title
plt.title('Support, Confidence, and Lift Bar Plot')

# Specify data labels
plt.ylabel('Metric Value')
plt.xlabel('Association Rules')

# Show the plot/graph
plt.show()




# 3D Plot

# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(support, lift, confidence)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:


#Import Statements
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

# Create a scatter plot
ax.scatter(dataset.support, dataset.confidence, dataset.lift, c='r', marker = 'o')

#Set Labels for each axis
ax.set_xlabel('support')
ax.set_ylabel('confidence')
ax.set_zlabel('lift')

# set the title of the plot
ax.set_title('3D plot of Support, Confidence and Lift')

# show the plot
plt.show()
