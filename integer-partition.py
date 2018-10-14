
# coding: utf-8

# In[1]:


def int_parti(row,column):

    #Defining matrix with row and column size

    T=[0]*row
    for i in range(row):
        T[i]=[0]*column

    #Main code follows

    for i in range(row):
        for j in range(column):
            if(i==0 and j==0):
                T[i][j]=1
            elif(i>j):
                T[i][j]=T[i-1][j]
            else:
                T[i][j]=T[i-1][j]+T[i][j-i]

    #printing the Matrix

    for i in range(row):
        print(T[i][:])

    return T

Y=int_parti(6,7)
