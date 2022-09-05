# oauth2_test



## Summary

* This is a demo project for OAuth2 Youtube video.
* You can learn about OAuth2 basics by following this tutorial.



## Set up instruction

1. Download this project.
2. Go to Google Cloud APIs & Services page(https://console.cloud.google.com/apis/credentials)
   1. Create a project if you don't have a project already.
   2. Select "OAuth consent screen" and create an OAuth consent screen. You will need domain verification process for production usage but it's okay to skip verification for local development.
      1. For "User type", select External.
      2. For "Publishing status", you can either set it as "testing" and select test users, or just set it as "production". You will be asked to submit information for Google to verify app registration. But for local development and testing, you can ignore it.
      3. For "Scopes", I added "https://www.googleapis.com/auth/photoslibrary.readonly" for my demo. If you are unable to navigate and select it, it mean you didn't enable "Photos Library API". Go to "Enabled APIs & services" tab and enable this service.
   3. Select "Credentials"
      1. Click "CREATE CREDENTIALS" and select "OAuth client ID".
      2. For "Application type", select "Web application".
      3. For "Authorized JavaScript origins", add "http://localhost".
      4. For "Authorized redirect URIs", add "http://localhost:5050/callback".
      5. Save
   4. Now you should be able to see "Client ID" and "Client secret" when you select OAuth 2.0 Client ID you just created.

3. In our project, copy over "Client ID" and "Client secret" to appsettings.yaml.
4. Run `python app.py`
5. In the browser, go to `http://localhost:5050/` and follow the steps in the UI.

