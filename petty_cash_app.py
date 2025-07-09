import pyrebase
from openpyxl import Workbook

# --- Firebase Configuration ---
firebaseConfig = {
    "apiKey": "AIzaSyAWTW8hg3iy8NjyxoFqKQ0lhtcvPzz-XWQ",
    "authDomain": "petty-cash-b66cb.firebaseapp.com",
    "databaseURL": "https://petty-cash-b66cb-default-rtdb.firebaseio.com",
    "projectId": "petty-cash-b66cb",
    "storageBucket": "petty-cash-b66cb.appspot.com",  # ✅ FIXED bucket domain
    "messagingSenderId": "514761669149",
    "appId": "1:514761669149:web:ad58d09976f3f89080e4f4",
    "measurementId": "G-MFE8MMYM8C"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

# --- Add Entry Function ---
def add_petty_cash(amount, description, paid_to, paid_by, date):
    data = {
        "amount by company": amount by company,
        "description": description,
        "paid_to": paid_to,
    
            "paid_by": paid_by,
        "date": date
    }
    db.child("petty_cash").push(data)
    print("✅ Entry Added to Firebase")

# --- Export All Entries to Excel ---
def export_to_excel():
    data = db.child("petty_cash").get()

    wb = Workbook()
    ws = wb.active
    ws.title = "Petty Cash Entries"

    # Headers
    ws.append(["Amount", "Description", "Paid To", "Paid By", "Date"])

    # Rows
    for entry in data.each():
        record = entry.val()
        ws.append([
            record.get("amount by company"),
            record.get("description"),
            record.get("paid_to"),
            record.get("paid_by"),
            record.get("date")
        ])

    file_name = "petty_cash_export.xlsx"
    wb.save(file_name)
    print(f"📁 Data exported to Excel → {file_name}")

# --- Run Program ---
add_petty_cash(500, "Tea & Snacks", "Vendor A", "Darshan", "2025-07-05")
export_to_excel()

