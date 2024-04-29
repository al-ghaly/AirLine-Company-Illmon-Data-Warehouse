import pandas as pd

# Define the table structures
tables = {
    "PassengerDim": [
        {"Column": "PassengerKey", "DataType": "NUMBER(10)", "Indexed": "Yes"},
        {"Column": "PassengerID", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "Name", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "Gender", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "Country", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "Age", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "Region", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "City", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "PostalCode", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "Email", "DataType": "VARCHAR2(250)", "Indexed": "No"}
    ],
    "StatusDim": [
        {"Column": "StutusKey", "DataType": "NUMBER(10)", "Indexed": "Yes"},
        {"Column": "StatusID", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "Name", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "Description", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "UpgradePriority", "DataType": "NUMBER(10)", "Indexed": "No"}
    ],
        "FareBasisDim": [
        {"Column": "FBKey", "DataType": "NUMBER(10)", "Indexed": "Yes"},
        {"Column": "Code", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "Description", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "Conditions", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "Refundable", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "Unrestricted", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "AdvancePurchaseRequirement", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "CancellationPenalty", "DataType": "BINARY_DOUBLE", "Indexed": "No"},
        {"Column": "ChangePenalty", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "DiscountRate", "DataType": "BINARY_DOUBLE", "Indexed": "No"},
        {"Column": "Restrictions", "DataType": "NUMBER(10)", "Indexed": "No"}
    ],
    "ClassDim": [
        {"Column": "ClassKey", "DataType": "NUMBER(10)", "Indexed": "Yes"},
        {"Column": "ClassID", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "ClassPurchased", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "ClassFlown", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "Purchased_Flown", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "ClassChange", "DataType": "VARCHAR2(250)", "Indexed": "No"}
    ],
    "PromotionDim": [
        {"Column": "PromotionKey", "DataType": "NUMBER(10)", "Indexed": "Yes"},
        {"Column": "PromotionID", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "Type", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "StartDate", "DataType": "DATE", "Indexed": "No"},
        {"Column": "EndDate", "DataType": "DATE", "Indexed": "No"},
        {"Column": "Terms", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "amount", "DataType": "NUMBER(10)", "Indexed": "No"}
    ],
    "DateDim": [
        {"Column": "DateKey", "DataType": "NUMBER(10)", "Indexed": "Yes"},
        {"Column": "Date", "DataType": "DATE", "Indexed": "No"},
        {"Column": "Day", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "Weekday", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "Weekend", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "WeekNumber", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "Month", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "Quarter", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "Year", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "FiscalMonth", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "FiscalQuarter", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "FiscalYear", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "Holiday", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "season", "DataType": "VARCHAR2(250)", "Indexed": "No"}
    ],
    "FlightDim": [
        {"Column": "FlightKey", "DataType": "NUMBER(10)", "Indexed": "Yes"},
        {"Column": "duration", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "Distance", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "ScheduledDepartureTime", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "ScheduledArrivalTime", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "ActualArrivalTime", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "ActualDepartureTime", "DataType": "NUMBER(10)", "Indexed": "No"}
    ],
    "PassengerProfileDim": [
        {"Column": "ProfileKey", "DataType": "NUMBER(10)", "Indexed": "Yes"},
        {"Column": "FrequentFLyerTier", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "HomeAirport", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "ClubMembershipStatus", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "LifeTimeMileageTier", "DataType": "VARCHAR2(250)", "Indexed": "No"}
    ],
    "AirportDim": [
        {"Column": "AirportKey", "DataType": "NUMBER(10)", "Indexed": "Yes"},
        {"Column": "AirportID", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "Code", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "Name", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "City", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "State", "DataType": "VARCHAR2(2520)", "Indexed": "No"},
        {"Column": "Country", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "Region", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "TimeZone", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "Lattitude", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "Longitude", "DataType": "NUMBER(10)", "Indexed": "No"}
    ],
    "AircraftDim": [
        {"Column": "AircraftKey", "DataType": "NUMBER(10)", "Indexed": "Yes"},
        {"Column": "AircraftID", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "Type", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "Manufacturer", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "Model", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "Capacity", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "FuelCapacity", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "WingSpan", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "Length", "DataType": "NUMBER(10)", "Indexed": "No"}
    ],
"BookingDim": [
        {"Column": "BookingKey", "DataType": "NUMBER(10)", "Indexed": "Yes"},
        {"Column": "BookingID", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "SeatNumber", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "Gate", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "ConfirmationNumber", "DataType": "NUMBER(10)", "Indexed": "No"}
    ],
    "ChannelDim": [
        {"Column": "ChannelKey", "DataType": "NUMBER(10)", "Indexed": "Yes"},
        {"Column": "ChannelID", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "Name", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "Type", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "Category", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "ContactMethod", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "Accessibility", "DataType": "VARCHAR2(50)", "Indexed": "No"}
    ],
    "EmployeeDim": [
        {"Column": "EmployeeKey", "DataType": "NUMBER(10)", "Indexed": "Yes"},
        {"Column": "EmployeeID", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "Name", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "Gender", "DataType": "VARCHAR2(50)", "Indexed": "No"},
        {"Column": "Country", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "HomeCity", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "Age", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "Region", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "Email", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "Phone", "DataType": "VARCHAR2(200)", "Indexed": "No"},
        {"Column": "HireDate", "DataType": "DATE", "Indexed": "No"},
        {"Column": "Role", "DataType": "VARCHAR2(250)", "Indexed": "No"}
    ],
    "Interaction": [
        {"Column": "InteractionKey", "DataType": "NUMBER(10)", "Indexed": "Yes"},
        {"Column": "InteractionID", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "Severity", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "Type", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "When_", "DataType": "VARCHAR2(250)", "Indexed": "No"},
        {"Column": "Description", "DataType": "NUMBER(10)", "Indexed": "No"}
    ],
    "TimeOfDayDim": [
        {"Column": "TimeKey", "DataType": "NUMBER(10)", "Indexed": "Yes"},
        {"Column": "Time", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "Hour", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "Minute", "DataType": "NUMBER(10)", "Indexed": "No"}
    ], "FlightActivity": [
        {"Column": "BookedSeats", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "PassengersCount", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "EmptySeats", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "FuelConsumption", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "CrewCount", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "SrcAirportKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "DstAirportKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "ScheduledArrDateKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "ActualArrDateKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "ScheduledDepDateKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "ActualDepDateKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "FlightKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "AircraftKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "CaptinKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "CoCaptinKey", "DataType": "NUMBER(10)", "Indexed": "No"}
    ],
    "Reservations": [
        {"Column": "TotalFare", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "ReservationID_#DD", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "AncillaryRevenue", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "GovernmentalTaxes", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "AirportTaxes", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "SecurityFees", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "OtherFees", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "BaggageFees", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "Discount", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "UpgradeFees", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "DepartureDate", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "PassengerKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "ChannelKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "ClassKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "FBKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "SrcAirportKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "DstAirportKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "ProfileKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "DepartureTimeKey", "DataType": "NUMBER(10)", "Indexed": "No"}
    ],
    "FrequentFlyers": [
        {"Column": "PointsRedeemed", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "PointsEarned", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "Cancelled", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "OvernightStand", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "ReservationID_#DD", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "PassengerKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "StatusKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "FBKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "ClassKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "PromotionKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "ReservationDate", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "SrcAirportKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "DstAirportKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "ProfileKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "BookingKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "ChannelKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "FlightKey", "DataType": "NUMBER(10)", "Indexed": "No"}
    ],
    "CustomerCare": [
        {"Column": "RespondeDelay", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "ResolutionDelay", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "Duration", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "ProfileKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "FlightKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "PassengerKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "SubmissionDate", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "ResponseDate", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "ResolutionDate", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "ChannelKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "EmployeeKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "InteractionKey", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "SubmissionTime", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "ResponseTime", "DataType": "NUMBER(10)", "Indexed": "No"},
        {"Column": "ResolutionTime", "DataType": "NUMBER(10)", "Indexed": "No"}
    ]

}

# Convert the table structures to DataFrames
sheets = {table_name: pd.DataFrame(columns_info) for table_name, columns_info in tables.items()}

# Write each DataFrame to a separate sheet in an Excel file
excel_writer = pd.ExcelWriter('DatabaseSchema.xlsx', engine='xlsxwriter')
for sheet_name, df in sheets.items():
    df.to_excel(excel_writer, sheet_name=sheet_name, index=False)

# Save the Excel file
excel_writer.close()
