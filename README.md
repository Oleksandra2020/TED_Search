# Ukrainian TED search engine
### *Description*

This project is about searching for TED conferences in Ukrainian. It uses linked list data structure as well as Flask framework. It is already [here](tedsearch.pythonanywhere.com), so feel free to try it out!

### *Table of contents*

[Homework0 part1](https://github.com/Oleksandra2020/Final_project/wiki/12-питань)

[Homework0 part2](https://github.com/Oleksandra2020/Final_project/wiki/Зареферовані-дописи)

[Homework1](https://github.com/Oleksandra2020/Final_project/wiki/Опис-проблеми,-або-Домашнє-завдання-№1)

[Homework2](https://github.com/Oleksandra2020/Final_project/wiki/Система,-дані,-бібліотеки,-або-Домашнє-завдання-№2)

### *Installation*

You do not need to install anyhting. I allocated this project on pythonanywhere.com,
so the url will be added later. However, if you want to run it locally, you will need to install these libraries:

- flask
- pandas

### *Usage*

[TED search](tedsearch.pythonanywhere.com)

Example of usage:

First, choose a topic you want to find

![](screens/img1.png)

Here you are! You can watch the video directly on the site or watch it on ted.com (the link is after the title). At the bottom, you can find a short description of a conference. Beside, you can find youtube hyperlinks to the videos on similar topic.

![](screens/img2.png)

You can always return to the initial page by clicking the button in the top left corner.

Keep in mind that the talks are up to 2017. 
Also, you will have a chance to make another input if there are no talks found or you have made a mistake entering the previous one.

![](screens/img3.png)

### *Current version of repository includes:*

- examples folder: 
    - an example of using youtube-transcripts-api 
    - json file the module in the folder returns
- modules folder:
    - csv_reader.py: processes csv data necessary for the research
    - data_collector.py: retrieves data from api and saves it in json-format in data folder
    - flask_app.py
    - node_.py: representation of linked list
    - normalizer.py: removes stop words and stems the given words
    - templates folder
- example_data: a few examples of processed data that I will use for further research
- docs

### *Credits*

Oleksandra Hutor :butterfly: