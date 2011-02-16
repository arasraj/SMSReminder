import tornado.httpserver
import tornado.ioloop
import tornado.web
import heapq
import datetime
from message import Message
from sms import main

heap = []

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    self.write('<html> \
                <body><form method="post" action="http://192.168.1.5:8888/schedule"><table> \
		<tr><td>Number:<input type="text" name="number"></td></tr> \
		<tr><td>Message:<input type="text" name="message"></td></tr> \
		<tr><td>Date:<input type="text" name="time"></td></tr> \
		<tr><td><input type="submit" value="Submit"></td></tr> \
	        </table> \
	        </form> \
                </body> \
                </html>')

class Heap(tornado.web.RequestHandler):

  def post(self):
    time_schedule = self.get_argument("time")
    tokens = time_schedule.split()   
    date = tokens[0].split('-')
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])

    time_token = tokens[1]
    #user_time = int(time_token[:-2]) 
    user_time = time_token[:-2].split(':')
    hours = int(user_time[0])
    minutes = 0
    if len(user_time) > 1:
      minutes = int(user_time[1])
    am_pm = time_token[-2:]
    if am_pm == 'pm':
      hours += 12
    
    message = self.get_argument("message")
    number = self.get_argument("number")
    dt = datetime.datetime(year, month, day, hours, minutes)
    obj = Message(message, number, dt)
    heapq.heappush(heap, obj)
    for item in heap:
      print item.message, item.number, item.time

class SendSMS(tornado.web.RequestHandler):
  def get(self):
      while (heap and heap[0].time <= datetime.datetime.now()):
        min_item = heapq.heappop(heap)
        main(min_item.number, min_item.message)    
  
application = tornado.web.Application([(r"/", MainHandler), (r'/schedule', Heap), (r'/send', SendSMS),])


if __name__ == '__main__':
  http_server = tornado.httpserver.HTTPServer(application)
  http_server.listen(8888)
  tornado.ioloop.IOLoop.instance().start()
