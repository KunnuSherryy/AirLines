# Importing the Libraries
from supabase import create_client, Client
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os

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

@app.route('/add_airport', methods=['GET', 'POST'])
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

@app.route('/airports')
def list_airports():
    data = supabase.table('airport').select("*").execute()
    return render_template('table_view.html', table_name="Airports", rows=data.data)

# 2. for adding and viewing employee data

@app.route('/add_employee', methods=['GET', 'POST'])
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

@app.route('/employees')
def list_employees():
    data = supabase.table('employee').select("*").execute()
    return render_template('table_view.html', table_name="Employees", rows=data.data)

# 3. for adding and viewing the plane data
@app.route('/add_plane', methods=['GET', 'POST'])
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

@app.route('/planes')
def list_planes():
    data = supabase.table('plane').select("*").execute()
    return render_template('table_view.html', table_name="Planes", rows=data.data)

# 4. for adding and viewing the flight data

@app.route('/add_flight', methods=['GET', 'POST'])
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

@app.route('/flights')
def list_flights():
    data = supabase.table('flight').select("*").execute()
    return render_template('table_view.html', table_name="Flights", rows=data.data)

# 5. for adding and viewing passenger data

@app.route('/add_passenger', methods=['GET', 'POST'])
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

@app.route('/passengers')
def list_passengers():
    data = supabase.table('passenger').select("*").execute()
    return render_template('table_view.html', table_name="Passengers", rows=data.data)

# 6. for adding and viewing flightSchedule data

@app.route('/add_flightschedule', methods=['GET', 'POST'])
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

@app.route('/flightschedules')
def list_flightschedules():
    data = supabase.table('flightschedule').select("*").execute()
    return render_template('table_view.html', table_name="Flight Schedules", rows=data.data)


# 7. for adding and viewing booking data

@app.route('/add_booking', methods=['GET', 'POST'])
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

@app.route('/bookings')
def list_bookings():
    data = supabase.table('booking').select("*").execute()
    return render_template('table_view.html', table_name="Bookings", rows=data.data)


# 8. for adding and viewing flight employee data

@app.route('/add_flightemployee', methods=['GET', 'POST'])
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

@app.route('/flightemployees')
def list_flightemployees():
    data = supabase.table('flightemployee').select("*").execute()
    return render_template('table_view.html', table_name="Flight Employees", rows=data.data)


if __name__ =='__main__':
    app.run(debug=True)
=======

>>>>>>> fd26e9ecfc60e385169980c8d844d8025166c1c8
