import time

class DemoMiddleware:
     def __init__(self, get_response):
        self.get_response = get_response
     
     def __call__(self, request):
        start_time = time.time()
     
        response = self.get_response(request)
     
        duration = time.time() - start_time
        print(f"The request '{request.path}' took {duration:.3f} seconds to complete")
     
     
        return response


     
    #  def process_view(self,request, view_func
    #                   , view_args, view_kwargs):
    #      print(f'the request: {view_args}')
    #      pass
     
    #  def process_request(self, request):
    #     request.start_time = time.time()

    #  def process_response(self, request, response):
    #     # Calculate the time taken for the request
    #     duration = time.time() - request.start_time
    #     # Print the message
    #     print(f"The request '{request.path}' took {duration:.3f} seconds to complete")
       