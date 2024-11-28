from src.drivers.google.request import Request

rq = Request.fromConfig()

rq.build('', None)

data = rq.make()



print(data['items'][0]['volumeInfo']['title'])
