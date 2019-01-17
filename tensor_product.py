import numpy as np
def naive_vector_dot(x,y):
        print "vector_dot() +++++"
        assert len(x.shape) == 1
        assert len(y.shape) == 1
        x = x.copy()
	z = 0
        for i in range(x.shape[0]):
                print "x[%s] = %s,y[%s] = %s, x[%s] * y[%s] = %s" % (i,x[i],i,y[i],i,i,x[i]*y[i])
                z += x[i] * y[i]
        print "vector_dot() z : ",z
        print "vector_dot() -----"
        return z
def naive_matrix_vector_dot(x,y):
        print "matrix_vector_dot() +++++"
        assert len(x.shape) == 2
        assert len(y.shape) == 1
        x = x.copy()
        z = np.zeros(x.shape[0])
        for i in range(x.shape[0]):
		for j in range(x.shape[1]):
	                print "x[%s,%s] = %s,y[%s] = %s, x[%s,%s] * y[%s] = %s" % (i,j,x[i,j],j,y[j],i,j,j,x[i,j]*y[j])
        	        z[i] += x[i,j] * y[j]
        print "matrix_vector_dot() z : ",z
	type(z)
	print "type : ",type(z)
        print "matrix_vector_dot() -----"
        return z
def naive_matrix_vector_dot2(x,y):
        print "matrix_vector_dot2() +++++"
        assert len(x.shape) == 2
        assert len(y.shape) == 1
        x = x.copy()
        z = np.zeros(x.shape[0])
	print "type z : ",type(z)
	print "type z[0] : ",type(z[0])
        for i in range(x.shape[0]):
                for j in range(x.shape[1]):
                        print "x[%s,%s] = %s,y[%s] = %s, x[%s,%s] * y[%s] = %s" % (i,j,x[i,j],j,y[j],i,j,j,x[i,j]*y[j])
                        #z[i] += x[i,j] * y[j]
		z[i] = naive_vector_dot(x[i],y)
        print "matrix_vector_dot2() z : ",z
        type(z)
        print "type : ",type(z)
        print "matrix_vector_dot2() -----"
        return z
def naive_matrix_matrix_dot(x,y):
        print "matrix_matrix_dot() +++++"
	print "(%s,%s) * (%s,%s) = (%s * %s)" %(x.shape[0],x.shape[1],y.shape[0],y.shape[1],x.shape[0],y.shape[1])
        assert x.shape[1] == y.shape[0]
        x = x.copy()
        z = np.zeros((x.shape[0],y.shape[1]))
        print "type z : ",type(z)
        print "type z[0] : ",type(z[0])
        for i in range(x.shape[0]):
                for j in range(y.shape[1]):
			for k in range(x.shape[1]):
	                        print "x[%s,%s] = %s,y[%s,%s] = %s, x[%s,%s] * y[%s,%s] = %s" % (i,k,x[i,k],k,j,y[k,j],i,k,k,j,x[i,k]*y[k,j])
        	                z[i,j] += x[i,k] * y[k,j]
#	                z[i,j] = naive_vector_dot(x[i],y)
        print "matrix_matrix_dot() z : ",z
        type(z)
        print "type : ",type(z)
        print "matrix_matrix_dot() -----"
        return z
def naive_matrix_matrix_dot2(x,y):
        print "matrix_matrix_dot2() +++++"
        print "(%s,%s) * (%s,%s) = (%s * %s)" %(x.shape[0],x.shape[1],y.shape[0],y.shape[1],x.shape[0],y.shape[1])
        assert x.shape[1] == y.shape[0]
        x = x.copy()
        z = np.zeros((x.shape[0],y.shape[1]))
        print "type z : ",type(z)
        print "type z[0] : ",type(z[0])
        for i in range(x.shape[0]):
                for j in range(y.shape[1]):
                        for k in range(x.shape[1]):
                                print "x[%s,%s] = %s,y[%s,%s] = %s, x[%s,%s] * y[%s,%s] = %s" % (i,k,x[i,k],k,j,y[k,j],i,k,k,j,x[i,k]*y[k,j])
                        z[i,j] = naive_vector_dot(x[i,:],y[:,j])
        print "matrix_matrix_dot2() z : ",z
        type(z)
        print "type : ",type(z)
        print "matrix_matrix_dot2() -----"
        return z
def naive_matrix_matrix_dot3(x,y):
        print "matrix_matrix_dot3() +++++"
        print "(%s,%s) * (%s,%s) = (%s * %s)" %(x.shape[0],x.shape[1],y.shape[0],y.shape[1],x.shape[0],y.shape[1])
        assert x.shape[1] == y.shape[0]
        x = x.copy()
        z = np.zeros((x.shape[0],y.shape[1]))
        print "type z : ",type(z)
        print "type z[0] : ",type(z[0])
        for i in range(x.shape[0]):
                for j in range(y.shape[1]):
                        for k in range(x.shape[1]):
                                print "x[%s,%s] = %s,y[%s,%s] = %s, x[%s,%s] * y[%s,%s] = %s" % (i,k,x[i,k],k,j,y[k,j],i,k,k,j,x[i,k]*y[k,j])
	for j in range(y.shape[1]):
                 z[:,j] = naive_matrix_vector_dot(x,y[:,j])
        print "matrix_matrix_dot3() z : ",z
        type(z)
        print "type : ",type(z)
        print "matrix_matrix_dot3() -----"
        return z

x = np.array([7,6,5,4,3,2,1,0])
print "x : ",x
y = np.array([8,7,6,5,4,3,2,1])
print "y : ",y
#invalid
#z=(x).(y)
#print "x.y = ", (x.y)
naive_vector_dot(x,y)
print "np.dot(x,y) = ",np.dot(x,y)

z=np.array([[7,6,5,4,3,2,1,0],
[1,1,1,1,1,1,1,1]])
naive_matrix_vector_dot(z,y)
naive_matrix_vector_dot2(z,y)
print "np.dot(z,y) = ",np.dot(z,y)
type(np.dot(z,y))
print "type : ",type(np.dot(z,y))

matrix1 = np.array([[1,2,3],[2,3,4]])
matrix2 = np.array([[1,2,3,4],[2,3,4,5],[3,4,5,6]])
naive_matrix_matrix_dot(matrix1,matrix2)
naive_matrix_matrix_dot2(matrix1,matrix2)
naive_matrix_matrix_dot3(matrix1,matrix2)
print "np.dot(matrix1,matrix2) : ",np.dot(matrix1,matrix2)
