from threading import Thread

def async(func):
	def wrapper(*args,**kwargs):
		t = Thread(target=func,args=args,kwargs=kwargs)
		t.start()
	return wrapper
	 