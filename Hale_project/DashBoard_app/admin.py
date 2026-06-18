from django.contrib import admin

# Register your models here.
from .models import *



from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User



admin.site.register(Feeback)
admin.site.register(ADDSECTION)
admin.site.register(PatientTable)
admin.site.register(APPOINTMENTSAVED)
admin.site.register(MedicineList)
admin.site.register(Department)
admin.site.register(Staffs)
admin.site.register(profit)


def last_login_logout(self, obj):
        if obj.last_login:
            return f'{obj.last_login.strftime("%Y-%m-%d %H:%M:%S")} - {obj.logout_time.strftime("%Y-%m-%d %H:%M:%S")}' if obj.logout_time else _('Logged in')
        return _('Never logged in')
