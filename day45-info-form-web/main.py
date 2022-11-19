from bs4 import BeautifulSoup

with open("website.html",encoding="utf-8") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, "html.parser")


# find_all() can find a lot of same tag  it will show as list

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# for tags in all_anchor_tags:
#     # print(tags.getText())
#     print(tags.get("href"))
    
# heading = soup.find(name="h1", id ="name")
# print(heading)

# section_heading = soup.find(name="h3",class_="heading")
# print(section_heading.getText())

# print(soup.title)
# print(soup.a)

#get anchor tag 
company_url = soup.select_one(selector="p a")
name = soup.select_one(selector="#name")
heading = soup.select(".heading")
print(company_url)