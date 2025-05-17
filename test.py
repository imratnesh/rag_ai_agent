import requests

# Test Resume Upload
files = {"file": open("resumes/sample_resume.pdf", "rb")}
upload_response = requests.post("http://127.0.0.1:5000/upload", files=files)
print("Upload Response:", upload_response.json())

# Test Chat Query
query_data = {"message": "Find a Python developer with ML skills"}
chat_response = requests.post("http://127.0.0.1:5000/chat", json=query_data)
print("Chat Response:", chat_response.json())
