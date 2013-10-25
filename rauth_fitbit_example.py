#!/usr/bin/python
import rauth

from _credentials import consumer_key, consumer_secret

base_url = "https://api.fitbit.com"
request_token_url = base_url + "/oauth/request_token"
access_token_url = base_url + "/oauth/access_token"
authorize_url = "http://www.fitbit.com/oauth/authorize"

fitbit = rauth.OAuth1Service(
    name="fitbit",
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    request_token_url=request_token_url,
    access_token_url=access_token_url,
    authorize_url=authorize_url,
    base_url=base_url)

request_token, request_token_secret = fitbit.get_request_token()

print " request_token        = %s" % request_token
print " request_token_secret = %s" % request_token_secret
print 

authorize_url = fitbit.get_authorize_url(request_token)

print "Go to the following page in your browser: " + authorize_url
print 

accepted = 'n'
while accepted.lower() == 'n':
    accepted = raw_input('Have you authorized me? (y/n) ')
pin = raw_input('Enter PIN from browser ')

session = fitbit.get_auth_session(request_token,
                                    request_token_secret,
                                    method="POST",
                                    data={'oauth_verifier': pin})

print ""
print " access_token        = %s" % session.access_token
print " access_token_secret = %s" % session.access_token_secret
print ""

url = base_url + "/1/" + "user/-/profile.json"

r = session.get(url, params={}, header_auth=True)
print r.json()