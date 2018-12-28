import redis

r = redis.Redis(host='localhost', port=6379, db=0)
def add_user(username,password):
	Id= r.get('id')
	r.rpush(username,Id)
	r.incr('id')
	r.rpush(username,password)

def add_friend(username,friend):
	r.rpush(username,friend)

def get_user_id(username):
	Id=r.lrange(username,0,0)
	if not Id : 
		return None
	return(Id[0])
def get_user_pass(username):
	password=r.lrange(username,1,1)
	if not password : 
		return None
	return(password[0])

def get_user_friends(username):
	friends=r.lrange(username,2,-1)
	if not friends : 
		return None
	return(friends)



r.flushdb()
r.set('id',0)

if __name__ == "__main__":
	add_user("arash","1234")
	add_user("mohsen","2345")
	add_user("amir","qwerty")

	add_friend('amir','mohsen')
	add_friend('amir','arash')

	print(get_user_id("amir"))	
	print(get_user_pass("amir"))
	print(get_user_friends("amir"))
	print(get_user_id("khaaali"))
	print(get_user_pass("khaaali"))
	print(get_user_friends("khaaali"))

