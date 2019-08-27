# Twitter Like Bot

A quick little personal project to learn to use Selenium web driver and automate some browsing activities!

This will log into my Twitter account and search for a specified hash tag. Scroll down the page x amount of times, store all tweets in a list and finally loop through and like each tweet.

## How to use

Make sure you have pipenv and download the repo, open the repo in shell and run:

	pipenv install

Then download your webdriver and place into virtual environment bin:

	downloads: https://github.com/mozilla/geckodriver/releases

Now install Selenium for Python:

	pipenv install selenium

Change line 10 & 11 by either adding your password and username directly or from environment variables.

Change line 46 to = how ever many times you want to scroll down.

Change line 73 inside () to be the hash tag you want to search.

Finally run the file:

	python3 app.py
