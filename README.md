# Medium Highlights to Pdf

Create pdf documents from your highlights of medium articles.

![alt text](https://github.com/fileames/Medium-Highlights-to-Pdf/blob/master/img/image.PNG?raw=true)

## Dependencies

-[BeautifulSoup](https://pypi.org/project/beautifulsoup4/) 
-[selenium](https://pypi.org/project/selenium/) 
-[reportlab](https://pypi.org/project/reportlab/)


## Usage

Create a txt file using medium article urls line by line.
Give it as a command line argument.

```bash
python medium.py myfile.txt
```

This project uses Chrome drivers but it can be updated to other [drivers](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/).

To access the highlights login to your medium account and press any key on the terminal for:
```bash
Logged in?
```

Then medium pages will open. Since Selenium doesn't wait for highlights to appear, everytime article opens check if it is fully loaded, then press any key:
```bash
Is the loading complete?
```
Your pdf will be created with the name "medium_highlights.pdf".


## Contributing
Pull requests are welcome. 

