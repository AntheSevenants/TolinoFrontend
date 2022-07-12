# TolinoFrontend
A selfhosted frontend for downloading ebooks on Tolino e-readers

Since [Standaard Boekhandel](https://www.standaardboekhandel.be/) shut down its Tolino integration (and the jerry-rigged [Vivlio Cloud](https://www.standaardboekhandel.be/vivlio-e-readers/cloud) no longer works on device), I decided to build my own frontend for wirelessly transferring ebooks to my Tolino Shine.

<p align="center">
<img src="https://user-images.githubusercontent.com/84721952/178437501-3a5295ed-bfae-4233-b5bf-f61acd63967e.png" width="450px" height="">
</p>

## Key properties and features

* built with Python
* works in the Tolino web browser
* supports adding ebooks straight to your e-reader's library
* pulls ebook metadata straight from the epub file
* no database
* supports basically every e-reader which can download epub files (i.e. Kobo e-readers)

Note that only regular `.epub` files are supported.

This frontend is built for **local use only**. Do not expose it to the internet.

## Running TolinoFrontend from source

0. Clone this repository and `cd` to it
1. `pip install -r requirements.txt`
2. `python3 server.py "path/to/folder/with/ebooks/"`

In your Tolino web browser, navigate to `host-ip:10964/tolino` to access the frontend. You can navigate between books by using the arrow keys in the upper right corner. To download a book, simply tap it and it will be automatically downloaded and added to your library.

## About the frontend

Designing this frontend was fun, but also challenging. My Tolino Shine runs [Android 2.3](https://en.wikipedia.org/wiki/Android_Gingerbread), a mobile operating system which came out in 2010 (!). This means that the web browser included on the device is extremely antiquated and does not support any modern web standards. Therefore, I had to work around some of its limitations to create the lay-out you see in the screenshot above. A special shout-out to [Can I Use](http://caniuse.com/) for showing me just how little the Android 2.3 browser supports!

I built the frontend in just an evening, so there are still some little things which could be improved. Still, my main objective of transferring ebooks wirelessly has been achieved, so I am fine with the state of the project as it is currently. In the future, I would like to package the frontend into a single (Windows) binary so less technically inclined Tolino owners can also use this software.