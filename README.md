
# pybing

This library provide support to query the Bing Search Engine

---

To use the webservice you need an API Key from Microsoft.
When you login (or register) with a Microsoft account, you can obtain a key (to be used with the library) from https://datamarket.azure.com/account/keys

To use the service you need to subscribe to it from https://datamarket.azure.com/dataset/bing/search
The free subscription offers 5000 queries per months.
If you need more you can pay and subscribe a different offer.

Last, you can check your subscription status (basically the queries left this month) at https://datamarket.azure.com/dataset/explore/5ba839f1-12ce-4cce-bf57-a49d98d29a44

---

# Example usage:
After downloading the library or adding it as a submodule in your project
```python
from pybing import Bing
bing = Bing("YOUR KEY HERE",)
response = bing.search(query+" wikipedia",top=1)
if response:
   first = response[0]
   print "%s (%s)\n%s" % (first.get('Title','no title'),first.get('Description','no description'),first.get('Url','no url'))
else:
   print "No results"
```

or you can test it directly from shell
```bash
python pybing.py YOURKEYHERE
```
