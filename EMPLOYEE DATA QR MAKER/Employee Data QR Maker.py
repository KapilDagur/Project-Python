import pyqrcode
import png
from  pyqrcode import QRCode
EMPLOYEE_ID = int(input("Enter Employee : "))
EMPLOYEE_NAME = input("Enter Employee Name : ")
EMPLOYEE_POST = input("Enter Employe Post Name : ")
EMPLOYEE_JOINING_YEAR = input("Enter Session (In YYYY-YYYY) : ")
EMPLOYEE_BLOOD_GROUP = input("Enter Blood Group : ")
EMPLOYEE_CONTACT_NUMBER = int(input("ENTER MOBILE NO : "))
EMPLOYEE_DATA = f"""EMPLOYEE ID : {EMPLOYEE_ID}
EMPLOYEE NAME : {EMPLOYEE_NAME}
EMPLOYEE POST NAME : {EMPLOYEE_POST}
EMPLOYEE JOINING YEAR : {EMPLOYEE_JOINING_YEAR}
EMPLOYEE BLOOD GROUP : {EMPLOYEE_BLOOD_GROUP}
EMPLOYEE CONTACT NO : +91 {EMPLOYEE_CONTACT_NUMBER}"""
EMPLOYEE_QR = pyqrcode.create(EMPLOYEE_DATA)
EMPLOYEE_QR.png(f"{EMPLOYEE_ID}.png",scale = 6)
