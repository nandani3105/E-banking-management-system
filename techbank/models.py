
from django.db import models
import uuid

# Create your models here.


class user_acount_request(models.Model):
    ACCOUNT_TYPES = [
        ('Savings', 'Savings'),
        ('Current', 'Current'),
    ]

    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    nation = models.CharField(max_length=100)
    address = models.TextField()
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    aadhar = models.CharField(max_length=12)
    pan = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='photos/')
    kyc_photo = models.ImageField(upload_to='kyc_photos/', blank=True, null=True)
    choose = models.CharField(max_length=10, choices=ACCOUNT_TYPES)

    def __str__(self):
        return self.fullname


class userAcount(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Used for login
    password = models.CharField(max_length=100)  # Store hashed password in production!
    phone = models.CharField(max_length=15)
    nation = models.CharField(max_length=50)
    address = models.TextField()
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    aadhar = models.CharField(max_length=12, unique=True)
    pan = models.CharField(max_length=10, unique=True)
    photo = models.ImageField(upload_to='profile_photos/')
    choose = models.CharField(max_length=30, choices=[('savings', 'Savings'), ('current', 'Current')])
    kyc_photo = models.ImageField(upload_to='kyc_photos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname




# model for vehicles insurence
class VehicleInsurance(models.Model):
    VEHICLE_TYPES = [
        ('Car', 'Car'),
        ('Two-Wheeler', 'Two-Wheeler'),
        ('Commercial Vehicle', 'Commercial Vehicle'),
    ]

    FUEL_TYPES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('CNG', 'CNG'),
    ]

    INSURANCE_TYPES = [
        ('Third-Party', 'Third-Party'),
        ('Comprehensive', 'Comprehensive'),
        ('Own Damage', 'Own Damage'),
    ]

    vehicle_type = models.CharField(max_length=30, choices=VEHICLE_TYPES)
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    registration = models.CharField(max_length=20)
    registration_year = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=20, choices=FUEL_TYPES)
    owner_name = models.CharField(max_length=100)
    aadhar = models.CharField(max_length=12)
    aadhar_photo = models.ImageField(upload_to='aadhar_photos/')
    pan = models.CharField(max_length=10)
    pan_photo = models.ImageField(upload_to='pan_photos/')
    vehicle_photo = models.ImageField(upload_to='vehicle_photos/')
    insurance_type = models.CharField(max_length=30, choices=INSURANCE_TYPES)
    duration = models.PositiveIntegerField()

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owner_name} - {self.registration}"


# model for card apply
EMPLOYMENT_CHOICES = [
    ('employed', 'Employed'),
    ('self-employed', 'Self-employed'),
    ('student', 'Student'),
    ('unemployed', 'Unemployed'),
    ('retired', 'Retired'),
]

CARD_TYPE_CHOICES = [
    ('credit', 'Credit Card'),
    ('debit', 'Debit Card'),
]

class CardApplication(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.TextField()
    employment_status = models.CharField(max_length=20, choices=EMPLOYMENT_CHOICES)
    annual_income = models.PositiveIntegerField()
    card_type = models.CharField(max_length=10, choices=CARD_TYPE_CHOICES)
    id_proof = models.FileField(upload_to='id_proofs/')
    address_proof = models.FileField(upload_to='address_proofs/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.card_type.title()} Application"


# model for health insurence

class HealthInsuranceApplication(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    ]

    ID_TYPE_CHOICES = [
        ('Aadhar', 'Aadhar'),
        ('PAN', 'PAN'),
        ('Passport', 'Passport'),
        ('Driving License', 'Driving License'),
    ]

    PLAN_CHOICES = [
        ('Individual Plan', 'Individual Plan'),
        ('Family Plan', 'Family Plan'),
        ('Senior Citizen Plan', 'Senior Citizen Plan'),
    ]

    fullname = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField()
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES)
    nationality = models.CharField(max_length=50)

    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

    id_type = models.CharField(max_length=20, choices=ID_TYPE_CHOICES)
    id_number = models.CharField(max_length=30)

    nominee_name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=50)
    nominee_contact = models.CharField(max_length=15)

    plan = models.CharField(max_length=25, choices=PLAN_CHOICES)

    declaration = models.BooleanField()

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fullname} - {self.plan}"


# model for life insurence

class LifeInsuranceApplication(models.Model):
    # Personal Details
    fullname = models.CharField(max_length=100, default='Unknown')
    dob = models.DateField(default='dd/mm/yyyy')
    gender = models.CharField(max_length=10, default='Not specified')
    marital_status = models.CharField(max_length=20, default='Single')

    # Contact Information
    email = models.EmailField(default='noemail@example.com')
    phone = models.CharField(max_length=15, default='0000000000')
    address = models.TextField(default='Not provided')

    # Identification
    id_type = models.CharField(max_length=50, default='Aadhar Card')
    id_number = models.CharField(max_length=50, default='0000-0000-0000')

    # Nominee Information
    nominee_name = models.CharField(max_length=100, default='Unknown')
    relationship = models.CharField(max_length=50, default='Not specified')
    nominee_contact = models.CharField(max_length=15, default='0000000000')

    # Plan & Declaration
    plan = models.CharField(max_length=50, default='Term Plan')
    declaration = models.BooleanField(default=False)

    # Timestamp
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fullname} - {self.plan}"

class trans(models.Model):
    fullname = models.CharField(max_length=100, default='Unknown')
    email = models.EmailField(default='unknown@example.com')
    IFSC = models.CharField(max_length=20, default='UNKNOWN0000')
    account_number = models.CharField(max_length=30, default='0000000000')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.full_name} - ₹{self.amount} on {self.date.strftime('%Y-%m-%d')}"
    


# model for support

class SupportRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    issue = models.TextField()
    submitted_on = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.email[:15]} - {'Resolved' if self.is_resolved else 'Pending'}"
    
# model for loan
class LoanApplication(models.Model):
    LOAN_TYPES = [
        ('Home Loan', 'Home Loan'),
        ('Education Loan', 'Education Loan'),
        ('Personal Loan', 'Personal Loan'),
    ]

    loan_type = models.CharField(max_length=20, choices=LOAN_TYPES)
    amount = models.PositiveIntegerField()
    duration = models.PositiveIntegerField(help_text="In years")
    account_no = models.CharField(max_length=20)
    aadhar = models.CharField(max_length=12)
    pan = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='loan_photos/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.loan_type} - {self.account_no}"
