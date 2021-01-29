# Vityasa Intern Hiring

View the API documentation [here](https://documenter.getpostman.com/view/12174054/TW6xnngp)

### Questions

- Write a web application (only API, no UI) in Python 3 that will take n items input and return the following stats about the positive integers in the dataset in JSON format. Eg:

Input:
POST /items
[1, 4, -1, "hello", "world", 0, 10, 7]

Output:
{
"valid_entries": 4,
"invalid_entries": 4,
"min": 1,
"max": 10,
"average": 5.5
}

- Write a web application (only API, no UI) in Python 3 that can be used as a scheduler. The server will maintain fixed slots of 1 hour starting from 12 AM (so, slots would be 0, 1, 2, .. 23 where each number represents the starting hour of the slot) and would accept bookings. Each slot can have maximum 2 bookings. Subsequent requests for the same slot would fail unless a booking is canceled. Implement two endpoints:

POST /booking - Given a name and slot number, save the details if space is available in the slot, else return error.
POST /cancel - Given a name and slot number, delete the booking if available else return error.
GET /booking - Show all bookings
Eg:

Input:
POST /booking
{
"slot": 1, "name": "John"
}
Output:
{
"status": "confirmed"
}

POST /booking
{
"slot": 2, "name": "Jane"
}
Output:
{
"status": "confirmed"
}

POST /booking
{
"slot": 2, "name": "Diana"
}
Output:
{
"status": "confirmed"
}

POST /booking
{
"slot": 2, "name": "Riker"
}
Output:
{
"status": "slot full, unable to save booking for Riker in slot 2"
}

GET /booking
[
{
"slot": 1,
"name": "John"
},
{
"slot": 2,
"name": ["Diana", "Jane"]
}
]

POST /cancel
{
"slot": 2, "name": "Diana"
}
Output:
{
"status": "canceled booking for Diana in slot 2"
}

POST /booking
{
"slot": 2, "name": "Riker"
}
Output:
{
"status": "confirmed booking for Riker in slot 2"
}

POST /cancel
{
"slot": 2, "name": "Diana"
}
Output:
{
"status": "no booking for the name Diana in slot 2"
}

GET /booking
[
{
"slot": 1,
"name": "John"
},
{
"slot": 2,
"name": ["Jane", "Riker"]
}
]

- Write a web application (only API, no UI) in Python 3 with one endpoint that accepts (x, y) coordinate values on a 2D plane.
  The response is a function of the current (x, y) input as well as the previously passed values.

Response:
Iff it's possible to make a square using any of the four points plotted so far, return the 4 points formatted as a string.
Otherwise, the response is just an acknowledgement of the input.
Once a successful response is returned, further calls to the API should just return the same response.

Bounds:

- Assumption 1: All input points can be assumed to lie in the positive quadrant.
- Assumption 2: You only need to consider axes-parallel squares (no tilted squares).

Bonus:
Support anonymous sessions so that it works for simultaneous users (using different clients).

Example request/response:

POST /plot
{
"x": 1, "y": 1
}
Output:
{
"status": "accepted"
}

POST /plot
{
"x": 1, "y": 5
}
Output:
{
"status": "accepted"
}

POST /plot
{
"x": 5, "y": 1
}
Output:
{
"status": "accepted"
}

POST /plot
{
"x": 5, "y": 2
}
Output:
{
"status": "accepted"
}

POST /plot
{
"x": 5, "y": 5
}
Output:
{
"status": "Success (1, 1) (1, 5) (5, 1) (5, 5)"
}
