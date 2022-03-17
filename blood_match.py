import requests

server = "http://vcm-7631.vm.duke.edu:5002"

r = requests.get(server+"/get_patients/th265")
print(r.status_code)
print(r.text)

don = requests.get(server+"/get_blood_type/M7")
print("status_code:" + str(don.status_code))
print("Donor blood type:" + don.text)

reci = requests.get(server+"/get_blood_type/F1")
print("status_code:" + str(reci.status_code))
print("Recipient blood type:" + reci.text)


def compat(donor, recipient):
    if recipient == 'A+':
        if donor == 'A+' or 'A-' or 'O+' or 'O-':
            return "Yes"
        else:
            return "No"
    elif recipient == 'A-':
        if donor == 'A-' or 'O-':
            return "Yes"
        else:
            return "No"
    elif recipient == 'B+':
        if donor == 'B+' or 'B-' or 'O+' or 'O-':
            return "Yes"
        else:
            return "No"
    elif recipient == 'B-':
        if donor == 'B-' or 'O-':
            return "Yes"
        else:
            return "No"
    elif recipient == 'AB+':
        return 'Yes'
    elif recipient == 'A-':
        if donor == 'AB-' or 'A-' or 'B-' or 'O-':
            return "Yes"
        else:
            return "No"
    elif recipient == 'O+':
        if donor == 'O+' or 'O-':
            return "Yes"
        else:
            return "No"
    elif recipient == 'O-':
        if donor == 'O-':
            return "Yes"
        else:
            return "No"

print("Acceptable? " + compat(don.text, reci.text))

out_data = {'Name': "th265", 'Match': compat(don.text, reci.text)}
r = requests.post(server+"/match_check", json=out_data)
print("status_code:" + str(r.status_code))
print("Answer is " + r.text)

    