from imptee import foo, show
import imptee

show()
imptee.foo = 123
print 'foo from impter:', foo
print 'foo from imptee:', imptee.foo
imptee.show()
show()
foo = '000'
imptee.show()
show()
print 'foo from imptee:', imptee.foo
print 'foo from impter:', foo
