{
    "name": "Hospital Management",
    "summary": "Manage hospital system",
    "author": "Mohammed alhelal",
    "license": "LGPL-3",
    "version": "1.0.0",
    "category": "Hospital",
    "depends": ["mail", "product"],
    "sequence": -100,
    "data": [
        "security/ir.model.access.csv",
        "data/patient_tag_data.xml",
        "data/patient.tag.csv",
        "data/sequence_data.xml",
        "wizards/views/cancel_appointment_view.xml",
        "views/hospital_actions.xml",
        "views/patient_view.xml",
        "views/appointment_view.xml",
        "views/patient_tag_view.xml",
        "views/hospital_menu.xml" 
    ],
    "demo": [
    ],
    "application": True,
    "auto_install": False
}
