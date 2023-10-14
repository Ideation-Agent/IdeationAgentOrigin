from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from selenium import webdriver
from linkedin_scraper import Person, actions
from selenium.webdriver.chrome.options import Options
import openai
import json


app = FastAPI()

class LinkedinURL(BaseModel):
    linkedin_url: str

class IdeaSource(BaseModel):
    linkedin_summary: str
    interests: str = None

load_dotenv('.env')
linkedin_email = os.getenv('LINKEDIN_EMAIL')
linkedin_password = os.getenv('LINKEDIN_PASSWORD')
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.get("/")
async def root():
	return { "message" : "Hello World" }

@app.post("/check_bio/")
async def check_bio(linkedin_url: LinkedinURL):
    print(f"linkedin_url: , {linkedin_url.linkedin_url}")
    options = Options()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=options)
    actions.login(driver, linkedin_email, linkedin_password)
    person = Person(linkedin_url.linkedin_url, driver=driver)
    bio = person.about + str(person.experiences) + str(person.educations) + str(person.interests) + str(person.accomplishments)
    return bio

@app.post("/generate_initial_ideas/")
async def generate_initial_ideas(idea_source: IdeaSource):
    user_input = f"linkedin_summary : , {idea_source.linkedin_summary}, interests : , {idea_source.interests}"
    print(user_input)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", 
             "content": """
             You are a world class business idea generator, who can generate the best startup ideas. 
             If the user provide linkedin information and interests, you will try to generate the 5 best startup ideas.
             You should generate service name, define clear problem and solution for each idea.
             Reply only in json with the following format:

            {
                \"ideas\": {
                    \"service_name\":  \"name of service\",
                    \"problem\": \"original and clear problem definition, not phenomenon\",
                    \"solution\": \"solution should be direct and actionable without further planning\",
                },
            }

             """},
            {"role": "user", "content": user_input},
        ]
    )
    ideas_str_str = response["choices"][0]["message"]["content"]
    ideas = json.loads(ideas_str_str)
    return ideas
     
