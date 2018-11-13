import numpy as np
import csv
import matplotlib.pyplot as plt

readFilePath = r'C:\Users\Adarsh\Downloads\18100006-eng\ml_18100006.csv'

def estimate_coef(x, y):
    n = np.sign(x)
    m_x = np.mean(x)
    m_y = np.mean(y)
#    x = x.reshape((1, -1))
#    y = y.reshape(1,-1)
    SS_xx = 0
    SS_xy = 0
    SS_xy = np.sum(y * x - n * m_y * m_x)
    SS_xx = np.sum(x * x - n * m_x * m_x)

    #for i in range(1, (n-1)):
        #SS_xy = SS_xy + (y[i]*x[i] - n*m_y*m_x)
        #SS_xx = SS_xx+ (x[i]*x[i] - n*m_x*m_x)
    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x
    return (b_0, b_1)


def plot_regression_line(x, y, b):
	# plotting the actual points as scatter plot
	plt.scatter(x, y, color = "m",
			marker = "o", s = 30)

	# predicted response vector
	y_pred = b[0] + b[1]*x

	# plotting the regression line
	plt.plot(x, y_pred, color = "g")

	# putting labels
	plt.xlabel('x')
	plt.ylabel('y')

	# function to show plot
	plt.show()

def main():
#    food = []
 #   transport = []
  #  shelter = []
   # all_items = []
    #months_count = []
    # row1 = ['date', 'Product Groups', 'Consumer Price Index']

    food = np.array()
    shelter = np.array()
    transport = np.array()
    all_items = np.array()
    months_count =np.array()
    with open(readFilePath, 'r', newline='') as readFile:
        # next(readFile)  # Skip over header in input file.
        readCSV = csv.reader(readFile, delimiter=',')

        i = 1.0
        for row in readCSV:
            if (row[1] in ('All-items')):
                all_items.append(row[2])
                months_count.append(i)
            elif (row[1] in ('Food')):
                food.append(row[2])
            elif (row[1] in ('Shelter')):
                shelter.append(row[2])
            elif (row[1] in ('Transportation')):
                transport.append(row[2])


            i = i+1.0
    all_items = [float(i) for i in all_items]
    print(all_items)

    #all_items = np.asarray(all_items)
    food = np.asarray(food)
    shelter = np.asarray(shelter)
    transport = np.asarray(transport)

    #print(months_count)
    b = estimate_coef(months_count,all_items)
    plot_regression_line(months_count,all_items,b)


if __name__ =="__main__":
    main()