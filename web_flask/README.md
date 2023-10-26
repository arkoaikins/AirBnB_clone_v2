# AirBnB clone - Web framework :page_with_curl: 0x04. AirBnB clone - Web framework
## In this project :bulb:
## Overview
- This is the webframe work project for the AirBnB clone
- The web framwork used is Flask
   - Installation of flash `pip3 install flask`
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

### Important resources used

[What is a Web Framework?](https://intranet.alxswe.com/rltoken/64SQpOGx46Ljp0zFJchESg)

[A Minimal Application](https://intranet.alxswe.com/rltoken/NopQlHIr9J_9OPX9XRgfvw)

[Routing](https://intranet.alxswe.com/rltoken/cQiIhbSdIcg1Ao1MICseBg)

[Rendering Templates](https://intranet.alxswe.com/rltoken/DBM65T59nySd0ZRlZZ0CXw)

[Synopsis](https://intranet.alxswe.com/rltoken/5Y_A7XB9Qo1JeZgiSUq0yQ)

[Variables](https://intranet.alxswe.com/rltoken/ITzobwYP1Lc4KqEUUcYCGw)

[Comments](https://intranet.alxswe.com/rltoken/ykUFuQSE9KD1M7WGY-4v4w)

[Whitespace Control](https://intranet.alxswe.com/rltoken/NMLZom50ZVOxQlgYW3rnuQ)

[List of Control Structures (read up to “Call”)](https://intranet.alxswe.com/rltoken/5AGhzIt0zSpPJh9SFysdMQ)

[Flask](https://intranet.alxswe.com/rltoken/VJs151_hsE9g7Cw-Pz5bVg)

[Jinja](https://intranet.alxswe.com/rltoken/2y_hunzGCCvSot06EW67UQ)

[The ultimate flask tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)


### Task 0
Script that Starts a Flask web application

- Root  application is listening on `0.0.0.0`, port `5000`
- Routes:
  - `/`: display "Hello HBNB!"
- option `strict_slashes=False` in route definition

Script is runned

- `python3 -m web_flask.0-hello_route`

In another tab

- curl 0.0.0.0:5000 ; echo "" | cat -e


### Task 1
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
You must use the option strict_slashes=False in your route definition

### Task 2
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
You must use the option strict_slashes=False in your route definition

### Task 3
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
/python/<text>: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
You must use the option strict_slashes=False in your route definition

### Task 4
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
/python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
/number/<n>: display “n is a number” only if n is an integer
You must use the option strict_slashes=False in your route definition

### Task 5
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
/python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
/number/<n>: display “n is a number” only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n” inside the tag BODY
You must use the option strict_slashes=False in your route definition

### Task 6
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
/python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
/number/<n>: display “n is a number” only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n” inside the tag BODY
/number_odd_or_even/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n is even|odd” inside the tag BODY
You must use the option strict_slashes=False in your route definition


