// Initialize Lucide icons
document.addEventListener('DOMContentLoaded', function() {
    lucide.createIcons();
    initializeDashboard();
});

// Sample data for tables
const tableData = {
    airport: [
        {
            id: 'AP001',
            airportId: 'AP001',
            name: 'John F. Kennedy International Airport',
            city: 'New York',
            contactNo: '+1 (718) 244-4444',
            address: 'Queens, NY 11430, United States'
        },
        {
            id: 'AP002',
            airportId: 'AP002',
            name: 'Heathrow Airport',
            city: 'London',
            contactNo: '+44 844 335 1801',
            address: 'Longford, Hounslow TW6, United Kingdom'
        },
        {
            id: 'AP003',
            airportId: 'AP003',
            name: 'Dubai International Airport',
            city: 'Dubai',
            contactNo: '+971 4 224 5555',
            address: 'Dubai, United Arab Emirates'
        }
    ],
    plane: [
        {
            id: 'PL001',
            planeId: 'PL001',
            model: 'Boeing 787-9',
            capacity: 290,
            manufacturer: 'Boeing',
            year: 2018
        },
        {
            id: 'PL002',
            planeId: 'PL002',
            model: 'Airbus A350-900',
            capacity: 325,
            manufacturer: 'Airbus',
            year: 2019
        }
    ],
    flight: [
        {
            id: 'FL001',
            flightId: 'FL001',
            origin: 'New York (JFK)',
            destination: 'London (LHR)',
            distance: 5541,
            duration: '7h 30m',
            planeId: 'PL001'
        },
        {
            id: 'FL002',
            flightId: 'FL002',
            origin: 'London (LHR)',
            destination: 'Dubai (DXB)',
            distance: 3400,
            duration: '6h 45m',
            planeId: 'PL002'
        }
    ],
    flightSchedule: [
        {
            id: 'FS001',
            scheduleId: 'FS001',
            flightId: 'FL001',
            departureTime: '2025-05-15T08:30:00',
            arrivalTime: '2025-05-15T16:00:00',
            status: 'Scheduled'
        },
        {
            id: 'FS002',
            scheduleId: 'FS002',
            flightId: 'FL002',
            departureTime: '2025-05-16T14:15:00',
            arrivalTime: '2025-05-16T21:00:00',
            status: 'Scheduled'
        }
    ],
    passenger: [
        {
            id: 'PS001',
            passengerId: 'PS001',
            firstName: 'John',
            lastName: 'Smith',
            email: 'john.smith@example.com',
            phone: '+1 555-123-4567',
            passportNo: 'AB1234567'
        },
        {
            id: 'PS002',
            passengerId: 'PS002',
            firstName: 'Emma',
            lastName: 'Johnson',
            email: 'emma.j@example.com',
            phone: '+44 7700 900123',
            passportNo: 'CD7654321'
        }
    ],
    booking: [
        {
            id: 'BK001',
            bookingId: 'BK001',
            passengerId: 'PS001',
            scheduleId: 'FS001',
            bookingDate: '2025-04-10',
            seatNo: '12A',
            class: 'Business',
            status: 'Confirmed'
        },
        {
            id: 'BK002',
            bookingId: 'BK002',
            passengerId: 'PS002',
            scheduleId: 'FS002',
            bookingDate: '2025-04-12',
            seatNo: '18F',
            class: 'Economy',
            status: 'Confirmed'
        }
    ],
    employee: [
        {
            id: 'EM001',
            employeeId: 'EM001',
            firstName: 'Sarah',
            lastName: 'Wilson',
            position: 'Pilot',
            email: 'sarah.w@abcairlines.com',
            phone: '+1 555-987-6543',
            hireDate: '2020-06-15'
        },
        {
            id: 'EM002',
            employeeId: 'EM002',
            firstName: 'Michael',
            lastName: 'Brown',
            position: 'Flight Attendant',
            email: 'michael.b@abcairlines.com',
            phone: '+1 555-456-7890',
            hireDate: '2021-02-10'
        }
    ],
    flightEmployee: [
        {
            id: 'FE001',
            assignmentId: 'FE001',
            scheduleId: 'FS001',
            employeeId: 'EM001',
            role: 'Captain',
            status: 'Assigned'
        },
        {
            id: 'FE002',
            assignmentId: 'FE002',
            scheduleId: 'FS001',
            employeeId: 'EM002',
            role: 'Cabin Crew',
            status: 'Assigned'
        }
    ]
};

// Table schema definitions for form generation
const tableSchema = {
    airport: [
        { name: 'airportId', label: 'Airport ID', type: 'text' },
        { name: 'name', label: 'Airport Name', type: 'text' },
        { name: 'city', label: 'City', type: 'text' },
        { name: 'contactNo', label: 'Contact Number', type: 'tel' },
        { name: 'address', label: 'Address', type: 'textarea' }
    ],
    plane: [
        { name: 'planeId', label: 'Plane ID', type: 'text' },
        { name: 'model', label: 'Model', type: 'text' },
        { name: 'capacity', label: 'Capacity', type: 'number' },
        { name: 'manufacturer', label: 'Manufacturer', type: 'text' },
        { name: 'year', label: 'Year', type: 'number' }
    ],
    flight: [
        { name: 'flightId', label: 'Flight ID', type: 'text' },
        { name: 'origin', label: 'Origin', type: 'text' },
        { name: 'destination', label: 'Destination', type: 'text' },
        { name: 'distance', label: 'Distance (km)', type: 'number' },
        { name: 'duration', label: 'Duration', type: 'text' },
        { name: 'planeId', label: 'Plane ID', type: 'select', options: 'plane' }
    ],
    flightSchedule: [
        { name: 'scheduleId', label: 'Schedule ID', type: 'text' },
        { name: 'flightId', label: 'Flight ID', type: 'select', options: 'flight' },
        { name: 'departureTime', label: 'Departure Time', type: 'datetime-local' },
        { name: 'arrivalTime', label: 'Arrival Time', type: 'datetime-local' },
        { name: 'status', label: 'Status', type: 'select', options: ['Scheduled', 'Delayed', 'Cancelled', 'Completed'] }
    ],
    passenger: [
        { name: 'passengerId', label: 'Passenger ID', type: 'text' },
        { name: 'firstName', label: 'First Name', type: 'text' },
        { name: 'lastName', label: 'Last Name', type: 'text' },
        { name: 'email', label: 'Email', type: 'email' },
        { name: 'phone', label: 'Phone', type: 'tel' },
        { name: 'passportNo', label: 'Passport No', type: 'text' }
    ],
    booking: [
        { name: 'bookingId', label: 'Booking ID', type: 'text' },
        { name: 'passengerId', label: 'Passenger ID', type: 'select', options: 'passenger' },
        { name: 'scheduleId', label: 'Schedule ID', type: 'select', options: 'flightSchedule' },
        { name: 'bookingDate', label: 'Booking Date', type: 'date' },
        { name: 'seatNo', label: 'Seat No', type: 'text' },
        { name: 'class', label: 'Class', type: 'select', options: ['Economy', 'Premium Economy', 'Business', 'First'] },
        { name: 'status', label: 'Status', type: 'select', options: ['Confirmed', 'Cancelled', 'Checked-in'] }
    ],
    employee: [
        { name: 'employeeId', label: 'Employee ID', type: 'text' },
        { name: 'firstName', label: 'First Name', type: 'text' },
        { name: 'lastName', label: 'Last Name', type: 'text' },
        { name: 'position', label: 'Position', type: 'text' },
        { name: 'email', label: 'Email', type: 'email' },
        { name: 'phone', label: 'Phone', type: 'tel' },
        { name: 'hireDate', label: 'Hire Date', type: 'date' }
    ],
    flightEmployee: [
        { name: 'assignmentId', label: 'Assignment ID', type: 'text' },
        { name: 'scheduleId', label: 'Schedule ID', type: 'select', options: 'flightSchedule' },
        { name: 'employeeId', label: 'Employee ID', type: 'select', options: 'employee' },
        { name: 'role', label: 'Role', type: 'select', options: ['Captain', 'First Officer', 'Cabin Crew', 'Purser'] },
        { name: 'status', label: 'Status', type: 'select', options: ['Assigned', 'Unassigned', 'On Leave'] }
    ]
};

// Current table being displayed
let currentTable = 'airport';
let editMode = false;
let currentRecordId = null;

// Initialize dashboard
function initializeDashboard() {
    // Set up menu click handlers
    setupMenuHandlers();
    
    // Generate tables for all entities
    generateAllTables();
    
    // Show default table (airport)
    showTable('airport');
}

// Set up menu click handlers
function setupMenuHandlers() {
    document.querySelectorAll('.menu-item').forEach(item => {
        item.addEventListener('click', function() {
            const tableName = this.getAttribute('data-table') || this.textContent.trim().toLowerCase().replace(/\s+/g, '');
            showTable(tableName);
        });
    });
}

// Generate all tables based on schema
function generateAllTables() {
    Object.keys(tableSchema).forEach(tableName => {
        generateTable(tableName);
    });
}

// Generate a single table
function generateTable(tableName) {
    // Create table container if it doesn't exist
    let tableContainer = document.getElementById(`${tableName}-table`);
    if (!tableContainer) {
        tableContainer = document.createElement('div');
        tableContainer.id = `${tableName}-table`;
        tableContainer.className = 'table-container hidden';
        
        const tableHeader = document.createElement('div');
        tableHeader.className = 'table-header';
        tableHeader.innerHTML = `<h2>${formatTableName(tableName)} Information</h2>`;
        
        tableContainer.appendChild(tableHeader);
        
        const table = document.createElement('table');
        const thead = document.createElement('thead');
        const tbody = document.createElement('tbody');
        tbody.id = `${tableName}-tbody`;
        
        // Create table headers
        const headerRow = document.createElement('tr');
        tableSchema[tableName].forEach(column => {
            const th = document.createElement('th');
            th.textContent = column.label;
            headerRow.appendChild(th);
        });
        
        // Add actions column
        const actionsHeader = document.createElement('th');
        actionsHeader.textContent = 'Actions';
        headerRow.appendChild(actionsHeader);
        
        thead.appendChild(headerRow);
        table.appendChild(thead);
        table.appendChild(tbody);
        tableContainer.appendChild(table);
        
        document.querySelector('.main-content').appendChild(tableContainer);
    }
    
    // Update table data
    updateTableData(tableName);
}

// Update table data
function updateTableData(tableName) {
    const tbody = document.getElementById(`${tableName}-tbody`);
    if (!tbody) return;
    
    tbody.innerHTML = '';
    
    // Add table rows
    tableData[tableName].forEach(record => {
        const row = document.createElement('tr');
        
        tableSchema[tableName].forEach(column => {
            const cell = document.createElement('td');
            cell.textContent = record[column.name] || '';
            row.appendChild(cell);
        });
        
        // Add action buttons
        const actionsCell = document.createElement('td');
        actionsCell.className = 'action-cell';
        
        // Edit button
        const editBtn = document.createElement('button');
        editBtn.className = 'icon-button edit-btn';
        editBtn.innerHTML = '<i data-lucide="edit" style="width: 18px;"></i>';
        editBtn.addEventListener('click', () => openEditModal(tableName, record.id));
        
        // Delete button
        const deleteBtn = document.createElement('button');
        deleteBtn.className = 'icon-button delete-btn';
        deleteBtn.innerHTML = '<i data-lucide="trash-2" style="width: 18px;"></i>';
        deleteBtn.addEventListener('click', () => deleteRecord(tableName, record.id));
        
        actionsCell.appendChild(editBtn);
        actionsCell.appendChild(deleteBtn);
        row.appendChild(actionsCell);
        
        tbody.appendChild(row);
    });
    
    // Reinitialize Lucide icons for dynamic content
    lucide.createIcons();
}

// Show/hide tables based on selection
function showTable(tableName) {
    // Hide all tables
    document.querySelectorAll('.table-container').forEach(table => {
        table.classList.add('hidden');
    });
    
    // Show selected table
    const selectedTable = document.getElementById(`${tableName}-table`);
    if (selectedTable) {
        selectedTable.classList.remove('hidden');
    }
    
    // Update current table title
    document.getElementById('current-table-title').textContent = formatTableName(tableName);
    
    // Update active menu item
    document.querySelectorAll('.menu-item').forEach(item => {
        item.classList.remove('active');
        
        const itemTable = item.getAttribute('data-table') || 
                          item.textContent.trim().toLowerCase().replace(/\s+/g, '');
        
        if (itemTable === tableName) {
            item.classList.add('active');
        }
    });
    
    // Update current table reference
    currentTable = tableName;
}

// Format table name for display
function formatTableName(tableName) {
    return tableName
        .replace(/([A-Z])/g, ' $1')
        .replace(/^./, str => str.toUpperCase())
        .trim();
}

// Open modal for adding a new record
function openAddModal() {
    document.getElementById('modal-title').textContent = `Add ${formatTableName(currentTable)}`;
    
    // Generate form based on schema
    generateForm(currentTable);
    
    // Show modal
    document.getElementById('modal-overlay').classList.add('active');
    
    // Set mode
    editMode = false;
    currentRecordId = null;
}

// Open modal for editing an existing record
function openEditModal(tableName, id) {
    document.getElementById('modal-title').textContent = `Edit ${formatTableName(tableName)}`;
    
    // Generate form based on schema
    generateForm(tableName);
    
    // Find record
    const record = tableData[tableName].find(item => item.id === id);
    
    if (record) {
        // Populate form with record data
        tableSchema[tableName].forEach(column => {
            const input = document.getElementById(column.name);
            if (input) {
                input.value = record[column.name] || '';
            }
        });
    }
    
    // Show modal
    document.getElementById('modal-overlay').classList.add('active');
    
    // Set mode
    editMode = true;
    currentTable = tableName;
    currentRecordId = id;
}

// Generate form based on schema
function generateForm(tableName) {
    const form = document.getElementById('record-form');
    form.innerHTML = '';
    
    tableSchema[tableName].forEach(field => {
        const formGroup = document.createElement('div');
        formGroup.className = 'form-group';
        
        const label = document.createElement('label');
        label.setAttribute('for', field.name);
        label.textContent = field.label;
        
        let input;
        
        if (field.type === 'textarea') {
            input = document.createElement('textarea');
        } else if (field.type === 'select') {
            input = document.createElement('select');
            
            // Add options
            if (typeof field.options === 'string') {
                // Options from another table
                if (tableData[field.options]) {
                    tableData[field.options].forEach(option => {
                        const optEl = document.createElement('option');
                        optEl.value = option.id;
                        
                        // Display value based on entity type
                        if (field.options === 'passenger') {
                            optEl.textContent = `${option.firstName} ${option.lastName} (${option.passengerId})`;
                        } else if (field.options === 'flight') {
                            optEl.textContent = `${option.origin} to ${option.destination} (${option.flightId})`;
                        } else if (field.options === 'flightSchedule') {
                            const flight = tableData.flight.find(f => f.id === option.flightId);
                            const departureDate = new Date(option.departureTime).toLocaleDateString();
                            optEl.textContent = `${flight ? flight.origin + ' to ' + flight.destination : ''} - ${departureDate} (${option.scheduleId})`;
                        } else if (field.options === 'employee') {
                            optEl.textContent = `${option.firstName} ${option.lastName} - ${option.position} (${option.employeeId})`;
                        } else if (field.options === 'plane') {
                            optEl.textContent = `${option.model} (${option.planeId})`;
                        } else {
                            optEl.textContent = option.id;
                        }
                        
                        input.appendChild(optEl);
                    });
                }
            } else if (Array.isArray(field.options)) {
                // Static options
                field.options.forEach(option => {
                    const optEl = document.createElement('option');
                    optEl.value = option;
                    optEl.textContent = option;
                    input.appendChild(optEl);
                });
            }
        } else {
            input = document.createElement('input');
            input.type = field.type;
        }
        
        input.id = field.name;
        input.name = field.name;
        input.placeholder = `Enter ${field.label.toLowerCase()}`;
        
        if (field.type !== 'select') {
            input.required = true;
        }
        
        formGroup.appendChild(label);
        formGroup.appendChild(input);
        form.appendChild(formGroup);
    });
}

// Close modal
function closeModal() {
    document.getElementById('modal-overlay').classList.remove('active');
}

// Save record (add or update)
function saveRecord() {
    // Get form data
    const form = document.getElementById('record-form');
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());
    
    // Add ID if editing
    if (editMode && currentRecordId) {
        data.id = currentRecordId;
    } else {
        // Generate new ID for new records
        const idField = tableSchema[currentTable][0].name;
        data.id = data[idField];
    }
    
    // Update data store
    if (editMode) {
        // Update existing record
        const index = tableData[currentTable].findIndex(item => item.id === currentRecordId);
        if (index !== -1) {
            tableData[currentTable][index] = data;
        }
    } else {
        // Add new record
        tableData[currentTable].push(data);
    }
    
    // Update table
    updateTableData(currentTable);
    
    // Show success message
    alert(`${editMode ? 'Updated' : 'Added'} ${formatTableName(currentTable)} successfully!`);
    
    // Close modal
    closeModal();
}

// Delete record
function deleteRecord(tableName, id) {
    if (confirm(`Are you sure you want to delete this ${formatTableName(tableName)}?`)) {
        // Remove record from data store
        const index = tableData[tableName].findIndex(item => item.id === id);
        if (index !== -1) {
            tableData[tableName].splice(index, 1);
        }
        
        // Update table
        updateTableData(tableName);
        
        // Show success message
        alert(`${formatTableName(tableName)} deleted successfully!`);
    }
} 