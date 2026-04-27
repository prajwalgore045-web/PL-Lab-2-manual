class MyError(Exception):pass
try:raise MyError
except MyError:print('custom')