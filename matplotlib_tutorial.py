from matplotlib import pyplot as plt

# plt.plot([1,2,3],[2,5,7])
# plt.title("random Data") #to give the plot a heading
# plt.xlabel("This is x")
# plt.ylabel("This is y")
# plt.show()

'''The above code will display a plot with the title "random Data" and the x and y axis labelled as "This is x" and "This is y" respectively.
__________________________________________'''

# x=[1,5,4]
# y=[23,45,89]
# x2=[3,7,3]
# y2=[5,8,9]

# plt.plot(x,y,label='first',linewidth=2)
# plt.plot(x2,y2,label="second")
# plt.legend()
# plt.show()
'''The above code will display a plot with two lines. The first line is plotted using the x and y values and the second line is plotted using the x2 and y2 values.
 _______________________________________________'''

# Histogram

x=[28, 45, 22, 34, 56, 20, 42, 30, 51, 29, 39, 25, 48, 55, 37, 41, 19, 59, 31, 26, 49, 36, 40, 54, 23, 33, 47, 18, 58, 24, 38, 21, 52, 32, 57, 35, 50, 46, 27, 44, 60, 43, 53, 19, 22, 58, 30, 38, 49, 55, 40, 46, 31, 23, 37, 41, 28, 52, 24] #input value

plt.hist(x,bins=5,ec="red")#ec=edge color

plt.xlabel("age")
plt.ylabel("count")
plt.title("Population Age count")

plt.show()

