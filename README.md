# UmpAvailability-MS3
Continuation of work on the MS3 to complete

## Introduction/Description
The purpose of this app is allow teams to find available umpires in the area to attend matches The Umpires will be able to browse a list of matches that require an umpire and see the date, time and physical location of the match.

## Project Overview
This app will have a main page which members will be allowed to log in or if they do not have an account will allow both Netball Club representatives and Umpires to create accounts, update passwords and delete accounts. 
A Netball Representative will be able to create a request for a match, the match will have an area, City, Date, Time and exact location within the request. 
An Umpire will be able to view netball matches within an area or location and be able to confirm that they can attend the match. There are assumtions made that the matches will take an hours' slot and that there is a set amount that the umpire will be paid for travelling expenses.

Users will be people from clubs that need to request a match.
Umpires will be umpires looking to find a match.

## User Experience (UX)

### Project Goals
This app that will allow clubs to create a request for an umpire for a match or matches. There will also be an option to cancel the match if there are any issues. This will allow umpires to view any upcoming matches that still require an umpire within the area they are currently in.

### User Stories
1. User Story 
    * As a new club representative I need to be able to create a new login, so I can search for umpires
    * Acceptance Criteria: A new user can create a new login to be able to use the app
2. User Story 
    * As a Club representative looking for an umpire, I need to be able to add a request for an umpire, so that the match can go ahead
    * Acceptance Criteria: A Club representative can request an umpire and receive a confirmation from an umpire to umpire the netball match
3. User Story 
    * As an umpire I need to be able to create a new login, so I can search for matches in my area
    * Acceptance Criteria: A new user can create a new login to be able to use the app
4. User Story 
    * As an Umpire, I need to view matches in my area, so that I can umpire the match.
    * Acceptance Criteria: A match request is visable on the app for me to confirm I am available to umpire
5. User Story
    * As a club user, I want to be able to update my password, to ensure security of my log in to the site
    * Acceptance Criteria: Change Password option is available for me to change my password
6. User Story
    * As an umpire, I want to be able to update my password, to ensure security of my log in to the site
    * Acceptance Criteria: Change Password option is available for me to change my password
7. User Story
    * As a Club user, I want to be able to delete my account, if I leave the club
    * Acceptance Criteria: Ability to delete my user details
8. User Story
    * As an umpire, I want to be able to delete my account, if I am no longer able to umpire
    * Acceptance Criteria: Ability to delete my user details

### Wire Frames
to be added:
ERD - Conceptual, Logical, Physical


### Database Process:

#### Database Structure:
clubmambers
umpires
matches
confirmation

.clubmembers:
enid INT PRIMARY KEY
first_name VARCHAR(50)
surname VARCHAR(50)
club VARCHAR(75)
area VARCHAR(50)
city VARCHAR(50)

.umpires:
enid INT PRIMARY KEY
first_name VARCHAR(50)
surname VARCHAR(50)
award BOOLEAN
area VARCHAR(50)
city VARCHAR(50)

.matches:
date DATE
time TIME
area VARCHAR
city VARCHAR
venue VARCHAR
requesterid INT FOREIGN KEY
hometeam VARCHAR 
cancelled BOOLEAN

.confirmation:
id INT FOREIGN KEY
match_date DATE
match_time TIME
venue VARCHAR(50)
home_team VARCHAR(50)
umpire_id INT
umpire_mame VARCHAR(50)
cancelled
confirmed

### SQL QUERY TO CREATE TABLES:
CREATE TABLE IF NOT EXISTS clubmembers(
	enid INT PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	surname VARCHAR(50) NOT NULL,
	club VARCHAR(75) NOT NULL,
	area VARCHAR(50) NOT NULL,
	city VARCHAR(50) NOT NULL
)

CREATE TABLE if not exists umpires (
	enid INT PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	surname VARCHAR(50) NOT NULL,
	award BOOLEAN NOT NULL,
	area VARCHAR(50) NOT NULL,
	city VARCHAR(50) NOT NULL
)
CREATE TABLE IF NOT EXISTS matches(
	id SERIAL PRIMARY KEY,
	match_date DATE NOT NULL,
	match_time TIME NOT NULL,
	area VARCHAR(50) NOT NULL,
	city VARCHAR(50) NOT NULL,
	venue VARCHAR(150) NOT NULL,
	home_team VARCHAR(50) NOT NULL,
	cancelled BOOLEAN
	)
CREATE TABLE IF NOT EXISTS confirmation(
	id INT FOREIGN KEY,
	match_date DATE NOT NULL,
	match_time TIME NOT NULL,
	venue VARCHAR(50) NOT NULL,
	home_team VARCHAR(50) NOT NULL,
	umpire_id INT NOT NULL,
	umpire_mame VARCHAR(50) NOT NULL,
	cancelled BOOLEAN,
	confirmed BOOLEAN
)

#### Features
- Current Features
    - Create a new user (club representative)
    - Create a new user (umpire)
    - Create a new match request
    - Confirm avilability to umpire the match
    - Delete match request (if cancelled)
- Future Features
    - Send popup message to all umpires in an area when a new match is available

#### Technologies Used
- Visual Studio
- GitHub
- PostgreSQL
- Python

#### Local Developement Set Up
1. MS3 VS set up
    * Logged onto Visual Studio
        * created a new folder MS3_Umpire_Avilability
        * opened the folder in VS
    * logged into GitHub and created a new repository MS3_Umpire_Availability
        * copied the code to set up on vs
    * Navigated back to VS and pasted this into terminal
        * confirmed the readme file is now available in GitHub
    * Visual Studio
        * installed Python
        * Installed Django
        * Installed venv
        * Installed PostgreSQL

#### Live Development

#### Screenshots


### Credits
- ERD diagrams were created using Lucid (https://lucid.app/) 
- postgreSQL 
- Free download of Netball court picture:(https://unsplash.com/photos/a-black-and-white-photo-of-a-basketball-court-IXFZANd1kxk)

