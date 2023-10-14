# 1. 필요한 라이브러리 임포트
import requests
import json
import openai
from dotenv import load_dotenv
import os
import time

# # 1. check_bio
# url = "http://localhost:8010/check_bio/"
# url = "http://c16d-182-230-164-18.ngrok.io/check_bio/"
# data = {"linkedin_url": "https://www.linkedin.com/in/jongwon-park-247692147/"}
# start_time = time.time()
# res = requests.post(url, data=json.dumps(data), timeout=600)
# end_time = time.time()
# print(res.text)
# print(f"elapsed time: {end_time - start_time} seconds")

# # 2. generate_initial_ideas
# url = "http://localhost:8010/generate_initial_ideas/"
# data = {"linkedin_summary": """I am interested in ML applications that can make a real-world impact.[Experience(institution_name='Antler · Full-time', linkedin_url='https://www.linkedin.com/company/27221633/', website=None, industry=None, type=None, headquarters=None, company_size=None, founded=None, from_date='Sep 2023', to_date='Present', description='Make something big\nMake something big', position_title='Enterpreneur in Antler', duration='2 mos', location='Seoul, South Korea · On-site'), Experience(institution_name='MakinaRocks · Full-time', linkedin_url='https://www.linkedin.com/company/13752292/', website=None, industry=None, type=None, headquarters=None, company_size=None, founded=None, from_date='Jun 2022', to_date='Jul 2023', description='* Control optimization of HVAC system in an electric car. I improved the performance of the RL agent in a model-based manner. \n* PID auto-tuning agent for industrial machines, proof of concept. I developed a reward model and RL agent using one-step MDP.\n* Control optimization of HVAC system in an electric car. I improved the performance of the RL agent in a model-based manner. * PID auto-tuning agent for industrial machines, proof of concept. I developed a reward model and RL agent using one-step MDP.', position_title='Machine Learning Engineer', duration='1 yr 2 mos', location='Gangnam District, Seoul, South Korea'), Experience(institution_name='Seoul National University · Full-time', linkedin_url='https://www.linkedin.com/company/15096106/', website=None, industry=None, type=None, headquarters=None, company_size=None, founded=None, from_date='Sep 2019', to_date='Jul 2022', description='', position_title='Masters Candidate', duration='2 yrs 11 mos', location=''), Experience(institution_name='Tesser Inc. · Part-time', linkedin_url='https://www.linkedin.com/company/13210718/', website=None, industry=None, type=None, headquarters=None, company_size=None, founded=None, from_date='Aug 2021', to_date='Dec 2021', description='I used 3D brain segmentation model for detecting malignant tumors.\nI used 3D brain segmentation model for detecting malignant tumors.', position_title='AI Researcher', duration='5 mos', location=''), Experience(institution_name='Test and Evaluation Group, ROK Army · Full-time', linkedin_url='https://www.linkedin.com/search/results/all/?keywords=Test+and+Evaluation+Group%2C+ROK+Army', website=None, industry=None, type=None, headquarters=None, company_size=None, founded=None, from_date='Jan 2020', to_date='Jul 2021', description='I submitted several academic papers and proposals about defense science.\nOne of my proposals named "Testing Off-Road Self-Driving using Simulation" was accepted by the Defense Experiment Program (AKA Korean DARPA).\nI submitted several academic papers and proposals about defense science. One of my proposals named "Testing Off-Road Self-Driving using Simulation" was accepted by the Defense Experiment Program (AKA Korean DARPA).', position_title='AI Researcher at ROK Army', duration='1 yr 7 mos', location=''), Experience(institution_name='Computer Vision Lab, Seoul National University · Full-time', linkedin_url='https://www.linkedin.com/search/results/all/?keywords=Computer+Vision+Lab%2C+Seoul+National+University', website=None, industry=None, type=None, headquarters=None, company_size=None, founded=None, from_date='Oct 2018', to_date='Feb 2019', description='Won the best undergrad paper award from Korea Computer Congress 2019.\n"Efficient Pseudo Labeler for Semi-Supervised Semantic Segmentation"\nWon the best undergrad paper award from Korea Computer Congress 2019. "Efficient Pseudo Labeler for Semi-Supervised Semantic Segmentation"', position_title='Research Assistant', duration='5 mos', location='')][Education(institution_name='Sungkyunkwan University', linkedin_url='https://www.linkedin.com/company/15096111/', website=None, industry=None, type=None, headquarters=None, company_size=None, founded=None, from_date='2014 -', to_date='', description='', degree="Bachelor's degree, Computer Science")][][]""", 
#         "interests": "software, ai, medical"}
# res = requests.post(url, data=json.dumps(data))


# 3. discuss to business plan
# url = "http://localhost:8010/discuss/"
url = "http://c16d-182-230-164-18.ngrok.io/discuss/"
data = {
    "log": {
        "service_name" : "MedBot Analytics",
        "problem": "Ineffective tracking and predictive analysis of patient health, leading to delayed treatments.",
        "service_idea" : "Develop an AI-driven platform that uses machine learning to predict potential health issues based on patient medical history, current vitals, and other relevant data, enabling proactive medical treatments.",
        "dialog" : []
    },
    "human_input": "",
    "speaker_list": [],
}
res = requests.post(url, data=json.dumps(data))
message = json.loads(res.text)
dialog = [{f"{message['speaker']}": f"{message['contents']}"}]
print(dialog)
while not message["is_finished"]:
	data = {
		"log": {
			"service_name" : "MedBot Analytics",
			"problem": "Ineffective tracking and predictive analysis of patient health, leading to delayed treatments.",
			"service_idea" : "Develop an AI-driven platform that uses machine learning to predict potential health issues based on patient medical history, current vitals, and other relevant data, enabling proactive medical treatments.",
			"dialog" : dialog
		},
		"human_input": "",
		"speaker_list": [],
	}
	res = requests.post(url, data=json.dumps(data))
	message = json.loads(res.text)
	dialog.append({f"{message['speaker']}": f"{message['contents']}"})
	print(dialog)

data = {
		"log": {
			"service_name" : "MedBot Analytics",
			"problem": "Ineffective tracking and predictive analysis of patient health, leading to delayed treatments.",
			"service_idea" : "Develop an AI-driven platform that uses machine learning to predict potential health issues based on patient medical history, current vitals, and other relevant data, enabling proactive medical treatments.",
			"dialog" : dialog
		},
		"human_input": "ok. continue discussion.",
		"speaker_list": [2, 1],
	}
res = requests.post(url, data=json.dumps(data))
message = json.loads(res.text)
dialog.append({f"{message['speaker']}": f"{message['contents']}"})
print(dialog)

while not message["is_finished"]:
	data = {
		"log": {
			"service_name" : "MedBot Analytics",
			"problem": "Ineffective tracking and predictive analysis of patient health, leading to delayed treatments.",
			"service_idea" : "Develop an AI-driven platform that uses machine learning to predict potential health issues based on patient medical history, current vitals, and other relevant data, enabling proactive medical treatments.",
			"dialog" : dialog
		},
		"human_input": "",
		"speaker_list": [],
	}
	res = requests.post(url, data=json.dumps(data))
	message = json.loads(res.text)
	dialog.append({f"{message['speaker']}": f"{message['contents']}"})
	print(dialog)

url = "http://localhost:8010/generate_business_plan/"
data = {
		"log": {
			"service_name" : "MedBot Analytics",
			"problem": "Ineffective tracking and predictive analysis of patient health, leading to delayed treatments.",
			"service_idea" : "Develop an AI-driven platform that uses machine learning to predict potential health issues based on patient medical history, current vitals, and other relevant data, enabling proactive medical treatments.",
			"dialog" : dialog
		}
}
res = requests.post(url, data=json.dumps(data))
bp = json.loads(res.text)
print(bp)




