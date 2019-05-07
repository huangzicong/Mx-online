# _*_ coding: utf-8 _*_
from django import forms
import re
from operation.models import UserAsk


class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        """
        验证手机号是否合法
        :return:
        """
        mobile = self.changed_data['mobile']
        REGEX_MOBILE = "^1[358]\\d{9}$|^147\\d{8}$|^176\\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u'手机号码格式错误', code="mobile_invalid")
