# Lecture 9 & 10: Build an App

## Web Application Architecture
- recap on what's behind www.google.com
- ![](https://www.velvetech.com/wp-content/uploads/2021/07/web-architecture-diagram.jpg)
- who will be building what? Roles in tech companies
  - Front-end engineer
  - Back-end engineer
  - Full-stack engineer
  - UI/UX designer
  - Product manager
  - Machine learning engineer
  - Data scientist
  - Data analyst
- Choose of tech stack
  - language: python (java/scala/R/go/...)
  - communication protocol: http
  - web framework: flask (django/tornado/flastapi/...)
  - API design: REST (grpc/graphql/...)
  - host: your laptop (for now)
      
## Introduction to `Flask`
- set up a simple [flask service](https://flask.palletsprojects.com/en/2.0.x/)
  - `conda create -n lecture_9 python=3.10 -y`
  - create a simple flask app
    - `FLASK_ENV=development FLASK_APP=app/step1.py flask run`
    - `FLASK_ENV=development` is helpful for debugging w/o restarting the service, but only use for debug
    - `FLASK_APP` is a macro variable to define the app entry point
    - `<p>Hello, World!</p>` is [HTML syntax](https://www.w3schools.com/html/html5_syntax.asp)
      - we won't cover this part too much as this will usually be handled by front-end
  - another way to trigger flask app:
    - `FLASK_ENV=development python app/step2.py`
    - debug mode is still valid
    - more customizable
      - `create_app` can do more things, such as loading models, loading data, which is global
      - you can specify your own port other than `5000`
  - other useful concept  
    - see `step3.py`
    - Routing
    - Variables
    - [HTTP methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
    - `json` response
    - request body  
    - play around with [curl](https://www.keycdn.com/support/popular-curl-examples): `curl -X POST localhost:5000/login`
- Unit test
  - how to unit test endpoint
    - okay way -- you can just test the function itself, but this is not native!
    - checkout `pytest tests/test_endpoint_1.py`
- Loading data/model
  - where to load the model
  - global variable in Flask
  - `step4.py`
  - be careful of modifying global variable as raise condition can happen!
- error handling
  - [http status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
  - `step5.py`
  - check network status
  - bad status != failure, so use it carefully
- blueprint
  - how do you organize when you have 1000 endpoint methods?
    - you might want to create multiple files
    - this will cause circular dependency
      - main file (where `app` is defined) need to import other files
      - the other files need to import the main file
    - solution -- blueprint
  - `step6.py`
- documentation
  - problems you will face
    - how do you want everyone to know what endpoint can you provide?
    - how to keep documentation alive?
    - how to do schema checks?
  - one solution: [flasgger](https://github.com/flasgger/flasgger)
  - `step7.py`
    - go to http://localhost:5000/apidocs/
  - schema checks
    - `jsonschema`, so documentation, schema definition, schema check, all in one place!


## Let's build a real app!
- simple requirement
  - a trained model
      - productionalize model training
      - load data, save model
      - how to use `click` to solve input param issue
  - a serivce
    - how to load model
    - how to load data
  - a predict method
    - how to add validation? (open-ended topic)
- getting fancier
  - adding a database (no code)
  

## Additional topic (If time allows...)
- how to productionize model training (white-boarding)
- how to do model promotion
- parallel programming or multi threading
- solidity/python/blockchain