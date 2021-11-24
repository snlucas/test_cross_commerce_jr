from rest_framework.views import APIView
from rest_framework.response import Response
import requests


class ListData(APIView):
    def __init__(self):
        super().__init__()
        self.url = "http://challenge.dienekes.com.br/api/numbers?page="
    

    def get(self, request, format=None):
        '''
        Return a list with the whole data.
        '''
        # Received data
        data = self.extract_api_data().values()
        # Extract values to a list
        data = list(data)
        # Merge lists into one
        data = sum(data, [])

        # Generate Response
        response = {}
        response['data'] = data

        return Response(response)


    def extract_api_data(self) -> dict:
        '''
        Return a dict of each page data
        '''
        page_data = {}
        i = 1

        # If KeyError exception -> means we're on the last page.
        # So, return the whole data.
        try:
            while True:
                # Request remaing pages data
                url = f'{self.url}{i}'
                r = requests.get(url).json()

                # Feeds hash with data from each page
                page_data[f'page{i}'] = r['numbers']

                i += 1  # Next Page
        except KeyError:
            return page_data
