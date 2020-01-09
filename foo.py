from ctypes import *
lib = cdll.LoadLibrary("libmih.so") # if this fails setup your LD_LIRBARY_PATH

class Foo(object):
        def __init__(self,b,k):
            self.obj = lib.mihasher_new(b,k)
        def test_batch(self, results, numres, numcand, numdups, numlookups, maxrho, ticks, queries, numq, dim1queries):
            lib.mihasher_batchquery(self.obj, results, numres, numcand, numdups, numlookups, maxrho, ticks, queries, numq, dim1queries) 

f = Foo(1,2)
f.test_batch(1,2,3,4,5, 6, 7,"foo",9,10)
