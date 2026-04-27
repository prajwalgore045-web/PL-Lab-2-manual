class A:
 def a(self):print('A')
class B:
 def b(self):print('B')
class E(A,B):pass
e=E();e.a();e.b()