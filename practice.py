import json
from collections import Counter

with open('medical_records.json', 'r') as file:
    data = json.load(file)



# Question 1 What percentage of patients are smokers or have a history with tobacco use?
total_patients = len(data["Patient_Social_History"])
smokers_count = 0

for patient in data["Patient_Social_History"]:
    if patient["Tobacco_Use"] == "TRUE":
        smokers_count += 1

percentage_smokers = (smokers_count / total_patients) * 100
print(f"Percentage of patients who are smokers or have a history of tobacco use: {percentage_smokers:.2f}%")




# Question 2 What is the most common type of insurance provider among patients? 
insurance_companies = [entry['Company_Name'] for entry in data['Patient_Insurance_Info']]
insurance_count = Counter(insurance_companies)
most_common_insurance = insurance_count.most_common(1)
print(f"The most common insurance provider is {most_common_insurance[0][0]} with {most_common_insurance[0][1]} patients.")




# Question 3 What are the most common age groups of patients visiting the facility? 
ages = [patient['Age'] for patient in data['Patient_Info']]
age_groups = {
    "18-29": (18, 29),
    "30-39": (30, 39),
    "40-49": (40, 49),
    "50-59": (50, 59),
    "60+": (60, float('inf'))
}

grouped_ages = []

for age in ages:
    for group, (lower, upper) in age_groups.items():
        if lower <= age <= upper:
            grouped_ages.append(group)
            break

age_group_counts = Counter(grouped_ages)
most_common_age_group = age_group_counts.most_common(1)
print(f"The most common age group is: {most_common_age_group[0][0]} with {most_common_age_group[0][1]} patients.")




# Question 4 We can ask what’s the most common allergy amongst the patients

all_allergies = []
# Collecting all allergies from each patient
for patient in data['Patient_Allergies']:
    allergies = patient.get('Patient_Allergies', [])
    for allergy in allergies:
        all_allergies.append(allergy['Allergy_Name'])
# print(patient)

# Count the occurrences of each allergy
allergy_counts = Counter(all_allergies)

# Get the most common allergy
most_common_allergy = allergy_counts.most_common(1)

# Print the most common allergy or a message if no allergies were found
if most_common_allergy:
    print(f"The most common allergy is: {most_common_allergy[0][0]} with {most_common_allergy[0][1]} occurrences.")
else:
    print("No allergies found.")


# Question 5 which pharmacy is used the most with our patients
pharmacy_usage = {}

for patient in data["Pharmacy"]:
    pharmacy_name = patient["Location"]
    if pharmacy_name in pharmacy_usage:
        pharmacy_usage[pharmacy_name] += 1
    else:
        pharmacy_usage[pharmacy_name] = 1

most_used_pharmacy = max(pharmacy_usage, key=pharmacy_usage.get)
print(f"The most used pharmacy is: {most_used_pharmacy}")