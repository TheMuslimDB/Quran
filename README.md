# Quran
<center> <img alt="logo" src="site-logo.png"> </center>    


data scraped from [quran.com](https://quran.com/)    
you can find the data in the [data branch](https://github.com/TheMuslimDB/Quran/tree/data).      
you can find the code in the [code branch](https://github.com/TheMuslimDB/Quran/tree/code).      



## Data
**note**: i added the dots to make it more readable :)    

- **surahs_info.json**
    ```json
    {
        "1": {
            "revelationPlace": "makkah",
            "transliteratedName": "Al-Fatihah",
            "versesCount": 7,
            "translatedName": "The Opener",
            "slug": "al-fatihah"
        },
        ...
    }
    ```

- **surahs_detailed_info.json**
    ```json
    {
        "1": {
            "short_description": "This Surah is named Al-Fatihah...",
            "src": "Sayyid Abul...",
            "content": [
                {
                    "title": "Name",
                    "body": [
                        "This Surah is named Al-Fatihah..." 
                    ]
                },
                {
                    "title": "Period of Revelation",
                    "body": [
                        "Surah Al-Fatihah is one of the very earliest Revelations...",
                    ]
                },
                {
                    "title": "Theme",
                    "body": [
                        "This Surah is in fact a prayer that Allah has taught to all those...",
                        "From this theme, it becomes clear..."
                    ]
                }
            ],
        },
        ...
    }
    ```
