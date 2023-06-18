# 1. NLP Evaluation Task ***(Ilyas ADEN)***:
## **Objectif:** creating a PII (Personal identification information) detection and anonymisation proof of concept using different MRT (Masking Redaction Techniques).
### **mymrtool** is proof of concept created in oder to detect and anonymise PII in a given text file document.

This python script will allow you to identify at the first glance following PII in the data then anonynised by redaction.
-	UK social security number (e.g. "AB 123456 )
-	UK phone numbers (e.g. "+447789654411" or "07444467712")
-	UK postcodes (e.g. "RG2 BA5" or "RG25BA")
-	email address (e.g. "abc_def@google.com")

**Output:** Application will allow you to upload a text file then return anonymised text file.

# 2. Deployment in 10 steps to Heroku platform
- 1. Install the Heroku CLI if you haven't already.
- 2. Create a Heroku account if you haven't already.
- 3. Navigate to the directory where your app is located (the directory should contain app.py, requirements.txt, and Procfile).
- 4. Run heroku login to log in to your Heroku account.
- 5. Run heroku create to create a new app on Heroku. Heroku will generate a random name for your app.
- 6. Run *git init* to initialize a git repository in your project directory.
- 7. Run heroku *git:remote -a app.py* to set the remote for Heroku (replace mymrtool with the name generated by Heroku).
- 8. Run *git add .* to add all the files to the git repository.
- 9. Run *git commit -m "Initial commit"* to commit the files.
- 10. Run *git push heroku master* to push your code to Heroku.
 
**Once the push is complete, your app should be deployed! You can visit the URL provided by Heroku in your web browser to see your app live.
If you encounter any issues during deployment, make sure to check the logs for any errors or missing dependencies. You can view the logs by running heroku logs --tail.
