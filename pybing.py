# -*- coding: utf-8 -*-
#
#  pybing
#  Author: Simone Cingano (simonecingano@gmail.com)
#  Web: http://simonecingano.it
#  Repository: https://github.com/yupswing/pybing
#  Licence: 
#
# The MIT License (MIT)
#
# Copyright (c) 2012-2015 Simone Cingano
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# ---

# You can obtain a key here https://datamarket.azure.com/account/keys
# check your service at https://datamarket.azure.com/dataset/explore/5ba839f1-12ce-4cce-bf57-a49d98d29a44
# and subscribe to use the service here https://datamarket.azure.com/dataset/bing/search
# (5000 queries per months for free)

# Example usage:
#  from pybing import Bing
#  bing = Bing("YOUR KEY HERE",)
#  response = bing.search(query+" wikipedia",top=1)
#  if response: print response[0].get('Url','')
#  else: print "No results"

# Test from shell
#  python pybing.py YOURKEYHERE

import urllib
import urllib2
import json
import sys

def main():
    import sys
    key = None
    if len(sys.argv)>1:
        key = sys.argv[1]
    if not key:
        print ">> PLEASE PROVIDE YOUR KEY AS ARGUMENT <<"
        print "    >> READ THE SOURCE FOR LINKS <<"
        return 0
    bing = Bing(key)
    result = bing.search("python programming language")
    if result:
        print result
    else:
        print "No results"

class Bing:
    key = ''

    def __init__(self,key,top=5,search_type="Web",market="",adult=""):
        # Custom parameters for this instance
        # This could be overrided in every search
        self.key = key
        self.top = top
        self.search_type = search_type
        self.market = market
        self.adult = adult

    def search(self, query, **kwargs):
        """ returns an array [{'Title':'', 'Description':'', 'Url':''},...] """

        #query: string (the query)
        #search_type: string (Web, Image, News, Video)
        #top: int (number of results)
        #market: string (lang code, ie "en-US")
        #adult: string (Strict, Moderate, Off)

        # Retrive the settings for this single query
        key=self.key
        query = urllib.quote(query)
        top = kwargs.get("top",self.top)
        search_type = kwargs.get("search_type",self.search_type)
        market = kwargs.get("market",self.market)
        adult = kwargs.get("adult",self.adult)
        user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)'

        # Prepare the credentials
        credentials = (':%s' % key).encode('base64')[:-1]
        auth = 'Basic %s' % credentials

        # Generate query url
        url = 'https://api.datamarket.azure.com/Data.ashx/Bing/Search/'+search_type
        url+='?Query=%27'+query+'%27'
        if market: url+='&Market=%27'+market+'%27'
        if adult: url+='&Adult=%27'+adult+'%27'
        url+='&$top='+str(top)+'&$format=json'

        # Query BING
        request = urllib2.Request(url)
        request.add_header('Authorization', auth)
        request.add_header('User-Agent', user_agent)
        request_opener = urllib2.build_opener()
        try:
            response = request_opener.open(request)
            response_data = response.read()
            json_result = json.loads(response_data)
            result_list = json_result['d']['results']
        except urllib2.HTTPError as error:
            raise

        # Return the results array
        return result_list

if __name__ == "__main__":
    main()
