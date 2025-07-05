from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.views.decorators.cache import cache_page
from django.http import HttpResponse
from techbank.models import userAcount
from .utils import handle_kyc_photo
from .models import user_acount_request, userAcount, VehicleInsurance, HealthInsuranceApplication, LifeInsuranceApplication, trans, CardApplication, LoanApplication, SupportRequest
from django.contrib.auth import views as auth_views


def user_app(request):
    return render(request,'user_app.html')

def account_requests(request):
    return render(request,'account_requests.html')

def currency_exchange(request):
    return render(request,'currency_exchange.html')

def loan(request):
    return render(request,'loan.html')

def support(request):
    return render(request,'support.html')

def health(request):
    return render(request,'health.html')

def life(request):
    return render(request,'life.html')




def success(request, id):
    account = get_object_or_404(user_acount_request, id=id)  # use the id for logic if needed
    return render(request, 'success.html', {'account': account})

def create_acc_request(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        nation = request.POST.get('nation')
        address = request.POST.get('address')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        aadhar = request.POST.get('aadhar')
        pan = request.POST.get('pan')
        choose = request.POST.get('choose')
        photo = request.FILES.get('photo')
        kyc_photo_data = request.POST.get('kyc_photo')
        kyc_image_file = handle_kyc_photo(kyc_photo_data)

        account = user_acount_request(
            fullname=fullname,
            email=email,
            password=password,
            phone=phone,
            nation=nation,
            address=address,
            state=state,
            pincode=pincode,
            aadhar=aadhar,
            pan=pan,
            photo=photo,
            choose=choose
        )

        if kyc_image_file:
            account.kyc_photo = kyc_image_file
        
        account.save()

        
        return redirect(f'/success/{account.id}/')  # or a success page
    return render(request, 'create_acc_request.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import user_acount_request

def netbanking(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        try:
            user = user_acount_request.objects.get(phone=phone, password=password)
            # Login successful
            request.session['user_id'] = user.id  # Optional: store session
            return redirect('user_acount')  # Replace 'dashboard' with your next page URL name
        except user_acount_request.DoesNotExist:
            messages.error(request, 'Invalid phone number or password.')

    return render(request, 'netbanking.html')


def user_acount(request):
    return render(request,'user_acount.html')


def user_account_request_list(request):
    account = user_acount_request.objects.all()
    return render(request, 'user_account_request_list.html', {'account': account})




def get_user(request):
    email = request.GET.get('email')
    account = []
    if email:
        account = user_acount_request.objects.filter(email=email)
    return render(request, 'user_account_request_list.html', {'account': account})


def vehicle_insuranceform(request):
    if request.method == 'POST':
        vehicle_type = request.POST.get('vehicleType')
        manufacturer = request.POST.get('manufacturer')
        model = request.POST.get('model')
        registration = request.POST.get('registration')
        registration_year = request.POST.get('registrationYear')
        fuel_type = request.POST.get('fuelType')
        owner_name = request.POST.get('ownerName')
        aadhar = request.POST.get('aadhar')
        pan = request.POST.get('pan')
        insurance_type = request.POST.get('insuranceType')
        duration = request.POST.get('duration')
        aadhar_photo = request.FILES.get('aadharPhoto')
        pan_photo = request.FILES.get('panPhoto')
        vehicle_photo = request.FILES.get('vehiclePhoto')

        # Save to DB
        v_insurances = VehicleInsurance(
            vehicle_type=vehicle_type,
            manufacturer=manufacturer,
            model=model,
            registration=registration,
            registration_year=registration_year,
            fuel_type=fuel_type,
            owner_name=owner_name,
            aadhar=aadhar,
            aadhar_photo=aadhar_photo,
            pan=pan,
            pan_photo=pan_photo,
            vehicle_photo=vehicle_photo,
            insurance_type=insurance_type,
            duration=duration
        )
        v_insurances.save()

        return redirect('success')  # Redirect to the list page or a success page

    return render(request, 'vehicle_insuranceform.html')  # Template you just shared

def vehicle_insurance_list(request):
    v_insurances = VehicleInsurance.objects.all()
    return render(request, 'vehicle_insurance_list.html', {'v_insurances': v_insurances})




def health_insurance_form(request):
    if request.method == 'POST':
       # Get data from POST request
        fullname = request.POST.get('fullname')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        marital_status = request.POST.get('marital_status')
        nationality = request.POST.get('nationality')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')

        id_type = request.POST.get('id_type')
        id_number = request.POST.get('id_number')
        nominee_name = request.POST.get('nominee_name')
        relationship = request.POST.get('relationship')
        nominee_contact = request.POST.get('nominee_contact')
        plan = request.POST.get('plan')
        declaration = request.POST.get('declaration') == 'on'  # checkbox

        # Save to database
        health_applications = HealthInsuranceApplication(
            fullname=fullname,
            gender=gender,
            dob=dob,
            marital_status=marital_status,
            nationality=nationality,
            phone=phone,
            email=email,
            address=address,
            id_type=id_type,
            id_number=id_number,
            nominee_name=nominee_name,
            relationship=relationship,
            nominee_contact=nominee_contact,
            plan=plan,
            declaration=declaration
        )
        health_applications.save()

        return redirect('success')  # Redirect to a "success" page

    return render(request, 'health_insurance_form.html')


def health_insurance_list(request):
    health_applications = HealthInsuranceApplication.objects.all()
    return render(request, 'health_insurance_list.html', {'health_applications': health_applications})




def life_insurance_form(request):
    if request.method == 'POST':
        
        # Fetch and clean POST data
        fullname = request.POST.get('fullname')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        marital_status = request.POST.get('marital_status')

        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        id_type = request.POST.get('id_type')
        id_number = request.POST.get('id_number')

        nominee_name = request.POST.get('nominee_name')
        relationship = request.POST.get('relationship')
        nominee_contact = request.POST.get('nominee_contact')

        plan = request.POST.get('plan')
        declaration = request.POST.get('declaration') == 'on'

        # Save the form to the database
        life_insurance = LifeInsuranceApplication(
            fullname=fullname,
            dob=dob,
            gender=gender,
            marital_status=marital_status,
            email=email,
            phone=phone,
            address=address,
            id_type=id_type,
            id_number=id_number,
            nominee_name=nominee_name,
            relationship=relationship,
            nominee_contact=nominee_contact,
            plan=plan,
            declaration=declaration
        )
        life_insurance.save()

        return redirect('success')  # Ensure 'success' URL/view exists
        
    # GET request: render blank form
    return render(request, 'life_insurance_form.html')

def life_insurance_list(request):
    life_insurance = LifeInsuranceApplication.objects.all()
    return render(request, 'life_insurance_list.html', {'life_insurance': life_insurance})


def user_profile(request):
    return render(request,'user_profile.html')




def transaction(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        IFSC = request.POST.get('IFSC')
        account_number = request.POST.get('account_number')
        amount = request.POST.get('amount')

        trans_page = trans(
            full_name=full_name,
            email=email,
            IFSC=IFSC,
            account_number=account_number,
            amount=amount
        )
        trans_page.save()
        return redirect('success.html')  # Make sure this name matches your URL name

    return render(request, 'transaction.html')

def transaction_list(request):
    trans_page = trans.objects.all()
    return render(request, 'transaction_list.html', {'trans_page': trans_page})



def card_apply(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        employment_status = request.POST.get('employment_status')
        annual_income = request.POST.get('annual_income')
        card_type = request.POST.get('card_type')
        id_proof = request.FILES.get('id_proof')
        address_proof = request.FILES.get('address_proof')

        card_app = CardApplication(
            name=name,
            dob=dob,
            email=email,
            phone=phone,
            address=address,
            employment_status=employment_status,
            annual_income=annual_income,
            card_type=card_type,
            id_proof=id_proof,
            address_proof=address_proof
        )
        card_app.save()
        return redirect('success')  # Replace with your success page route name

    return render(request, 'card_apply.html')


def card_application_list(request):
    card_app = CardApplication.objects.all()
    return render(request, 'card_application_list.html', {'card_app': card_app})

# loan view

def loan(request):
    if request.method == 'POST':
        loan_type = request.POST.get('loanType')
        amount = request.POST.get('amount')
        duration = request.POST.get('duration')
        account_no = request.POST.get('accountNo')
        aadhar = request.POST.get('aadhar')
        pan = request.POST.get('pan')
        photo = request.FILES.get('photo')

        loan_form = LoanApplication(
            loan_type=loan_type,
            amount=amount,
            duration=duration,
            account_no=account_no,
            aadhar=aadhar,
            pan=pan,
            photo=photo
        )
        loan_form.save()
        return redirect('success')  # Replace 'success' with your actual success page name

    return render(request, 'loan.html') 

def loan_application_list(request):
    loan_form = LoanApplication.objects.all()
    return render(request, 'loan_application_list.html', {'loan_form': loan_form})


# Admin page view

def Admin_page(request):
    context = {
        'user_account_request_list': user_acount_request.objects.count(),
        'loan_applications_list': LoanApplication.objects.count(),
        'transaction_list': trans.objects.count(),
        'life_insurance_list': LifeInsuranceApplication.objects.count(),
        'health_insurance_list': HealthInsuranceApplication.objects.count(),
        'vehicle_insurance_list': VehicleInsurance.objects.count(),
        'card_application_list': CardApplication.objects.count(),
        'support': SupportRequest.objects.count(),
    }
    return render(request, 'Admin_page.html', context)
