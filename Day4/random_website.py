# Write a program that choose a random website name from list and open it in your browser 
import random
import webbrowser

websites = [ "https://www.youtube.com", "https://www.stackoverflow.com", "https://www.reddit.com"]

selected_website = random.choice(websites)
webbrowser.open(selected_website)
