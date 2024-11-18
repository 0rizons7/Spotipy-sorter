# Spotify Playlist Organizer

Organizes tracks from a Spotify playlist into another one, sorting them by artist and album.

*Organise les morceaux d'une playlist Spotify dans une autre, en les triant par artiste et album.*  

---

## Features / Fonctionnalités

- **Fetch tracks from a playlist:** Retrieves all tracks from a specified playlist.
  *Récupère tous les morceaux d'une playlist spécifiée*  

- **Sort by artist and album:** Groups tracks by artist, and further sorts them by album.  
  *Regroupe les morceaux par artiste, puis les trie par album, et les liste par ordre alphabétique.*  

- **Add sorted tracks to another playlist:** Inserts sorted tracks into a target playlist. 
  *Ajoute les morceaux triés dans une playlist cible.*  

---

## Requirements / Pré-requis

1. **Spotify Developer Account:**  
   Create an app on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) to obtain your client ID and secret.  
   *Créez une application sur le [Tableau de bord Spotify Developer](https://developer.spotify.com/dashboard/) pour obtenir votre client ID et votre secret.*  

2. **Python Packages:**  
   Install the following Python packages:
   *Installez les packages Python suivants :*  
   - [spotipy](https://spotipy.readthedocs.io/en/2.19.0/)  
   - [python-dotenv](https://pypi.org/project/python-dotenv/)  

---

## Installation

1. **Clone the repository:**
   ***Clonez le dépôt :***
   ```bash
   git clone https://github.com/your-username/spotify-playlist-organizer.git
   cd spotify-playlist-organizer
   ```  

3. **Install dependencies:**
   ***Installez les dépendances :***
   ```bash
   pip install spotipy python-dotenv
   ```  

5. **Create a `.env` file:**  
   Add your Spotify credentials in a `.env` file at the root:
   *Ajoutez vos identifiants Spotify dans un fichier `.env` à la racine :*  
   ```plaintext
   CLIENT-ID=your-client-id
   CLIENT-SECRET=your-client-secret
   ```  
---

## Usage / Utilisation

1. **Modify playlist IDs:**  
   Replace the `playlist_from` and `playlist_to` variables in the script with your desired Spotify playlist IDs:
   *Remplacez les variables `playlist_from` et `playlist_to` dans le script par les IDs des playlists Spotify souhaitées :*
   ```python
   playlist_from = "source-playlist-id"
   playlist_to = "target-playlist-id"
   ```  
---

## Notes

- Ensure the target playlist (`playlist_to`) is empty to avoid conflicts.  
  *Assurez-vous que la playlist cible (`playlist_to`) est vide pour éviter les conflits.*  

- You need to authenticate with Spotify the first time you run the script. This will open a browser window for login.  
  *Vous devrez vous authentifier auprès de Spotify la première fois que vous exécutez le script. Cela ouvrira une fenêtre de navigateur pour la connexion.*  

---

## Contributions / Contributions

Feel free to contribute by creating issues or submitting pull requests.  
*N'hésitez pas à contribuer en créant des issues ou en soumettant des pull requests.*  
