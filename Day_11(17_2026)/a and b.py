# # Approach ->>>01(direct approach)
#
# import a
# import b
#
# obj1=a.animal() #here i created object for "a" class as "obj1".
# #by using module name.class name we can invoke classes (a.animal)
# obj1.display()#i like cow
#
# obj2=b.bird()##here i created object for "b" class as "obj2".
# #by using module name.class name we can invoke classes (b.animal)
# obj2.display()#i like parrot

# Approach->>>02 (module name and class name)
from a import animal
from b import bird

obj1=animal()
obj1.display()#i like cow

obj2=bird()
obj2.display()#i like parrot