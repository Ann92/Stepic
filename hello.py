def app (environ, start_response):
	status = '200 OK'
	headers = [
		('Content-Type', 'text/plain')
	]
	result = ''
	for str in environ['QUERY_STRING'].split('&'):
		result+=str+'\n'
	body = 'Hello, world!'
	start_response(status, headers)
	return [result]
