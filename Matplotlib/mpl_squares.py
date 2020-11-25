#Importing matplotlib
import matplotlib.pyplot as plt

#input values
input_values = [1,2,3,4,5,6]
squares = [1,4,9,16,26,36]

#plotting
fig, ax = plt.subplots()
ax.set_facecolor((.12,.12,.12))
ax.plot(input_values, squares, linewidth=1.5)

#setting up the title
ax.set_title("Graph of square numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=15)
ax.set_ylabel("Squares", fontsize=15)

#displaying the graph
plt.show()
