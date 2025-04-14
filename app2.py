# Importing the Libraries
from supabase import create_client, Client
from flask import Flask, render_template, request, redirect, url_for, Blueprint
from dotenv import load_dotenv
import os

# Initialize blueprint
view = Blueprint('view', __name__)


# Load environment variables
load_dotenv()

# Initializing the app
app = Flask(__name__)

# Connecting to Supabase
url = os.getenv("SUPABASE_URI")
key = os.getenv("SUPABASE_API_KEY")
supabase: Client = create_client(url, key)

#Performing the Create and Read Operations

# 1. for adding and viewing airport data 

@view.route('/add_airport', methods=['GET', 'POST'])
def add_airport():
    if request.method == 'POST':
        data = {
            "name": request.form['name'],
            "city": request.form['city'],
            "contactno": request.form['contactno'],
            "address": request.form['address']
        }
        supabase.table('airport').insert(data).execute()
        return redirect(url_for('list_airports'))
    return render_template('airport.html')

@view.route('/airports')
def list_airports():
    data = supabase.table('airport').select("*").execute()
    return render_template('table_view.html', table_name="Airports", rows=data.data)

# 2. for adding and viewing employee data

@view.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        data = {
            "name": request.form['name'],
            "designation": request.form['designation'],
            "address": request.form['address'],
            "contactno": request.form['contactno']
        }
        supabase.table('employee').insert(data).execute()
        return redirect(url_for('list_employees'))
    return render_template('emp.html')

@view.route('/employees')
def list_employees():
    data = supabase.table('employee').select("*").execute()
    return render_template('table_view.html', table_name="Employees", rows=data.data)

# 3. for adding and viewing the plane data
@view.route('/add_plane', methods=['GET', 'POST'])
def add_plane():
    if request.method == 'POST':
        data = {
            "capacity": request.form['capacity'],
            "modeltype": request.form['modeltype'],
            "manufacturer": request.form['manufacturer'],
            "licenseno": request.form['licenseno']
        }
        supabase.table('plane').insert(data).execute()
        return redirect(url_for('list_planes'))
    return render_template('planeinfo.html')

@view.route('/planes')
def list_planes():
    data = supabase.table('plane').select("*").execute()
    return render_template('table_view.html', table_name="Planes", rows=data.data)

# 4. for adding and viewing the flight data

@view.route('/add_flight', methods=['GET', 'POST'])
def add_flight():
    if request.method == 'POST':
        data = {
            "sourceairportid": int(request.form['sourceairportid']),
            "destinationairportid": int(request.form['destinationairportid']),
            "arrivaltime": request.form['arrivaltime'],
            "departuretime": request.form['departuretime'],
            "fair": float(request.form['fair'])
        }
        supabase.table('flight').insert(data).execute()
        return redirect(url_for('list_flights'))
    return render_template('flightinfo.html')

@view.route('/flights')
def list_flights():
    data = supabase.table('flight').select("*").execute()
    return render_template('table_view.html', table_name="Flights", rows=data.data)

# 5. for adding and viewing passenger data

@view.route('/add_passenger', methods=['GET', 'POST'])
def add_passenger():
    if request.method == 'POST':
        data = {
            "name": request.form['name'],
            "address": request.form['address'],
            "contactno": request.form['contactno']
        }
        supabase.table('passenger').insert(data).execute()
        return redirect(url_for('list_passengers'))
    return render_template('passengerinfo.html')

@view.route('/passengers')
def list_passengers():
    data = supabase.table('passenger').select("*").execute()
    return render_template('table_view.html', table_name="Passengers", rows=data.data)

# 6. for adding and viewing flightSchedule data

@view.route('/add_flightschedule', methods=['GET', 'POST'])
def add_flightschedule():
    if request.method == 'POST':
        data = {
            "flightid": int(request.form['flightid']),
            "planeid": int(request.form['planeid']),
            "date": request.form['date']
        }
        supabase.table('flightschedule').insert(data).execute()
        return redirect(url_for('list_flightschedules'))
    return render_template('flightschedule.html')

@view.route('/flightschedules')
def list_flightschedules():
    data = supabase.table('flightschedule').select("*").execute()
    return render_template('table_view.html', table_name="Flight Schedules", rows=data.data)


# 7. for adding and viewing booking data

@view.route('/add_booking', methods=['GET', 'POST'])
def add_booking():
    if request.method == 'POST':
        data = {
            "passengerid": int(request.form['passengerid']),
            "scheduleid": int(request.form['scheduleid']),
            "seatno": request.form['seatno'],
            "bookingdate": request.form['bookingdate']
        }
        supabase.table('booking').insert(data).execute()
        return redirect(url_for('list_bookings'))
    return render_template('booking.html')

@view.route('/bookings')
def list_bookings():
    data = supabase.table('booking').select("*").execute()
    return render_template('table_view.html', table_name="Bookings", rows=data.data)


# 8. for adding and viewing flight employee data

@view.route('/add_flightemployee', methods=['GET', 'POST'])
def add_flightemployee():
    if request.method == 'POST':
        data = {
            "flightid": int(request.form['flightid']),
            "employeeid": int(request.form['employeeid']),
            "assignmentdate": request.form['assignmentdate'],
            "role": request.form['role']
        }
        supabase.table('flightemployee').insert(data).execute()
        return redirect(url_for('list_flightemployees'))
    return render_template('FlightEmployee.html')

@view.route('/flightemployees')
def list_flightemployees():
    data = supabase.table('flightemployee').select("*").execute()
    return render_template('table_view.html', table_name="Flight Employees", rows=data.data)


# Route to handle deletion of rows
@view.route('/delete/airport/<int:id>')
def delete_airport(id):
    supabase.table('airport').delete().eq('airportid', id).execute()
    return redirect(url_for('list_airports'))

@view.route('/delete/employee/<int:id>')
def delete_employee(id):
    supabase.table('employee').delete().eq('employeeid', id).execute()
    return redirect(url_for('list_employees'))

@view.route('/delete/plane/<int:id>')
def delete_plane(id):
    supabase.table('plane').delete().eq('planeid', id).execute()
    return redirect(url_for('list_planes'))

@view.route('/delete/flight/<int:id>')
def delete_flight(id):
    supabase.table('flight').delete().eq('flightid', id).execute()
    return redirect(url_for('list_flights'))

@view.route('/delete/passenger/<int:id>')
def delete_passenger(id):
    supabase.table('passenger').delete().eq('passengerid', id).execute()
    return redirect(url_for('list_passengers'))

@view.route('/delete/flightschedule/<int:id>')
def delete_flightschedule(id):
    supabase.table('flightschedule').delete().eq('scheduleid', id).execute()
    return redirect(url_for('list_flightschedules'))

@view.route('/delete/booking/<int:id>')
def delete_booking(id):
    supabase.table('booking').delete().eq('bookingid', id).execute()
    return redirect(url_for('list_bookings'))

@view.route('/delete/flightemployee/<int:id>')
def delete_flightemployee(id):
    supabase.table('flightemployee').delete().eq('flightemployeeid', id).execute()
    return redirect(url_for('list_flightemployees'))

## Updating the Data

# Update routes for each table
@view.route('/update/airport/<int:id>', methods=['GET', 'POST'])
def update_airport(id):
    if request.method == 'POST':
        data = {key: request.form[key] for key in request.form}
        supabase.table('airport').update(data).eq('airportid', id).execute()
        return redirect(url_for('list_airports'))
    else:
        response = supabase.table('airport').select("*").eq('airportid', id).execute()
        if response.data:
            return render_template("update_form.html", 
                                  row=response.data[0], 
                                  table_name="Airport", 
                                  primary_key="airportid")
        return "Record not found", 404

@view.route('/update/employee/<int:id>', methods=['GET', 'POST'])
def update_employee(id):
    if request.method == 'POST':
        data = {key: request.form[key] for key in request.form}
        supabase.table('employee').update(data).eq('employeeid', id).execute()
        return redirect(url_for('list_employees'))
    else:
        response = supabase.table('employee').select("*").eq('employeeid', id).execute()
        if response.data:
            return render_template("update_form.html", 
                                  row=response.data[0], 
                                  table_name="Employee", 
                                  primary_key="employeeid")
        return "Record not found", 404

@view.route('/update/plane/<int:id>', methods=['GET', 'POST'])
def update_plane(id):
    if request.method == 'POST':
        data = {key: request.form[key] for key in request.form}
        supabase.table('plane').update(data).eq('planeid', id).execute()
        return redirect(url_for('list_planes'))
    else:
        response = supabase.table('plane').select("*").eq('planeid', id).execute()
        if response.data:
            return render_template("update_form.html", 
                                  row=response.data[0], 
                                  table_name="Plane", 
                                  primary_key="planeid")
        return "Record not found", 404

@view.route('/update/flight/<int:id>', methods=['GET', 'POST'])
def update_flight(id):
    if request.method == 'POST':
        data = {key: request.form[key] for key in request.form}
        supabase.table('flight').update(data).eq('flightid', id).execute()
        return redirect(url_for('list_flights'))
    else:
        response = supabase.table('flight').select("*").eq('flightid', id).execute()
        if response.data:
            return render_template("update_form.html", 
                                  row=response.data[0], 
                                  table_name="Flight", 
                                  primary_key="flightid")
        return "Record not found", 404

@view.route('/update/passenger/<int:id>', methods=['GET', 'POST'])
def update_passenger(id):
    if request.method == 'POST':
        data = {key: request.form[key] for key in request.form}
        supabase.table('passenger').update(data).eq('passengerid', id).execute()
        return redirect(url_for('list_passengers'))
    else:
        response = supabase.table('passenger').select("*").eq('passengerid', id).execute()
        if response.data:
            return render_template("update_form.html", 
                                  row=response.data[0], 
                                  table_name="Passenger", 
                                  primary_key="passengerid")
        return "Record not found", 404

@view.route('/update/flightschedule/<int:id>', methods=['GET', 'POST'])
def update_flightschedule(id):
    if request.method == 'POST':
        data = {key: request.form[key] for key in request.form}
        supabase.table('flightschedule').update(data).eq('scheduleid', id).execute()
        return redirect(url_for('list_flightschedules'))
    else:
        response = supabase.table('flightschedule').select("*").eq('scheduleid', id).execute()
        if response.data:
            return render_template("update_form.html", 
                                  row=response.data[0], 
                                  table_name="Flight Schedule", 
                                  primary_key="scheduleid")
        return "Record not found", 404

@view.route('/update/booking/<int:id>', methods=['GET', 'POST'])
def update_booking(id):
    if request.method == 'POST':
        data = {key: request.form[key] for key in request.form}
        supabase.table('booking').update(data).eq('bookingid', id).execute()
        return redirect(url_for('list_bookings'))
    else:
        response = supabase.table('booking').select("*").eq('bookingid', id).execute()
        if response.data:
            return render_template("update_form.html", 
                                  row=response.data[0], 
                                  table_name="Booking", 
                                  primary_key="bookingid")
        return "Record not found", 404

# Special case for flightemployee which has a composite primary key
@view.route('/update/flightemployee/<int:flightid>/<int:employeeid>', methods=['GET', 'POST'])
def update_flightemployee(flightid, employeeid):
    if request.method == 'POST':
        data = {key: request.form[key] for key in request.form}
        supabase.table('flightemployee').update(data)\
               .eq('flightid', flightid)\
               .eq('employeeid', employeeid)\
               .execute()
        return redirect(url_for('list_flightemployees'))
    else:
        response = supabase.table('flightemployee').select("*")\
                  .eq('flightid', flightid)\
                  .eq('employeeid', employeeid)\
                  .execute()
        if response.data:
            return render_template("update_form.html", 
                                  row=response.data[0], 
                                  table_name="Flight Employee", 
                                  primary_key=None)  # No single primary key
        return "Record not found", 404

