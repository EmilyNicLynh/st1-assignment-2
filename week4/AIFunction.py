appointments = []  # A plain list — no database, no GUI

def store_appointment(patient_name, practitioner_name, appointment_time):
    """Store a basic appointment using simple Python data types."""
    
    # Basic validation to help beginners avoid silent errors
    if not patient_name:
        raise ValueError("Patient name cannot be empty.")
    if not practitioner_name:
        raise ValueError("Practitioner name cannot be empty.")
    if not appointment_time:
        raise ValueError("Appointment time cannot be empty.")
    
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    
    appointments.append(appointment)
    print("Appointment stored successfully!")