from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

print(soup.title)
print(soup.title.name)
print(soup.title.string)

# print(soup.prettify())

print(soup.li)
print(soup.find_all(name="li"))
all_li_tags = soup.find_all(name="li")

for tag in all_li_tags:
    print(tag.getText())

all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))


print(soup.find_all(name="h1"))
print(soup.find_all(name="h1", id="my_name"))
# name, id, class_ (because "class" is a python reserved word)
# tag.name, tag.text
# tag.get("attribute") -> gets the value of the attribute

company_url = soup.select_one(selector="p a")  # css selector
print(company_url)
