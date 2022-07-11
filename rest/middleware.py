from django.utils.deprecation import MiddlewareMixin
import json
from rest.models import RequestResponseRestapi
from django.utils import timezone
from configparser import ConfigParser

class LogMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        try:
            response_time = timezone.now()
            time_different = response_time.timestamp() - self.request_time.timestamp()
            RequestResponseRestapi.objects.filter(request_response_id = self.request_response_id).update(response_data = json.dumps(response.data,default = str),response_time = response_time,time_different = time_different)
        except Exception as e:
            pass
        return response
    def process_request(self, request):
        write_config = ConfigParser()
        write_config.add_section("DATABASE")
        # write_config.set("DATABASE","HOST",request.environ['HTTP_HOST'])  
        write_config.set("DATABASE","HOST","akkkk")  
        cfgfile = open("sample.ini",'w')
        write_config.write(cfgfile)
        cfgfile.close()
        # print(request.environ)
        # self.session['HTTP_HOST'] =  request.environ['HTTP_HOST']
        try:

            url = list(request.environ['PATH_INFO'].split("/"))
            app = 'common'
            # for live command the above if elif else condition and set default value for app
            # app = "default"
            
            self.request_time = timezone.now()
            request_details = {
                "request_data" : request.body.decode('utf-8'),
                "app" : app,
                "response_data" : None,
                "request_time" : self.request_time,
                "response_time" : None
            }
            request_data=RequestResponseRestapi(**request_details)
            request_data.save()
            self.request_response_id = request_data.request_response_id
        except Exception as e:
            pass
