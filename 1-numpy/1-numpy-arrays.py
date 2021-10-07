import numpy as np

# python list
my_list = [1, 2, 3]
print(str(type(my_list)) + ' - ' + str(my_list))

print('\n')

# numpy array
my_array = np.array(my_list)
print(str(type(my_array)) + ' - ' + str(my_array))

print('\n\n')

# python list of lists
my_list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(str(type(my_list_of_lists)) + '\n' + str(my_list_of_lists))

print('\n')

# numpy matrix
my_matrix = np.array(my_list_of_lists)
print(str(type(my_matrix)) + '\n' + str(my_matrix))

print('\n\n')

# numpy generated array from 0 to 10
my_array = np.arange(0, 11)
print(str(type(my_array)) + '\n' + str(my_array))

print('\n')

# numpy generated array from 0 to 10 with a step size of two
my_array = np.arange(0, 11, 2)
print(str(type(my_array)) + '\n' + str(my_array))

print('\n\n')

# numpy generated array of zeros
my_array = np.zeros(3)
print(str(type(my_array)) + '\n' + str(my_array))

print('\n')

# numpy matrix of zeros, the first value as the rows and the second one as the columns
my_matrix = np.zeros((5, 5))
print(str(type(my_matrix)) + '\n' + str(my_matrix))

print('\n\n')

# numpy generated array of ones
my_array = np.ones(3)
print(str(type(my_array)) + '\n' + str(my_array))

print('\n')

# numpy matrix of ones, the first value as the rows and the second one as the columns
my_matrix = np.ones((5, 5))
print(str(type(my_matrix)) + '\n' + str(my_matrix))

# NOTE: there's only zeros and ones functions on numpy

print('\n\n')

# numpy array of 10 evenly spaced values between 0 and 5
my_array = np.linspace(0, 5, 10)
print(str(type(my_array)) + '\n' + str(my_array))

print('\n')

# square numpy matrix filled with zeros and just ones on the diagonal
my_matrix = np.eye(5)
print(str(type(my_matrix)) + '\n' + str(my_matrix))

print('\n')

# reshaping an 25 lenght array to a 5x5 matrix
my_array = np.arange(0, 25)
print(str(type(my_array)) + '\n' + str(my_array))

print('\n')

my_matrix = my_array.reshape(5, 5)
print(str(type(my_matrix)) + '\n' + str(my_matrix))

print('\n')

# returning the higher value from any array/matrix
print(my_matrix.max())

# returning the lower value from any array/matrix
print(my_matrix.min())

print('\n')

# returning the index from the higher value from any array/matrix
print(my_matrix.argmax())

# returning the index from the lower value from any array/matrix
print(my_matrix.argmin())

print('\n')

# returning the shape of a array/matrix
print(my_array.shape)
print(my_matrix.shape)

# returning the datatype of a array/matrix
print(my_array.dtype)
print(my_matrix.dtype)
