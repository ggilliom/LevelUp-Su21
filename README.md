# LevelUp-Su21

FRONT END:

To run the program, you need only run two things in the terminal:

(This assumes that you've installed Python.)

1) python3 sheetScrape.py
2) python3 sheetSearchGUI.py

(Also, there are a variety of packages that were imported to the program. If the program doesn't run, that means you need to install some/all of the packages that are included at the top of one or both of the python files listed above.)

To navigate to the worksheet library, click start->register, enter a valid username/pwd, and then click Library...

BACK END:

back.py features a variety of functions that are designed to work in tandem with the front end. The various get methods present can be connected to different buttons and features within the GUI set up that allows the data process to flow properly. Sheet information, a list of sorted sheets, list of users, list of all sheets, and other information can be accessed solely by passing in either a username and/or a sheet name. Functions dealing with the internal rating system are also present, where users can apply ratings to different sheets that cause functions to be called to update the backend files that store information on users and sheets created within the application. More is to be done once networking capabilities are created, so much of it are prototype functions to be added on to or edited for the future. Still, their function now is commendable, useful, and relevant to the application.

The backend uses a file system that stores users within their own director and a master list of users exists for keeping track of all users within the application. Within each director for each user, files keeping track of the sheets and their information are stored alongside a master sheet within each of those user directories that keeps track of what sheets have been uploaded by each user.

## Presentation

Our video submission that summarizes our solution can be found [here](https://www.youtube.com/watch?v=VP-lClhMc94&feature=youtu.be&ab_channel=JakeLehner).
