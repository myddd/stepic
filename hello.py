from cgi import parse_qs

def application (env, start_response):
	resp = env['QUERY_STRING'].split("&")
  	resp = [item+"\r\n" for item in resp]
  	start_response ('200 OK', [('Content-Type', 'text/plain')])
  	return resp
	
