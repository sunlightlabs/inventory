#
# views.py
#

from django.shortcuts import redirect, render_to_response

# Create your views here.

def item_redir(request, id):
    return redirect("/admin/QRInventory/item/%s/" % (id))

# add item

# view an item 

# print sheet of qrcodes

#  index
def index(request): 
    return render_to_response('index.html', {'foo':'bar'})
