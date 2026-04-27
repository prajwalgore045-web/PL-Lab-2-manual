class A:
 def a(self):print('A')
class B(A):pass
class C(B):pass
C().a()