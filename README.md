# What is MyRLCounter?

Need your Rocket League matches data in real time?

**MyRLCounter** is a python framework forked from **"autoCounterWinnerOrLose"**
This fork has the objective of transforming the original script into an **easy-to-use framework**

But what is the original **"autoCounterWinnerOrLose"**?
The original "autoCounterWinnerOrLose" is a python script made by dhunted
The script has the objective of retrieving your current Rocket League match data in real time

# Installation

## Requirements:
- Python3

## Prepare the packages
1. Go to your MyRLCounter folder
2. Run the requirements file

**Windows/MacOS:**
```pip3 install -r requirements.txt```

**Linux:**
```python3 -m venv MyRLCounter```
```./MyRLCounter/bin/pip3 install -r requirements.txt```

And done, the installation is now complete

# How to run?
1. Open the ``RLCounter.py`` on your text editor / IDE
2. Change the variables ``api_key``, ``username`` and ``platform``, inside there's the information of what you should write there
3. Save the file
4. Run your script

**Windows/MacOS:**
```python3 <yourFileName>.py```

**Linux:**
```./MyRLCounter/bin/python3 <yourFileName>.py``

If you don't have yet a script, run the ``cmdExample.py`` that comes with the MyRLCounter ZIP file

# How do I make a script with MyRLCounter?

There's an example on the file ``cmdExample.py`` with all the possible commands

Don't forget to import the ``RLCounter`` on your script right at the start!
```import RLCounter as rlc```
