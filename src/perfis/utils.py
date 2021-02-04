import uuid as u

def get_random_code():
	code = str(u.uuid4())[:8].lower()
	return code