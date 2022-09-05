# OAuth2 Test



## Summary

* This is a demo project for OAuth2 Youtube video.
* You can learn about OAuth2 basics by following this tutorial.



## How to Set up

1. Download this project.
   1. Run `git clone https://github.com/insightintosoftware/oauth2_test.git`
   2. Run `cd oauth2_test`
   3. Run `python -m venv .` 
   4. Run `pip install -r requirements.txt`
   5. Run `python app.py`
   6. In your browser, go to `http://localhost:5050`. If you see "OAuth2 Test" page, you are good for now.
2. Go to Google Cloud APIs & Services page(https://console.cloud.google.com/apis/credentials)
   1. Create a new project.
   2. We'll use Google Photos Library for this demo.
      1. In the left navigation, click "Enabled APIs & services".
      2. Click "+ ENABLE APIS AND SERVICES"
      3. Type in "photos library api"
      4. Choose "Photos Library API"
      5. Click "ENABLE"
   3. Let's create OAuth consent screen.
      1. In left navigation, select "OAuth consent screen".
      2. For "User type", select External and click "Create".
      3. In "1 OAuth consent screen" step, put "App name", "User support email", "Developer contact information" and click "SAVE  AND CONTINUE".
      4. In "2 Scopes" step, I added "https://www.googleapis.com/auth/photoslibrary.readonly", which allows you to view your Google Photos library.
      5. In "3 Test users" step, save and continue.
      6. In "4 Summary" step, click "BACK TO DASHBOARD".
      7. You will see "OAuth consent screen" page, click "PUBLISH APP". This will change you app to production mode. If want to keep test mode and test, add Test users. For this demo, we'll just use production mode and ignore Google's app verification process.
   4. Let's create OAuth2 credentials.
      1. In left navigation, select "Credentials"
      2. Click "CREATE CREDENTIALS" and select "OAuth client ID".
      3. For "Application type", select "Web application".
      4. For "Authorized JavaScript origins", add "http://localhost".
      5. For "Authorized redirect URIs", add "http://localhost:5050/callback".
      6. Click "CREATE".
   5. Now you should be able to see "Client ID" and "Client secret" when you select OAuth 2.0 Client ID you just created.
3. Come back to our project and open appsettings.yaml. Replace YOUR_CLIENT_ID and YOUR_CLIENT_SECRET with your Client ID and Client secret.
4. Restart the app.
   1. Run `python app.py`



## OAuth2 Process

1. In the browser, go to `http://localhost:5050/`.
2. Click "Click Me" and that will start OAuth2 process.
3. Choose your Google ID which you want to access photos.
4. Google will show warning page "Google hasn't verified this app". Just click "Advanced" link and proceed with "Go to your app(unsafe)".
5. In Consent screen, you will see "View your Google Photos library." scope. Click "Continue".
6. Now you will see access_token from the screen.



## How to access your Google Photo library album and photo

1. During "OAuth2 Process", our app dumped access token to tokens.yaml file. We'll make use of this token to access Google Photo library.
2. Let's get your album list. In your browser, type in `http://localhost:5050/getalbum`. You will see your Google Photo album. We used access_token from tokens.yaml as a bearer token to get your album information. If see empty result, you should create a new album.
   1. Go to `https://photos.google.com/u/1/albums` and click "Create album"
   2. Add a photo inside the album.
3. Let's display the first photo of your first album. In your browser, type in `http://localhost:5050/getphoto` If the page crashes, follow step 2 and make sure you have an album and a photo inside.

