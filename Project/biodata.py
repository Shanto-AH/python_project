def collect_biodata():
    print("Enter your details:")
    name = input("Full Name: ")
    age = input("Age: ")
    gender = input("Gender: ")
    email = input("Email: ")
    phone = input("Phone Number: ")
    address = input("Address: ")
    
    biodata = {
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Email": email,
        "Phone": phone,
        "Address": address
    }
    
    return biodata

def display_biodata(biodata):
    print("\n===== User Biodata =====")
    for key, value in biodata.items():
        print(f"{key}: {value}")
    print("========================")

if __name__ == "__main__":
    user_data = collect_biodata()
    display_biodata(user_data)
