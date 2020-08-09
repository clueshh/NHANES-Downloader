# NHANES-DOWNLOADER

A [Scrapy](https://scrapy.org/) web crawler that parses and downloads all the
[NHANES](https://www.cdc.gov/nchs/nhanes/index.htm) data. 

The .XPT files are downloaded into the directories below with associated metadata stored in a .JSON file.

```
├───Demographics
│   ├───1999-2000
│   ├───...
│   └───2017-2018
├───Dietary
│   ├───1999-2000
│   ├───...
│   └───2017-2018
├───Examination
│   ├───1999-2000
│   ├───...
│   └───2017-2018
├───Laboratory
│   ├───1999-2000
│   ├───...
│   └───2017-2018
├───Non-Public
│   └───limited_access
└───Questionnaire
    ├───1999-2000
    ├───...
    └───2017-2018
```

## Usage

```bash
git clone https://github.com/clueshh/NHANES-Downloader.git
cd NHANES-Downloader
pip install -r requirements.txt
python main.py
```
