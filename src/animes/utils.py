import uuid

def get_random_code():
	code = str(uuid.uuid4())[:4].lower()
	return code