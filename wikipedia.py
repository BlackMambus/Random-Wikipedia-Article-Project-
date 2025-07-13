import requests
from bs4 import BeautifulSoup
import webbrowser

while True:
    response = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find(class_="firstHeading").text
    print(f"\nRandom Article: {title}")
    choice = input("Do you want to read it? (Y/N): ").lower()
    if choice == "y":
        webbrowser.open(response.url)
        break
    elif choice == "n":
        print("Fetching another article...")
    else:
        print("Invalid input. Exiting.")
        break

