import random
import matplotlib.pyplot as plt
from pixels import *
def point_generator(n,m):

    if n <2 or m <2:
        print("Minimum 2x2 grid")
        return
    
    total_squares = m * n
    matrix = []
    for i in range(0,n+1):
        row=[]
        for j in range(0,m+1):
            if i == 0 or i == n:
                row.append("H")
            else:
                row.append(random.choice(["H","V","D"]))
        matrix.append(row)
    return matrix

def square_reader(matrix):
    n = len(matrix) - 1
    m = len(matrix[0])-1
    squares=[]
    lhs=[]
    rhs=[]
    for i in range(0,n):
        row=[]
        for j in range(0,m):
            square = [matrix[i][j],matrix[i][j+1],matrix[i+1][j],matrix[i+1][j+1]]
            square=''.join(square)
            row.append(square)
        squares.append(row)
    for i in range(0,n):
        tmp_lhs=[matrix[i][0],matrix[i+1][0]]
        tmp_lhs=''.join(tmp_lhs)
        tmp_rhs=[matrix[i][m],matrix[i+1][m]]
        tmp_rhs=''.join(tmp_rhs)
        lhs.append(tmp_lhs)
        rhs.append(tmp_rhs)
        
    return squares, lhs, rhs

""" def square_assembler(squares,matrix,n,m):
    square_matrix=[]
    for i in range(0,n):
        row=[]
        for j in range(0,m):
            row.append(squares[(i*m)+j])
        square_matrix.append(row)
    return square_matrix """

def mosaic_assembler(squares,lhs,rhs):
    final_matrix=[]
    n=len(squares)
    m=len(squares[0])
    for i in range(0,n*9):
        final_matrix.append([])
    for i in range(0,n):
        lhs_pix=squares_dic[lhs[i] + "_LHS"]
        rhs_pix=squares_dic[rhs[i] + "_RHS"]
        for j in range(0,m):
            pixels=squares_dic[squares[i][j]]
            res_y = len(pixels)
            res_x = len(pixels[0])
            for k in range(0,res_y):
                for v in range(0,res_x):
                    final_matrix[(i*(res_y))+k].append(pixels[k][v])
        for w in range(0,9):
            final_matrix[(i*(res_y))+w] = final_matrix[(i*(res_y))+w]+ rhs_pix[w]
            final_matrix[(i*(res_y))+w] = lhs_pix[w] + final_matrix[(i*(res_y))+w]



   
        
    return final_matrix
                    

def full_generation(n,m):
    if n<2 or m<2:
        print("Must be 2x2 grid or larger")
        return
    points=point_generator(n,m)
    squares_data=square_reader(points)
    squares=squares_data[0]
    LHS=squares_data[1]
    RHS=squares_data[2]
    final_matrix=mosaic_assembler(squares,LHS,RHS)
    return final_matrix


def simple_image(final_matrix):
    im=plt.imshow(final_matrix,cmap="Greys")
    plt.show()

