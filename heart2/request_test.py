import requests

url = 'http://127.0.0.1:8000/predict/'

test_data = [
    [62, 1, 1, 140, 271, 0, 1, 152, 0, 1, 2],  # Heart Failure Detected
    [49, 0, 0, 105, 200, 1, 2, 175, 1, 1.5, 2],  # No Heart Failure Detected
    [37, 1, 0, 130, 315, 0, 1, 158, 0, 0, 2],    # No Heart Failure Detected
    [55, 0, 1, 132, 342, 0, 1, 166, 0, 1.2, 2],  # No Heart Failure Detected
    [42, 0, 2, 115, 211, 0, 2, 137, 0, 0, 2],    # No Heart Failure Detected
    [42, 1, 2, 160, 147, 0, 1, 146, 0, 0, 2],    # Heart Failure Detected
    [40, 1, 0, 120, 230, 0, 1, 140, 0, 0.5, 1],  # No Heart Failure Detected
    [60, 0, 1, 128, 250, 0, 2, 155, 1, 0.7, 2]   # No Heart Failure Detected
]

for data in test_data:
    response = requests.post(url, data={
        'age': data[0],
        'sex': data[1],
        'chest_pain_type': data[2],
        'resting_bp': data[3],
        'cholesterol': data[4],
        'fasting_bs': data[5],
        'resting_ecg': data[6],
        'max_hr': data[7],
        'exercise_angina': data[8],
        'oldpeak': data[9],
        'slope': data[10]
    })
    print(response.json())