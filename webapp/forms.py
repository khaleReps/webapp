from django import forms
from .models import UserProfile, BusinessProfile, UserSettings

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'first_name',
            'last_name',
            'profile_image',
            'email',
            'contact_number',
            'access_level',
            'role_based_permissions',
            'password_management',
            'two_factor_authentication',
            'security_questions',
            'email_notifications',
            'mobile_app_notifications',
            'time_zone',
            'language_preference',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control'}), 
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'access_level': forms.Select(attrs={'class': 'form-control'}),
            'role_based_permissions': forms.TextInput(attrs={'class': 'form-control'}),
            'password_management': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'two_factor_authentication': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'security_questions': forms.Textarea(attrs={'class': 'form-control'}),
            'email_notifications': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'mobile_app_notifications': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'time_zone': forms.TextInput(attrs={'class': 'form-control'}),
            'language_preference': forms.TextInput(attrs={'class': 'form-control'}),
        }

class BusinessProfileForm(forms.ModelForm):
    class Meta:
        model = BusinessProfile
        fields = [
            'business_name',
            'logo',
            'business_address',
            'currency_used',
            'tax_settings_and_rates',
            'tax_id',
            'currency',
            'fiscal_year_start',
            'fiscal_year_end',
            'country',
        ]
        widgets = {
            'business_name': forms.TextInput(attrs={'class': 'form-control'}),
            'logo': forms.FileInput(attrs={'class': 'form-control'}), 
            'business_address': forms.Textarea(attrs={'class': 'form-control'}),
            'currency_used': forms.TextInput(attrs={'class': 'form-control'}),
            'tax_settings_and_rates': forms.Textarea(attrs={'class': 'form-control'}),
            'tax_id': forms.TextInput(attrs={'class': 'form-control'}),
            'currency': forms.TextInput(attrs={'class': 'form-control'}),
            'fiscal_year_start': forms.DateInput(attrs={'class': 'form-control'}),
            'fiscal_year_end': forms.DateInput(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
        }


class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserSettings
        fields = [
            'dark_mode', 
            'date_format',
            'notification_preferences',
            'default_account',
            'currency',
            'country',
            'dashboard_layout',
            'currency_format',
            'default_ledger_settings',
            'email_alerts',
            'in_app_notifications',
            'third_party_app_integrations',
            'api_key_management',
            'default_categorization_rules',
            'invoice_approval_workflows',
            'auto_categorization_settings',
            'custom_report_templates',
            'export_formats',
           
        ]
        widgets = {
            'dark_mode': forms.CheckboxInput(attrs={'class': 'form-check-input'}), 
            'date_format': forms.TextInput(attrs={'class': 'form-control'}),
            'notification_preferences': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'default_account': forms.Select(attrs={'class': 'form-control'}),
            'currency': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'dashboard_layout': forms.TextInput(attrs={'class': 'form-control'}),
            'currency_format': forms.TextInput(attrs={'class': 'form-control'}),
            'default_ledger_settings': forms.TextInput(attrs={'class': 'form-control'}),
            'email_alerts': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'in_app_notifications': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'third_party_app_integrations': forms.TextInput(attrs={'class': 'form-control'}),
            'api_key_management': forms.TextInput(attrs={'class': 'form-control'}),
            'default_categorization_rules': forms.TextInput(attrs={'class': 'form-control'}),
            'invoice_approval_workflows': forms.TextInput(attrs={'class': 'form-control'}),
            'auto_categorization_settings': forms.TextInput(attrs={'class': 'form-control'}),
            'custom_report_templates': forms.TextInput(attrs={'class': 'form-control'}),
            'export_formats': forms.TextInput(attrs={'class': 'form-control'}),

        }
