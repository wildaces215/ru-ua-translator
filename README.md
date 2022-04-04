# ru-ua-translator
## Inspiration
Currently at the time of this writing there is a war happening in Ukraine but also online. Cyber Space specficially. While doing research trying to understand both sides, I really haven't found any good tools that enables me to translate text and be able to analyze text of both Ukrainian and Russian in great scale. So I decided to start creating a tool that allows me to translate text of both Ukrainian and Russian. Save it to a database and be able to export for analysis.

## Getting Started 
You must download and install argotranslate which you can find [here](https://github.com/argosopentech/argos-translate).

You must also install the models themselves which are found below:
- [Russian to English](https://argosopentech.nyc3.digitaloceanspaces.com/argospm/translate-ru_en-1_0.argosmodel)
- [Ukrainian to English](https://argosopentech.nyc3.digitaloceanspaces.com/argospm/translate-uk_en-1_4.argosmodel)


## How to Install
`pip install -r requirements.txt`
or 
`pip3 install -r requirements.txt`


##Current Status
Right now the Desktop GUI is being built and its in its first stage. Only translate.py can be used if one wishes to use as a command line program.
