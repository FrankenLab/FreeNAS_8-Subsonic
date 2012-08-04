import os
import platform
import pwd

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from subsonicUI.freenas import models, utils


class SubsonicForm(forms.ModelForm):

    class Meta:
        model = models.Subsonic
        #widgets = {
        #    'admin_pw': forms.widgets.PasswordInput(),
        #}
        exclude = (
            'enable',
            )

    def __init__(self, *args, **kwargs):
        self.jail = kwargs.pop('jail')
        super(SubsonicForm, self).__init__(*args, **kwargs)

        #if self.instance.admin_pw:
        #    self.fields['admin_pw'].required = False

    def save(self, *args, **kwargs):
        obj = super(SubsonicForm, self).save(*args, **kwargs)

        rcconf = os.path.join(utils.subsonic_etc_path, "rc.conf")
        with open(rcconf, "w") as f:
            if obj.enable:
                f.write('subsonic_enable="YES"\n')

            #subsonic_flags = ""
            #for value in advanced_settings.values():
            #    subsonic_flags += value + " "
            #f.write('subsonic_flags="%s"\n' % (subsonic_flags, ))

        os.system(os.path.join(utils.subsonic_pbi_path, "tweak-rcconf"))
