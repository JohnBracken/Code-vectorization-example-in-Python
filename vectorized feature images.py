#####################################################################################
#CODE SEGMENT:  Code vectorization for applying functions to multiple portions      #
# of a matrix at the same time without using loops. A matrix is created             #
# and then broken up into 2x2 cells.  The mean is calculated in each cell.          #
#This creates a matrix of means.                                                    #
#####################################################################################




###################
#LIBRARIES/MODULES#
###################

#Import the numeric python library.
import numpy as np





#Create a 6x8 matrix of the numbers 0-47 in order, starting from the top left.
matrix = np.arange(48).reshape(6,8)


#Split the matrix after every two rows in the horizontal direction.  Convert it back to numpy matrix
#format
matrix_horiz=np.split(matrix, matrix.shape[0]/2, axis = 0)
matrix_horiz=np.array(matrix_horiz)


#We now have a matrix containing 3 2x8 matrices.  Split each of these matrices after
#every two columns.  This will generate a matrix a new 4x3 matrix containing 2x2 matrix cells.
matrix_cells=np.split(matrix_horiz, matrix.shape[1]/2, axis = 2)
matrix_cells=np.array(matrix_cells)



#Calculate the mean in each cell of the matrix and then generate a matrix of means.
#Note that in the matrix of cells, the first dimension is the number of rows occupied by all the cells,
#The 2nd dimension(index) is the number of columns occupied by all the cells, and the last two dimensions
#Are the number of rows and columns of each cell.  Therefore, we need to calculate the mean along the
#last two axes to get the mean of each cell.
mean_image =np.mean(matrix_cells,axis=(2,3))



#Transpose the resulting mean image to show the means coinciding correctly with the positions of the
#2x2 cells in the original matrix.
mean_image = np.transpose(mean_image)



#Print the orginal matrix and the matrix of 2x2 cell means.
print(matrix)
print(mean_image)






































