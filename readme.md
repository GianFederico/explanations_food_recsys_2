# Explanations Food RecSys 2

:warning: This repository contains a newer version of the Explanations service by Matteo Mannavola and Roberta Sallustio. The original work is available in the [Explanations Food Recsys](https://github.com/swapUniba/explanations_food_recsys) repository. Further documentation of this new version is available in [foodWebApp/docs](https://github.com/swapUniba/explanations_food_recsys_2/tree/master/foodWebApp/docs). :warning:

The system consists of the Recommender service, the Explanations service and the web application.

The "foodWebApp" folder contains the Recommender and Explanations services (including a new command-line client for the explanation).<br />
The "foodrecsys2.1" folder contains the "Rec Sys" web application.<br />
The "foodRecExp" folder contains the "Rec Exp" web application.<br />


## Installation

Before starting the services make sure you are using Python 3 and install the flask microframework with the following command

```bash
    pip install flask flask-restful pandas
```

## Recommender Service

To start the Recommender execute the command

```bash
    ./start_server.sh 
```

To stop the Recommender execute the command

```bash
    ./stop_server.sh 
```

For more information on the service, read the repo documentation [FoodRecSys2020](https://github.com/swapUniba/FoodRecSys2020).


## Explanations Service

To start the Explanations service execute the command

```bash
    ./start_expl_server.sh 
```

To stop the Explanations service execute the command

```bash
    ./stop_expl_server.sh 
```

Inside the code, you will notice (in main) some arrays of strings containing the names of the explanation styles.
There are arrays with all the identifying names of the implemented styles, and those used for the current system configuration.
The service runs on port 5003. The service builds a JSON containing the name of the style and its explanation, for each style. The JSON is sent to the web application via the HTTP protocol.


## :warning: Command-line client :warning:

A new feature included in this version of the Explanations service is a command-line client. The server is assumed to be already running.

The client can be used by invoking the `cmd_expl.py` Python script via command line.

See the documentation in [foodWebApp/docs](https://github.com/swapUniba/explanations_food_recsys_2/tree/master/foodWebApp/docs) or use `-h`/`--help` to find information about the expected arguments.


## Web Application "Rec Exp"

The languages used for its development were PHP, HTML5 and CSS.

It is divided into 5 main pages:

    1)index.html, presentation page of the system and its operation;
    2)form.html, page for entering user information, which will be used by the recommender and the explanations service;
    3)recipes.php, page that has the task of creating the user profile by processing the information obtained, requesting the services of the food recommender system and explanations and displaying the results to the user with or without explanation. For a matter of organization and better modularity of the system, an external PHP module has been provided to include and from which to call the more complex functions that perform the tasks just described (/php/requestFunctions.php).
    4)bye.php, page that has the task of storing the results of the experiment in the results log (/results/explResults.csv) and to communicate to the user the conclusion of the experiment without errors.


In this configuration the web app always shows the explanation.
The styles used are those present in the code and are all double level, ie explanations with comparison between two recipes.


## Web Application "Rec Sys"

The "Rec Sys" web application differs from the previous one in that a value is generated randomly for each use (variable ShowExpl in form.php).
This value determines whether the configuration is without explanation, with single level explanation, or with double level explanation.
