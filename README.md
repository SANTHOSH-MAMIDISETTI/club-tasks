# tasks

tasks for club

## OVERVIEW OF TASKS DONE

| TASK NUMBER                                                                  | DESCRIPTION                       |      STATUS      |
| :--------------------------------------------------------------------------- | :-------------------------------- | :--------------: |
| [task-1](https://github.com/SANTHOSH-MAMIDISETTI/club-tasks/tree/main/task-1)   | webscraper                        |   COMPLETED 👍   |
| [task-2](https://github.com/SANTHOSH-MAMIDISETTI/club-tasks/tree/main/task-2)   | captcha automator                 |   COMPLETED 👍   |
| [task-3](https://github.com/SANTHOSH-MAMIDISETTI/club-tasks/tree/main/task-3)   | bandit  OTW                       |   COMPLETED 👍   |
| [task-4](https://github.com/SANTHOSH-MAMIDISETTI/club-tasks/tree/main/task-4)   | Programming                       |   COMPLETED 👍   |
| [task-5](https://github.com/SANTHOSH-MAMIDISETTI/club-tasks/tree/main/task-5)   | Spammer_Spaghetti                 |      trying      |
| [task-6](https://github.com/SANTHOSH-MAMIDISETTI/club-tasks/tree/main/task-6)   | not assigned                      |   not assigned   |
| [task-7](https://github.com/SANTHOSH-MAMIDISETTI/club-tasks/tree/main/task-7)   | not assigned                      |   not assigned   |
| [task-8](https://github.com/SANTHOSH-MAMIDISETTI/club-tasks/tree/main/task-8)   | pokedex                           |   COMPLETED 👍   |
| [task-9](https://github.com/SANTHOSH-MAMIDISETTI/club-tasks/tree/main/task-9)   | login form                        |   COMPLETED 👍   |
| [TASK-10](https://github.com/SANTHOSH-MAMIDISETTI/club-tasks/tree/main/task-10) | send tweet using python           | Techinical issue |
| [TASK-11](https://github.com/SANTHOSH-MAMIDISETTI/club-tasks/tree/main/task-11) | Stone Paper Scissors Telegram Bot |   COMPLETED 👍   |

## task 1

* [ ] A web scraping script was developed to extract data from a website, utilizing the BeautifulSoup, requests, and pandas libraries. The script first used the requests library to send a request to the website to check its status. Then, BeautifulSoup was utilized to scrape the necessary data from the website. Finally, pandas was employed to store the scraped data in a CSV file. The primary challenge faced during the development of this script was identifying the appropriate class and div elements of the targeted table.

## task 2

* [ ] A basic level captcha automation script was developed using the Pytesseract, pillow, and OpenCV libraries. The script takes an input image, converts it into text using the mentioned libraries, and pytesseract library specifically. The primary challenge encountered during the development of this script was determining the optimal combination of psm and oem values for the specific image being used. This script can handle basic level captchas, however, significant improvements would be required to effectively utilize it against more complex captchas.

## task 3

* [ ] I started playing Bandit, a series of Linux-based challenges on the OverTheWire wargames website, designed to teach basic Linux commands and system navigation. In each level, I had to log in using SSH (Secure Shell) protocol, providing the username "banditX" where X is the level number and the password from the previous level as the password.
* [ ] In level 0, I logged in using the username "bandit0" and the password "bandit0".
* [ ] In level 1, I logged in using the username "bandit1" and the password "bandit0", and then using the command cat readme I found the password for the next level in the file "readme" in the home directory.
* [ ] In level 2, I logged in using the username "bandit2" and the password from the previous level, then using the command cat ./-, I found the password for the next level in the file "-" in the home directory.
* [ ] In level 3,  the pasword is in a file whith blanks in the name  hence I did cat "file name with spaces" to read fiile and copy the passowrd.
* [ ] In level 4 , the password is in a hidden file in the inhere directory, hence I used la to list all files including hidden files and then cat .hidden to read the file and copy the password.
* [ ] In level 5, the password is in a file in the inhere directory, but it needs to be human readable, hence I used file ./* to  the type of data in the file and opened that one with ASCII in it.
* [ ] In level 6, the password is in a file in the inhere directory, with many sub directories hence I searched the file with the given parameters by ``find . -type f -readable -size 1033c ! -executable``and found the file and opened it with cat.
* [ ] In level 7, the password is in a file somewhere on the server and just like the previous level  it too had pareamters to search with. ``find / -user bandit7 -group bandit6 -size 33c | grep -w password``  the I cat the destiantion file and copied the password.
* [ ] In level 8, the password is in a large file and agnist the words "millionth" hence I used grep to search for the word and copied the password.    ``cat data.txt | grep millionth``
* [ ] In level 9  , the password is in data.txt but it's an unique value , hence I used   ``cat data.txt | sort | uniq -c -u``
* [ ] In level 10 , the password is in a file with a lot of text and the word "===" is repeated only once hence I used grep to search for the word and copied the password.
  ``strings data.txt | grep ===``
* [ ] In level 11, the password is in a file which as data encoded in base 64 , hence i used ``cat data.txt | base64 --decode`` to decode the data and copied the password.

## task 4

## task 5

## task 6

not assigned

## task 7

not assigned

## task 8

To create a Pokedex website using only HTML, CSS, and JavaScript, deployed on localhost, I  obtained  API key for a Pokedex API, such as the PokeAPI ([https://pokeapi.co/](https://pokeapi.co/)). Next, I would used JavaScript to make API calls to the Pokedex API and retrieve data about Pokemon. I would then used the data from the API to dynamically create HTML elements on my website, such as divs and images, to display information about Pokemon, such as their names, images. I would use CSS to style the website and make it visually appealing. I learnt a lot about Js by doing this task . Just did it in LocalHost. didn't host it.

## task 9

* [ ] As a beginner in web development, this was my first experience working with HTML, CSS, and JavaScript. Although the task did not specifically require the use of JavaScript, I chose to incorporate it in order to gain a better understanding of the basics. Overall, the experience was highly informative and beneficial to my learning progress. Just did it in LocalHost. didn't host it.

# task 10

* [ ] There is an issue with the twitter developer account ; which prevented me from genrating the API token , hence unable to do the task (for now).

# task 11

* [ ] I started by creating a new bot on Telegram by talking to the BotFather and obtained an API key. Then, I installed pyTelegramBotAPI using pip in my computer and imported the necessary libraries including random and telebot. I initialized the bot using the API key obtained by talking to the BotFather and created a dictionary containing the possible choices and their short forms. Then, I created a function to get the result of the game, comparing the user choice and the bot choice. I also created a callback function to handle the user's choice when they press the button. Additionally, I created a function to handle the /play command and generate the inline keyboard with the buttons. After that, I started the polling process to listen for incoming messages. I tested the bot by sending messages and interacting with the inline keyboard. Finally,
