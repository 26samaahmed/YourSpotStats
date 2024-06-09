# Top Spotify Stats and Visualization
The command-line application showcases the user's top 10 songs on Spotify and visualizes data such as Beats Per Minute (BPM) and valence through interactive graphs. It also lists the user's top artists. The process begins by requesting user authorization to access their Spotify data, after which the results are displayed.

Tech used: Python, Spotify API, Spotipy Library, Plotext, Pandas

## Requirement
> specify version of python here

To use this project, you'll need to obtain your own Spotify API credentials.

1. **Create a Spotify Developer Account**:
   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) and log in with your Spotify account.
   - If you don't have a Spotify account, create one.

2. **Create a New App**:
   - Click on the "Create an App" button.
   - Fill in the required details such as the App name and description.
   - After submitting, you will get a Client ID and a Client Secret.

3. **Set Up Redirect URI**:
   - In your app settings, set up a redirect URI, for example: `http://localhost:5000/callback`.

4. **Configure the Project**:
   - Create a `.env` file in the project root directory and add your credentials:
     ```dotenv
     SPOTIFY_CLIENT_ID=your_client_id
     SPOTIFY_CLIENT_SECRET=your_client_secret
     SPOTIFY_REDIRECT_URI=http://localhost:8888/callback
     ```

## Guide:
1. Clone the repository<br><br>
```sh
git clone https://github.com/26samaahmed/YourSpotStats
```

2. Navigate to Repository <br><br>
```sh
cd YourSpotStats
```

4. Create a virual environment<br><br>
 ```sh
 command on windows
 ```
 
 ```sh
 command on macos
 ```
6. Activate the virtual environment<br><br>
- Windows
 ```sh
 venv\Scripts\activate
 ```
   
- Mac
 ```sh
 source venv/bin/activate
 ```

8. Install Dependencies<br><br>
 ```sh
pip install -r requirements.txt
```

10. Run Project<br><br>
- Windows
```sh
py -3 main.py
```
- Mac
```sh
python3 main.py
``` 

<img width="771" alt="Screenshot 2024-05-30 at 7 40 47 PM" src="https://github.com/26samaahmed/userSpotStats/assets/111910374/183547dd-44f9-44f7-8fb6-3bb8acb6f6e2"><br>

<img width="771" alt="Screenshot 2024-06-02 at 1 09 32 PM" src="https://github.com/26samaahmed/YourSpotStats/assets/111910374/24a12811-b0f5-4536-b5a2-7df7cbcad9db">

<img width="771" alt="Screenshot 2024-06-02 at 1 10 00 PM" src="https://github.com/26samaahmed/YourSpotStats/assets/111910374/2bf14f60-e331-4d8f-93b6-d65e666cd928">


made with 💚 by sama ahmed
