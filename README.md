# NHANES-DOWNLOADER

A scrapy web crawler that scrapes and downloads all the NHANES data into a directory with the structure.

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

```shell script
git clone 
cd NHANES-Downloader
pip install -r requirements.txt
python main.py
```
