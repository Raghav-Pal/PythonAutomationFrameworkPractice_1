import inspect
# functions
def whoami():
    return inspect.stack()[1][3]
def whosdaddy():
    return inspect.stack()[2][3]
def foo():
    print("hello, I'm %s, daddy is %s" % (whoami(), whosdaddy()))
    bar()
def bar():
    print("hello, I'm %s, daddy is %s" % (whoami(), whosdaddy()))
def testOne():
   x = whoami()
   print(x)

johny = bar
# call them!
foo()
bar()
johny()
testOne()