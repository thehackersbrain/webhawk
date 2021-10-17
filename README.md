# WebHawk

> Web Recon Framework written in Python3

## Description

![WebHawk Banner Image](https://raw.githubusercontent.com/thehackersbrain/webhawk/main/screenshots/webhawk.png?token=AIY2SQM2ACU5ZBBWXDLXCGDBMIGRG)

<br/>**WebHawk** is a Web Recon framework written in Python3 by Gaurav Raj [TheHackersbrain](https://gauravraj.tech)

Which was originally inspired by **RED_HAWK** tool which is not maintained by now.

## Version

**Webhawk 0.0.8**

## Installation

### Install using Pip3

-   Create a new Python Virtual Environment
    ```bash
    python3 -m venv env
    ```
-   Activate the virtualenv

    ```bash
    source env/bin/activate
    ```

-   Install and Run the tool

    ```bash
    pip3 install webhawk && webhawk -h
    ```

-   Oneliner
    ```bash
    python3 -m venv env && source env/bin/activate && pip3 install webhawk && webhawk -h
    ```

### Run as Python Script

-   Clone this repo

    ```bash
    git clone https://github.com/thehackersbrain/webhawk.git
    ```

-   change the directory

    ```bash
    cd webhawk
    ```

-   Install required modules

    ```bash
    pip3 install -r requirements.txt
    ```

-   Run the `main.py` script
    ```bash
    python main.py -h
    ```

## Uses

-   Basic Scan

    ```bash
    webhawk -d 'gauravraj.tech'
    ```

    ![Basic Scan](https://raw.githubusercontent.com/thehackersbrain/webhawk/main/screenshots/webhawk.png?token=AIY2SQM2ACU5ZBBWXDLXCGDBMIGRG)

-   Subdomain Enumeration

    ```bash
    webhawk -d 'gauravraj.tech' -s
    ```

    ![Subdomain Enumeration](https://raw.githubusercontent.com/thehackersbrain/webhawk/main/screenshots/subdomain.png?token=AIY2SQKNBZVQQ6SC4CPVJSLBMIJS2)

-   Help Menu
    ```bash
    webhawk -h
    ```
    ![Help Menu](https://raw.githubusercontent.com/thehackersbrain/webhawk/main/screenshots/help_menu.png?token=AIY2SQO4TK5QZFOY6E7YSK3BMIJUI)

## About the Author

-   [Portfolio](https://gauravraj.tech/)
-   [Blog](https://blog.gauravraj.tech/)
-   [Github](https://github.com/thehackersbrain)
-   [Twitter](https://twitter.com/thehackersbrain/)
-   [LinkedIn](https://linkedin.com/in/thehackersbrain/)
-   [Instagram](https://www.instagram.com/thehackersbrain/)
-   [More Projects](https://github.com/thehackersbrain?tab=repositories)
