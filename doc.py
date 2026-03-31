wards = {
    "Cardiology": ["Alice", "Bob", "Carol"],
    "Neurology": ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology": ["Ivy", "Bob"],
}

staff = {}

for dept, docs in wards.items():
    print(staff, dept)