# IDS_Final_Project

This is the main codebase for our project. To get started, clone this repo and run the following to install the required packages:

``pip install -r requirements.txt``

To run the app, you can run:

``streamlit run app.py``

## File Structure

- ``app.py``: Main entry point of our web app
- ``pages/``: This directory contains the three primary features that our app will support: ``popularity.py``, ``lyrics.py``, ``audio.py``.
- ``data/``: This directory is an empty directory. Before developing the app on your local machine, please copy the ``SpotGenTrack`` directory of the Spotify dataset to this directory. Because the dataset size is too large, we exclude the dataset when pushing to Git. This will be automatically done by the ``.gitignore`` file.

**Note: Before pushing your code to Git, please save a backup copy before pushing in case something goes wrong with Git.**
