from django.contrib.admin import AdminSite

from .models.user import User
from .models.demmand import Demmand
from .models.address import Address


from .custom_admin.user import CustomUserAdmin
from .custom_admin.demmand import DemmandCustomAdmin
from .custom_admin.address import AddressCustomAdmin
# Register your models here.

class CustomAdmin(AdminSite):    
    site_header = "Droidpieces"
    site_header = "The place to Exchange Droid Pieces"
    site_title="DroidPieces"
    index_title="Admnistrativo"

admin_site = CustomAdmin(name='custom_admin')
admin_site.register(User, CustomUserAdmin)
admin_site.register(Demmand, DemmandCustomAdmin)
admin_site.register(Address,AddressCustomAdmin)

