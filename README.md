# flgaz-python

## Setup and user guide

- `git clone https://github.com/MarcusPlusPlusPlus/flgaz-python.git`
- `cd flgaz-python`
- `pip install -r requirement.txt` (use `sudo` if necessary)
- `flask run`

## Available routes

- [GET] `/` : return a single string _"Bienvenue !"_
    - No payload

---

- [GET] `/gaz` : access to the gazouille form
    - No payload

---

- [POST] `/gaz` : send a gazouille and redirect to the timeline
    - Payload (JSON):
```json
{
    "user-name": "str",
    "user-text": "str"
}
```

---

- [GET] `/timeline` : view all the gazouilles
    - No payload

## How does it work ?

- How do you get the gazouilles ? _You can access all the gazouilles from the timeline.`_
- How does you create a gazouille ? _From a basic html form. A gazouille is made from a username and a block of text._
- How does it stores the gazouilles ? _The gazouilles are stored inside a CSV file. Ths CSV file is updated when a gazouille is created_

## Used tools in this project

Used tools : Python 3.8.0, Flask==1.1.1
Flask is a WSGI lightweight web framework for python.
## Possible improvements

- Check TOP-10 owasp security risks
- Use another way to store gazouilles.
- Use an account to send gazouilles.
- Being able to modify gazouilles our own gazouilles.
- Search for specific gazouilles.
- Send different type of gazouille (text, link, media).
- Comment gazouilles
- Send gazouille to private rooms.
