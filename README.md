# Armstrong Purchase Requisition System

A web-based application for managing purchase requisitions and production orders.

## Overview

This application allows users to:
- Upload purchase requisition files (Excel/CSV)
- Store files in a shared network location
- View and download existing files
- Process purchase requisitions for production orders

## Installation

1. Download files from this repository
2. Run `install_armstrong.bat`
3. If prompted, install Python from Microsoft Store
4. A desktop shortcut will be created

## System Requirements

- Windows 10/11
- Python 3.11 or later (installer will help set this up)
- Network access to O: drive
- No admin rights needed

## File Structure


I need to build a small database that created the purchase requisition for our projects. There are 2 main tables; purchase_req and production_orders. Sometimes there isn't a production order yet

Step 1
I want to build an app which accepts a load of an excel or csv file of a Purchase_Req with the following fields

Item no         - A sequential number starting at 1
Qty		- Quantity of items
Description	- Description of item, can be up to 150 characters
LN Number	- Standard part number if applicable
Length (mm)	- Number with decimal points
Drilling detail	- Text up to 255
Assembly time	- Assembly time
Weight (kg)	- Number with decimal
Comments	- Any other information needed
Comments2	- Any other information needed

When the file is imported the headings and order of columns can be different so the app needs to ask the user which headings are which. Some can be guessed i.e

Item no / Item nr / Item no. / Item number / Item
Qty / Quantity
Description
Length / Length(mm) / Length (mm)
Drilling detail
Assembly time / Assy time
Weight / Weight(Kg)

So that needs to be checked.

Step 2
Also along side this all the Production orders need to be loaded in a table, the format for this is:
Production Start Date	- date (give a blank date if the date is prior to year 1900)
Prod. Order		- format = 552000444
Project			- Format 52P011573 or can be - (if - then use the Item as the Project and Item Description)
Item Description	- Text
Item			- Text
Operation Description	- Text
Order Status		- Short Text ie created, closed, active, cancelled
Requested Delivery Date
Planned Delivery Date
Planned Start Date
Actual Start Date
Completion Date

Step 3
Once all the data is entered the user need to be able to link their purchase req with the right Project item / order:

Project number, must format 52P###### eg 52P011573  - can have many production orders.
Project item, 52P011573-201  - has 1:1 relationship with Production order
Production order, eg 552001319 - has 1:1 relationship with Production item

Lets start with setting up the database and step 1


