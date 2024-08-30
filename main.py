import grequests
import json
from bs4 import BeautifulSoup


def write_json(fn,obj):
    with open(fn,"w") as f:
        json.dump(obj,f)

def read_json(fn):
    data = {}
    with open(fn,"r") as f:
        data = json.loads(f.read())
    return data

# will write to file called, 
# uncleaned surahs info from quran.com 
def scrape_surahs_info():
    4
    LINK_BASE = "https://quran.com/_next/data/g_X2zg8qfotZzHSQ9yuBX/en/surah/"
    urls = [LINK_BASE + str(i) + "/info.json" for i in range(1,114 + 1)]

    reses = [grequests.get(url) for url in urls]
    data = {}
    for idx , res in grequests.imap_enumerated(reses,size=20):
        print(idx,res)
        try:
            data[idx] = res.json()
        except Exception:
            pass
    with open("output/scraped_surahs_info.json","w") as f:
        json.dump(data,f)


# reads surahs_info.json and extracts all surahs general info
def extract_surahs_info():
    data = {}
    with open("output/scraped_surahs_info.json","r") as f:
        data = json.loads(f.read())
    write_json("output/surahs_info.json",data["0"]["pageProps"]["chaptersData"])

# scrape_surahs_info()

def extract_surahs_detailed_info():
    data = {}
    loaded = read_json("output/scraped_surahs_info.json")
    # offseted by one for some reason
    for i in range(0,114):
        chapter_info = loaded[str(i)]["pageProps"]["chapterInfoResponse"]["chapterInfo"]
        short_text =  chapter_info["shortText"]
        source =  chapter_info["source"]

        html_body =  chapter_info["text"]    
        body =  BeautifulSoup(html_body,"lxml")

        content = []
        content_buf = {"title" : "", "body" : []}
        for elem in body.select("html body")[0].children:
            if elem.name == None:
                continue
            if "h" in elem.name:
                if len(content_buf["title"]) != 0 or len(content_buf["body"]) != 0:
                    content.append(content_buf.copy())

                content_buf["title"] = elem.text
                content_buf["body"] = []
            else: 
                content_buf["body"].append(elem.text)
        if len(content_buf["title"]) != 0 or len(content_buf["body"]) != 0:
            content.append(content_buf)


        data[i + 1] = {
            "short_description" : short_text,
            "src" : source,
            "content" : content
        }
    write_json("output/surahs_detailed_info.json",data)

scrape_surahs_info()
extract_surahs_info()
extract_surahs_detailed_info()