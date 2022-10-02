import requests

url = 'http://localhost:5000/predict_api'
#url = "https://aw.moevinc.com/predict_api"
r = requests.post(url,json={'current_hour':12, 
							'current_day':2,
							'starting_SOC':90,
							"Miles_Driven":12,
							"Starting_Alt":30,
							"Max_Speed":21,
							"Accu_Descending":-986,
							"Accu_Ascending":50,
							"Average_temp":75})

print(r.json)



