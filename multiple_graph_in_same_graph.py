import matplotlib.pyplot as plt
# note :- we can only create 4 graph
plt.figure()  # want to create a new graph, call figure() again.
# create some data
x_series = [0, 1, 2, 3, 4, 5]
y_series_1 = [x ** 2 for x in x_series]
y_series_2 = [x ** 3 for x in x_series]

# plot the two lines
# To add multiple lines to a graph, simply call plot() again
plt.subplot(221)
plt.plot(x_series, y_series_1)
plt.plot(x_series, y_series_2)
plt.grid(True)

# add in labels and title
plt.subplot(222)
plt.xlabel("Small X Interval")
plt.ylabel("Calculated Data")
plt.title("Our Fantastic Graph")
# add limits to the x and y axis
plt.xlim(0, 6)
plt.ylim(-5, 80)
plt.plot(x_series, y_series_1, label="x^2")
plt.plot(x_series, y_series_2, label="x^3")
plt.grid(True)

plt.subplot(223)
plt.plot(x_series, y_series_1, label="x^2")
plt.plot(x_series, y_series_2, label="x^3")
plt.legend(loc="upper left")
plt.grid(True)

plt.subplot(224)
plt.plot(x_series, y_series_1, label="x^2")
plt.plot(x_series, y_series_2, label="x^3")
plt.legend(loc="upper left")
plt.grid(True)


# formatting
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,wspace=0.35)
plt.show()
