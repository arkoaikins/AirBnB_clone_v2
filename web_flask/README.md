# AirBnB clone - Web framework :page_with_curl: 0x04. AirBnB clone - Web framework
## In this project :bulb:
## Overview
- This is the webframe work project for the AirBnB clone
- The web framwork used is Flask
   - Installation of flash `pip3 install Flask`
- I covered concepts such as
  - Routes
  - Template
  - How to handle variables in Route
  - How to create HTML response in falsk by using a template
  - How to create a dynamic template(loops,condition..)
  - How to display in HTML data from a MySQL database
 
## Requirements of the project
- Used Vi/Vim editor
### Python Scripts
- files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- Code uses PEP 8 style(version 1.7)
- all modules have documention`(python3 -c 'print(__import__("my_module").__doc__)')`
- all classes have documention ` (python3 -c 'print(__import__("my_module").MyClass.__doc__)')`
- all functions(inside and outside a class) have documentation `python3 -c 'print(__import__("my_module").my_function.__doc__)'`
amd `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')`

###  HTML/CSS Files
- Codes are W3C compliant and validate with `W3C validator`(except for jinja templates)
- All CSS files are in the `styles` folder
- All images are in the `images` folder
- Did not use `!important` or `id`(`#...` in the CSS file)
- All tages are in uppercase
- The screenshots have been done on `Chrome 56.0.2924.87`
- No cross browsers

### Task 0
Script that Starts a Flask web application
- Root we application is listening on `0.0.0.0`, port `5000`
- Routes:
  - `/`: display "Hello HBNB!"
- option `strict_slashes=False` in route definition
Script is runned
- `python3 -m web_flask.0-hello_route`
