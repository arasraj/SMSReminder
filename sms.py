import urllib2
import urllib
import base64

def main(number, message):
  username = ''
  pwd = ''

  params = { 'To': number, 
             'From':'415-599-2671',
             'Body': message,
           }

  params = urllib.urlencode(params)
  request = urllib2.Request('https://api.twilio.com/2010-04-01/Accounts/%s/SMS/Messages' % username, params)
  request.http_method = 'POST'

  authstring = base64.encodestring('%s:%s' % (username, pwd))
  authstring = authstring.replace('\n', '')

  request.add_header('Authorization', 'Basic %s' % authstring)
  response = urllib2.urlopen(request).read()
  print "response: " , response

if __name__ == '__main__':
  main()
