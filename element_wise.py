import numpy as np
def naive_relu(x):
	print "relu() +++++"
	assert len(x.shape) == 2
	x = x.copy()
	for i in range(x.shape[0]):
		for j in range(x.shape[1]):
			print "x[%s,%s] = %s" % (i,j,x[i,j])
			x[i,j] = max(x[i,j],0)
	print "relu() x : ",x
	print "relu() -----"
	return x
def naive_add(x, y):
	print "add() +++++"
        assert len(x.shape) == 2
        assert len(y.shape) == 2
        x = x.copy()
        for i in range(x.shape[0]):
                for j in range(x.shape[1]):
                        print "x[%s,%s] = %s,y[%s,%s] = %s" % (i,j,x[i,j],i,j,y[i,j])
                        x[i,j] += y[i,j]
        print "add() x : ",x
	print "add() -----"
        return x
def naive_add_matrix_and_vector(x, y ):
        print "add_matrix_and_vector() +++++"
        assert len(x.shape) == 2
        assert len(y.shape) == 1
        x = x.copy()
        for i in range(x.shape[0]):
                for j in range(x.shape[1]):
                        print "x[%s,%s] = %s,y[%s] = %s" % (i,j,x[i,j],j,y[j])
                        x[i,j] += y[j]
        print "add_matrix_and_vector() x : ",x
        print "add_matrix_and_vector() -----"
        return x

import numpy as np
x = np.array([[7,6,5,4,3,2,1,0],
	[-7,-6,-5,-4,-3,-2,-1,0]])
print "x : ",x
y = np.array([[1,1,1,1,1,1,1,0],
        [-1,-1,-1,-1,-1,-1,-1,0]])
print "y : ",y
z = np.array([8,7,6,5,4,3,2,1])
print "z : ",z

naive_relu(x)
print "np.maximum : ",np.maximum(x,0)
naive_add(x,y)
print "x + y : ",(x+y)
naive_add_matrix_and_vector(x,z)
print "x + z : ", (x+z)
