import numpy as npy
import matplotlib.pyplot as plt
from numpy import polyfit


# draw/plot a line chart
def line_chart():
    print("Plot a line chart!")
    # basic settings
    pic_name = input("Name of picture: ")
    x_label = input("Name of x-axis: ")
    y_label = input("Name of y-axis: ")
    line_label = input("Name of line: ")
    # input array: x-axis and y-axis
    arr_x = input(x_label + " data: ")
    arr_y = input(y_label + " data: ")
    in_x = [float(count) for count in arr_x.split()]
    in_y = [float(count) for count in arr_y.split()]
    x = npy.array(in_x)
    y = npy.array(in_y)
    n = len(x)
    # console output messages
    print("Picture's name: %s, len of data: %d" % (pic_name, n))
    # plot settings
    plt.rcParams["figure.figsize"] = (10, 10)
    plt.subplots_adjust(left=0.06, right=0.94, top=0.92, bottom=0.08)
    plt.plot(x, y, label=line_label)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(pic_name)
    plt.legend()
    plt.show()
    #  messages
    print("Done!")


# fitting
def fitting():
    print("Optimize and plot a chart!")
    # basic settings
    pic_name = input("Name of picture: ")
    x_label = input("Name of x-axis: ")
    y_label = input("Name of y-axis: ")
    # input array: x-axis and y-axis
    arr_x = input(x_label + " data: ")
    arr_y = input(y_label + " data: ")
    in_x = [float(count) for count in arr_x.split()]
    in_y = [float(count) for count in arr_y.split()]
    x = npy.array(in_x)
    y = npy.array(in_y)
    n = len(x)
    print("Picture's name: %s, len of data: %d" % (pic_name, n))
    # plot settings
    plt.rcParams["figure.figsize"] = (10, 10)
    plt.subplots_adjust(left=0.06, right=0.94, top=0.92, bottom=0.08)
    output_result = polyfit(x, y, 1)
    # console output message
    print(y_label, " = ", output_result[0], " * ", x_label, " + ", output_result[1])
    # generate picture
    plt.plot(x, output_result[0] * x + output_result[1], "k-")
    plt.plot(x, y, "b--")
    plt.show()
    # messages
    print("Done!")


# draw/plot a pie chart
# TODO: The explode of the pie chart, input methods.
def pie_chart():
    title = input("Input title: ")
    # labels and size input
    input_label = input("Input labels: ").split()
    input_size = input("Input size: ").split()
    input_colors = input("Input colors: ").split()
    # input_explode = input("Input explode: ")
    labels = input_label
    size = input_size
    colors = input_colors
    # explode = (float(count) for count in input_explode.split())
    explode = (0.01, 0.01, 0.05)
    plt.pie(
        size,
        explode=explode,
        labels=labels,
        colors=colors,
        labeldistance=1.2,
        autopct="%3.2f",
        shadow=False,
        startangle=90,
        pctdistance=0.6
    )
    plt.axis("equal")
    plt.title(title)  # show title
    plt.legend()  # show legend
    plt.show()
