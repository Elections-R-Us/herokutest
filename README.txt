herokutest README
==================
morning-ridge-96369.herokuapp.com

morning-ridge-96369.herokuapp.com/?address=<<your address here>>

I've had inconsistent results with what type of address is
expected. I've tried my house address and a random address I found
online (for Seattle University, for no particular reason). It doesn't
work with some random NYC addresses I tried, or addresses of just
street numbers (e.g., my address with the house number removed). When
the address doesn't work, the server returns a response "bad
address?".


## References etc.
https://www.votinginfoproject.org/about/

https://developers.google.com/civic-information/

https://developers.google.com/civic-information/docs/embed

https://developers.google.com/civic-information/docs/v2/

Check out [default.py](/herokutest/views/default.py) for how the API is
consumed.
