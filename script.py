message = "Hello World!"
print(message)

name = "ada lovelace"
print(name.title())
# the title() method is a string method that changes the first letter of each word to a capital letter.
name = "Ada Lovelace"
print(name.upper())

name = "Ada Lovelace"
print(name.lower())
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")
# the f is a special indicator that tells Python to replace the variables in a string with their values.

print("Python")
print("\tPython")
#   the \t is a tab.
print("Languages:\nPython\nC\nJavaScript")
#   the \n is a new line.
print("Languages:\n\tPython\n\tC\n\tJavaScript")
#   the \n is a new line.
favorite_language = 'python '
favorite_language
favorite_language.rstrip()
favorite_language
#  the rstrip() method removes whitespace from the right side of a string.

nostarch_url = 'http://www.nostarch.com'
nostarch_url.removeprefix('http://')
print(nostarch_url)

simplle_url = nostarch_url.removeprefix('http://')
print(simplle_url)
#  removeprefix() is used to remove certain prefix from the string
