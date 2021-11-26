from rest_framework.views import APIView
from rest_framework.response import Response
import aiohttp
import asyncio

from test_cross_commerce.utils.quick_sort import quick_sort


class ListData(APIView):
    def __init__(self):
        super().__init__()
        self.url = "http://challenge.dienekes.com.br/api/numbers?page="

    def get(self, request, format=None):
        """
        Return a list with the whole data.
        """
        # Received data
        data = asyncio.run(self.extract_api_data()).values()
        # Extract values to a list
        data = list(data)
        # Merge lists into one
        data = sum(data, [])
        # Sort data
        quick_sort(data)

        # Generate Response
        response = {}
        response["data"] = data

        return Response(response)


    async def extract_api_data(self) -> dict:
        """
        Return a dict of each page data
        """
        page_data = {}
        i = 1
        async with aiohttp.ClientSession() as session:
            # If KeyError exception -> means we're on the last page.
            # So, return the whole data.
            try:
                while True:
                    # Request remaining pages data
                    url = f"{self.url}{i}"
                    async with session.get(url) as resp:
                        # Feeds hash with data from each page
                        data = await resp.json()
                        page_data[f"page{i}"] = data['numbers']
                    i += 1  # Next Page
            except KeyError:
                return page_data
