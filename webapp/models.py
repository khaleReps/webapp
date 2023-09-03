from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from django.utils.translation import gettext as _

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True, default='')
    full_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)

    # User Permissions
    access_level = models.CharField(
        max_length=10,
        choices=[
            ('admin', 'Admin'),
            ('user', 'User'),
            ('read-only', 'Read-only')
        ],
        default='user'
    )
    role_based_permissions = models.CharField(max_length=100)

    # Security Settings
    password_management = models.BooleanField(default=True)
    two_factor_authentication = models.BooleanField(default=False)
    security_questions = models.TextField()

    # Notification Preferences
    email_notifications = models.BooleanField(default=True)
    mobile_app_notifications = models.BooleanField(default=True)

    # Time Zone and Language
    time_zone = models.CharField(max_length=50, default='UTC')
    language_preference = models.CharField(max_length=10, default='en')

    def __str__(self):
        return self.full_name

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_format = models.CharField(max_length=10, default='')
    notification_preferences = models.BooleanField(default=True)
    default_account = models.ForeignKey('Account', on_delete=models.SET_NULL, null=True)
    currency = MoneyField(
        max_digits=10,
        decimal_places=2,
        default_currency='ZAR',
        default=Money(0, 'ZAR')
    )
    country = CountryField(default='ZA')
    
    # Preferences
    dashboard_layout = models.CharField(max_length=100)
    currency_format = models.CharField(max_length=10)
    default_ledger_settings = models.CharField(max_length=100)

    # Notification Settings
    email_alerts = models.BooleanField(default=True)
    in_app_notifications = models.BooleanField(default=True)

    # Integration Settings
    third_party_app_integrations = models.CharField(max_length=100)
    api_key_management = models.CharField(max_length=100)

    # Automation and Workflow Preferences
    default_categorization_rules = models.CharField(max_length=100)
    invoice_approval_workflows = models.CharField(max_length=100)
    auto_categorization_settings = models.CharField(max_length=100)

    # Report and Export Preferences
    custom_report_templates = models.CharField(max_length=100)
    export_formats = models.CharField(max_length=100)

    def __str__(self):
        return f"Settings for {self.user.username}"

class BusinessProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=100) 
    business_address = models.TextField() 
    tax_id = models.CharField(max_length=20, default='') 
    currency = models.CharField(max_length=3, default='')
    fiscal_year_start = models.DateField(null=True, default=None) 
    fiscal_year_end = models.DateField(null=True, default=None) 
    currency = MoneyField(
        max_digits=10,
        decimal_places=2,
        default_currency='ZAR',
        default=Money(0, 'ZAR')
    )
    country = CountryField(default='ZA')

    def __str__(self):
        return self.business_name

class Account(models.Model):
    business_profile = models.ForeignKey(BusinessProfile, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=255)
    account_category = models.CharField(max_length=100, default='')

    # Business Information
    business_name = models.CharField(max_length=100)
    business_address = models.TextField()
    tax_identification_number = models.CharField(max_length=20)

    # Financial Settings
    currency_used = models.CharField(max_length=3, default='USD')  # Replace with appropriate choices
    fiscal_year_start = models.DateField(null=True, default=None)
    fiscal_year_end = models.DateField(null=True, default=None)
    tax_settings_and_rates = models.TextField()  # You may want to define a separate model for tax settings and rates

    # Chart of Accounts
    account_customization = models.TextField()
    account_numbering_and_naming = models.TextField()

    # Payment and Billing Settings
    payment_methods_accepted = models.TextField()
    billing_and_invoicing_preferences = models.TextField()

    # User Access Management
    user_access_management = models.TextField()  # Describe the logic for adding/removing users and assigning roles and permissions

    # User-specific settings (e.g., user-specific tax settings)
    user_specific_settings = models.TextField()

    # Backup and Data Retention Settings
    data_backup_frequency = models.CharField(max_length=20, default='Daily')  # Replace with appropriate choices
    data_retention_policies = models.TextField()
    data_archiving_options = models.TextField()

    def __str__(self):
        return self.account_name
