# Project Name
UnjobsScraper

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Status](#status)
* [Contact](#contact)

## General info
This is a web crawling program which extracts the useful data from unjobs website and it is saved into a csv file. 

## Technologies
* scrapy - version 1.8.0
* python3 - version 3.6.8

## Setup
To install scrapy use following script in the command line:-

[pip install scrapy]

The latest version of ubuntu has default python3 installion,so you can simply use it.

If you have ubuntu version less than 17.10 then,
To install python3 you can use following script in the command line:-

[sudo apt-get update]
[sudo apt-get install python3.6]

This command runs the program and produces the .csv file:-

[scrapy runspider scraper.py -o result.csv -t csv]

## Status
Project is: _finished_

## Contact
Created by Kushal Dhungana. You can contact me by email(kushal.dhungana@gmail.com)
