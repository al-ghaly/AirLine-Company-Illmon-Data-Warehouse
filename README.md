# Airline Company Data Warehouse Project

## Overview
This repository contains all the necessary documentation and code for the Data Warehouse project designed for a major airline company. The project aims to enable the executive management to analyze current business processes and identify new opportunities through a structured Data Warehouse that consolidates data from various sources. This enables efficient analytical reporting and business intelligence for improving service delivery and expanding the company's market reach.

## Project Team
- Mohamed AlGhaly
- Salma Ahmed
- Ahmed Ali

## Project Milestones
- Data Wareouse Model (7 Business Processes Modeled on 2 Deliverables)
- PowerBI Dashboard Build on top of the DWH Model

## Documentation
Detailed project documentation is available in the `AirLine Company DWH Project.pdf`, which outlines the steps taken from business understanding to data analysis and dashboard building.

## Features
The Data Warehouse incorporates several key features:
- **Ticketing Transactions**: Analyzes sales performance, customer booking behaviors, and revenue management.
- **Frequent Flyers**: Tracking flyer behaviors and booking patterns for company's frequent flyers.
- **Customer Care**: Focuses on enhancing customer satisfaction by managing inquiries and feedback.
- **Flights**: Supports performance analysis and operational planning for flight operations.
- **Loyalty Program**: Manages the airline's loyalty program over all partnered companies.
- **Expenses**: Analyzes company's operational Expenses across different business processes.
- **Revenue**: Analyzes company's revenue over time.

## DWH MODEL

### First Delivery

![Model Delivery 1](https://github.com/al-ghaly/AirLine-Company-Illmon-Data-Warehouse/assets/61648960/f97c582a-54f8-47fe-a108-72eb2f9bc128)

### Second Delivery

![Model Delivery 2](https://github.com/al-ghaly/AirLine-Company-Illmon-Data-Warehouse/assets/61648960/90dbca24-d517-4ac3-a18c-27ee3589c342)

### Data Marts (Sample)

#### Reservations

![Reservations](https://github.com/al-ghaly/AirLine-Company-Illmon-Data-Warehouse/assets/61648960/00bc667e-250f-4c1f-996e-022029c127b2)

#### Customer Care

![Customer Care](https://github.com/al-ghaly/AirLine-Company-Illmon-Data-Warehouse/assets/61648960/4115f129-f187-49c0-b89c-14432e0e50f1)

## Installation
To set up the project on your local machine for development and testing purposes, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/al-ghaly/AirLine-Company-Illmon-Data-Warehouse.git
   ```
2. Navigate to the project directory:
   ```bash
   cd AirLine-Company-Illmon-Data-Warehouse
   ```

## Usage
The project uses Oracle DBMS. Ensure you have Oracle installed and configured on your system. Here are the steps to import the project and run it:
1. Execute the SQL scripts found in the `Schema Creation.SQL` to set up the database schema.
2. Use the `Populate.PY` script to generate sample data.
3. Populate the data into your database using the scripts in the `Data Population` folder.
4. Utilize SQL queries or BI tools to analyze the data.



