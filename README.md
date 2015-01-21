
# pybing

This python library provide support to query the Bing Search Engine<br/>
Originally forked from: https://code.google.com/p/pybing/<br/>
LICENCE: GNU GPL v2 http://www.gnu.org/licenses/old-licenses/gpl-2.0.html

---

To use the webservice you need an API Key from Microsoft.<br/>
When you login (or register) with a Microsoft account, you can obtain a key (to be used with the library) from<br/>
https://datamarket.azure.com/account/keys

To use the service you need to subscribe to it from<br/>
https://datamarket.azure.com/dataset/bing/search<br/>
The free subscription offers 5000 queries per months.<br/>
If you need more you can pay and subscribe a different offer.<br/>

Last, you can check your subscription status (basically the queries left this month) at<br/>
https://datamarket.azure.com/dataset/explore/5ba839f1-12ce-4cce-bf57-a49d98d29a44

---

# Example usage:
After downloading the library or adding it as a submodule in your project
```python
from pybing import Bing
bing = Bing("YOUR KEY HERE",)
query="python programming language"
response = bing.search(query,top=5,search_type='Web',market='en-US',adult='off')
if response:
    for result in response:
        print "TITLE: %s\nDESCRIPTION: %s\nURL: %s\n\n" % (result.get('Title','no title'),
                                                           result.get('Description','no description'),
                                                           result.get('Url','no url'))
else:
   print "No results"
```

or you can test it directly from shell
```bash
python pybing.py YOURKEYHERE
```
