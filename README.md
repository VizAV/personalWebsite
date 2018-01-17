# Personal Website
This repository has the source code of my personal landing page. At the moment the code is not hosted anywhere. The html design and the front end code is borrowed from [styleshout.com](http://www.styleshout.com/). The back-end framework is my own work. I referred multiple python tutorials for the same.

# Tech stack
1. Design and frontEnd : styleShout.com
2. Backend RESTAPI: python-flask
3. Email Client: Gmail.com
4. Database : Mongodb
5. Python 3.5
6. Ubuntu Xenial
# Installation
1. Clone the repository into a separate folder in your computer
***
git clone https://github.com/VizAV/personalWebsite.git
***
2. Create a virtual enviornment using virtualenv
***
virtualenv -p python3 env
***
3. Redirect the python
***
source env/bin/activate
***
4. Install all the packages 
***
pip install -r requirements.txt
***
5. Launch the server. In the terminal type:
***
python run.py
***
6. Go to brower and type the following address
***
localhost:8080/
***

Please Note that all the personal information have been commented. Replace them with an equivalent.
# Features
1. Display portfolios
2. Download Resume
3. Links to other social media profiles like facebook, medium, wordpress
4. Feedback message gets saved in our mongodb data
# Project management
Please follow this [link](https://trello.com/b/tGRCVmRd/website-development) for the project tracking
# Licence
This project is licensed under the MIT License - see the LICENSE.md file for details
