from cgi import parse_qs

def application (env, start_response):
	qs = parse_qs (env['QUERY_STRING'])
	res = ''
	for k,v in qs.iteritems():
		res += str(k) + '=' + str(v) + '\n'
	start_response ('200 OK', [('Content-Type', 'text/plain'),('Content-Length',str(len(res)))])
	return [res]
