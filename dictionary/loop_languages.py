# Create a dictionary of programming languages and their creators
languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C": "Dennis Ritchie",
    "C++": "Bjarne Stroustrup",
    "JavaScript": "Brendan Eich"
}

# Display each key and value using a loop
print("Programming Languages and their Creators:")
for language, creator in languages.items():
    print(f"Language: {language} -> Creator: {creator}")
