# FireWatch [HackUCI 2019]

![alt text](https://raw.githubusercontent.com/jackkolb/FireWatch/master/static/styles/gallery.jpg "Screenshot of the Fire Watch web app")

With the recent rise of wildfires disrupting wildlife, evacuating thousands of families and impacting many more, our team was inspired to create the next wildfire forecasting tool, FireWatch. Using metrics and predictive analysis, FireWatch displays possible future California wildfires onto a Google Maps API using Machine Learning with our mascot Disel the Dog!

Our process (with 4 team members and 36 hours):

[Data] Extract relevant data (wildfire history, altitude, vegetation, and precipitation patterns) from the CalFire Database and use Python scripts to parse data for model training.

[Backend] Host a Flask server with Python, which takes care of Machine Learning calculations and handling SendGrid email requests.

[Frontend] Create a user-friendly interface using HTML, CSS, and Javascript. We made sure that users who used our service would be able to find information easily and seamlessly all while enjoying a beautiful user experience. We provided a form to allow users to register for email alerts if a high chance of fire is in their area.
    
    
![alt text](https://raw.githubusercontent.com/jackkolb/FireWatch/master/static/styles/result.png "Logo Title Text 1")
