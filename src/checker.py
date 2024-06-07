import os
import requests
import colorama
from colorama import Fore
import time
import threading
from playsound import playsound  # Import playsound module for playing audio

def check_username(username):
    url = f"https://www.chess.com/member/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return f'{Fore.RED}username unavailable'
    elif response.status_code == 404:
        return f'{Fore.GREEN}username available'
    else:
        return f'unable to determine for {username} (status code: {response.status_code})'

# Function to play audio in a separate thread
def play_audio():
    playsound("audio.mp3")

# Read usernames from 'usernames.txt'
with open('usernames.txt', 'r') as file:
    usernames = [line.strip() for line in file.readlines()]

# Initialize variables
available_usernames = []
start_time = time.time()

# Start a new thread to play audio
audio_thread = threading.Thread(target=play_audio)
audio_thread.start()

# Check usernames sequentially
for username in usernames:
    result = check_username(username)
    if 'available' in result:
        available_usernames.append(username)
    print(f"{username}: {result}")

end_time = time.time()

# Calculate the total time taken
total_time = end_time - start_time

# Wait for the audio thread to finish
audio_thread.join()

# Print summary
print("\nChess.com username checker by Austin. V1.2")
print(f"Total available usernames: {len(available_usernames)}")
print(f"Total time taken: {total_time:.2f} seconds")

# Save available usernames to 'available.txt'
with open('available.txt', 'w') as file:
    for username in available_usernames:
        file.write(username + '\n')
