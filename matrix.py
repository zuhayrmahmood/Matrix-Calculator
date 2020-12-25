class matrix(object):
    def __init__(self, m, n):
        '''The constructor method, m is rows and n is columns (entries in each row)'''
        self.m = m #rows
        self.n = n #entries in the rows
    def __repr__(self):
        return "matrix({}, {})".format(self.m, self.n)

    def __str__(self):
        



