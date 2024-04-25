CREATE TABLE PassengerDim
(
  PassengerKey NUMBER(10) ,
  PassengerID NUMBER(10) ,
  Name VARCHAR2(250) ,
  Gender VARCHAR2(250) ,
  Country VARCHAR2(250) ,
  Age NUMBER(10) ,
  Region VARCHAR2(250) ,
  City VARCHAR2(250) ,
  PostalCode VARCHAR2(250) ,
  Email VARCHAR2(250) ,
  PRIMARY KEY (PassengerKey)
);


CREATE TABLE StatusDim
(
  StutusKey NUMBER(10) ,
  StatusID NUMBER(10) ,
  Name VARCHAR2(250) ,
  Description VARCHAR2(250) ,
  UpgradePriority NUMBER(10) ,
  PRIMARY KEY (StutusKey)
);


CREATE TABLE FareBasisDim
(
  FBKey NUMBER(10) ,
  Code VARCHAR2(250) ,
  Description VARCHAR2(250) ,
  Conditions VARCHAR2(250) ,
  Refundable NUMBER(10) ,
  Unrestricted NUMBER(10) ,
  AdvancePurchaseRequirement NUMBER(10) ,
  CancellationPenalty BINARY_DOUBLE ,
  ChangePenalty NUMBER(10) ,
  DiscountRate BINARY_DOUBLE ,
  Restrictions NUMBER(10) ,
  PRIMARY KEY (FBKey)
);


CREATE TABLE ClassDim
(
  ClassKey NUMBER(10) ,
  ClassID NUMBER(10) ,
  ClassPurchased VARCHAR2(250) ,
  ClassFlown VARCHAR2(250) ,
  Purchased_Flown VARCHAR2(250) ,
  ClassChange VARCHAR2(250) ,
  PRIMARY KEY (ClassKey)
);


CREATE TABLE PromotionDim
(
  PromotionKey NUMBER(10) ,
  PromotionID NUMBER(10) ,
  Type VARCHAR2(250) ,
  StartDate DATE ,
  EndDate DATE ,
  Terms VARCHAR2(250) ,
  amount NUMBER(10) ,
  PRIMARY KEY (PromotionKey)
);


CREATE TABLE DateDim
(
  DateKey NUMBER(10) ,
  "Date" DATE ,
  Day NUMBER(10) ,
  Weekday NUMBER(10) ,
  Weekend NUMBER(10) ,
  WeekNumber NUMBER(10) ,
  Month NUMBER(10) ,
  Quarter NUMBER(10) ,
  Year NUMBER(10) ,
  FiscalMonth NUMBER(10) ,
  FiscalQuarter NUMBER(10) ,
  FiscalYear NUMBER(10) ,
  Holiday NUMBER(10) ,
  season VARCHAR2(250) ,
  PRIMARY KEY (DateKey)
);


CREATE TABLE FlightDim
(
  FlightKey NUMBER(10) ,
  duration NUMBER(10) ,
  Distance NUMBER(10) ,
  ScheduledDepartureTime NUMBER(10) ,
  ScheduledArrivalTime NUMBER(10) ,
  ActualArrivalTime NUMBER(10) ,
  ActualDepartureTime NUMBER(10) ,
  PRIMARY KEY (FlightKey)
);


CREATE TABLE PassengerProfileDim
(
  ProfileKey NUMBER(10) ,
  FrequentFLyerTier VARCHAR2(250) ,
  HomeAirport VARCHAR2(250) ,
  ClubMembershipStatus VARCHAR2(250) ,
  LifeTimeMileageTier VARCHAR2(250) ,
  PRIMARY KEY (ProfileKey)
);


CREATE TABLE AirportDim
(
  AirportKey NUMBER(10) ,
  AirportID NUMBER(10) ,
  Code VARCHAR2(250) ,
  Name VARCHAR2(250) ,
  City VARCHAR2(250) ,
  State VARCHAR2(2520) ,
  Country VARCHAR2(250) ,
  Region VARCHAR2(250) ,
  TimeZone VARCHAR2(250) ,
  Lattitude NUMBER(10) ,
  Longitude NUMBER(10) ,
  PRIMARY KEY (AirportKey)
);


CREATE TABLE AircraftDim
(
  AircraftKey NUMBER(10) ,
  AircraftID NUMBER(10) ,
  Type VARCHAR2(250) ,
  Manufacturer VARCHAR2(250) ,
  Model VARCHAR2(250) ,
  Capacity NUMBER(10) ,
  FuelCapacity NUMBER(10) ,
  WingSpan NUMBER(10) ,
  Length NUMBER(10) ,
  PRIMARY KEY (AircraftKey)
);


CREATE TABLE BookingDim
(
  BookingKey NUMBER(10) ,
  BookingID NUMBER(10) ,
  SeatNumber NUMBER(10) ,
  Gate NUMBER(10) ,
  ConfirmationNumber NUMBER(10) ,
  PRIMARY KEY (BookingKey)
);


CREATE TABLE ChannelDim
(
  ChannelKey NUMBER(10) ,
  ChannelID NUMBER(10) ,
  Name VARCHAR2(250) ,
  Type VARCHAR2(250) ,
  Category VARCHAR2(250) ,
  ContactMethod VARCHAR2(250) ,
  Accessibility VARCHAR2(1) ,
  PRIMARY KEY (ChannelKey)
);


CREATE TABLE EmployeeDim
(
  EmployeeKey NUMBER(10) ,
  EmployeeID NUMBER(10) ,
  Name VARCHAR2(250) ,
  Gender VARCHAR2(50) ,
  Country VARCHAR2(250) ,
  HomeCity VARCHAR2(250) ,
  Age NUMBER(10) ,
  Region VARCHAR2(250) ,
  Email VARCHAR2(250) ,
  Phone VARCHAR2(200) ,
  HireDate DATE ,
  Role VARCHAR2(250) ,
  PRIMARY KEY (EmployeeKey)
);


CREATE TABLE Interaction
(
  InteractionKey NUMBER(10) ,
  InteractionID NUMBER(10) ,
  Severity NUMBER(10) ,
  Type VARCHAR2(250) ,
  When_ VARCHAR2(250) ,
  Description NUMBER(10) ,
  PRIMARY KEY (InteractionKey)
);


CREATE TABLE TimeOfDayDim
(
  TimeKey NUMBER(10) ,
  Time NUMBER(10) ,
  Hour NUMBER(10) ,
  Minute NUMBER(10) ,
  PRIMARY KEY (TimeKey)
);


CREATE TABLE FlightActivity
(
  BookedSeats NUMBER(10) ,
  PassengersCount NUMBER(10) ,
  EmptySeats NUMBER(10) ,
  FuelConsumption NUMBER(10) ,
  CrewCount NUMBER(10) ,
  SrcAirportKey NUMBER(10) ,
  DstAirportKey NUMBER(10) ,
  ScheduledArrDateKey NUMBER(10) ,
  ActualArrDateKey NUMBER(10) ,
  ScheduledDepDateKey NUMBER(10) ,
  ActualDepDateKey NUMBER(10) ,
  FlightKey NUMBER(10) ,
  AircraftKey NUMBER(10) ,
  CaptinKey NUMBER(10) ,
  CoCaptinKey NUMBER(10) ,
  FOREIGN KEY (SrcAirportKey) REFERENCES AirportDim(AirportKey),
  FOREIGN KEY (DstAirportKey) REFERENCES AirportDim(AirportKey),
  FOREIGN KEY (ScheduledArrDateKey) REFERENCES DateDim(DateKey),
  FOREIGN KEY (ActualArrDateKey) REFERENCES DateDim(DateKey),
  FOREIGN KEY (ScheduledDepDateKey) REFERENCES DateDim(DateKey),
  FOREIGN KEY (ActualDepDateKey) REFERENCES DateDim(DateKey),
  FOREIGN KEY (FlightKey) REFERENCES FlightDim(FlightKey),
  FOREIGN KEY (AircraftKey) REFERENCES AircraftDim(AircraftKey),
  FOREIGN KEY (CaptinKey) REFERENCES EmployeeDim(EmployeeKey),
  FOREIGN KEY (CoCaptinKey) REFERENCES EmployeeDim(EmployeeKey)
);


CREATE TABLE Reservations
(
  TotalFare NUMBER(10) ,
  ReservationID_#DD NUMBER(10) ,
  AncillaryRevenue NUMBER(10) ,
  GovernmentalTaxes NUMBER(10) ,
  AirportTaxes NUMBER(10) ,
  SecurityFees NUMBER(10) ,
  OtherFees NUMBER(10) ,
  BaggageFees NUMBER(10) ,
  Discount NUMBER(10) ,
  UpgradeFees NUMBER(10) ,
  DepartureDate NUMBER(10) ,
  PassengerKey NUMBER(10) ,
  ChannelKey NUMBER(10) ,
  ClassKey NUMBER(10) ,
  FBKey NUMBER(10) ,
  SrcAirportKey NUMBER(10) ,
  DstAirportKey NUMBER(10) ,
  ProfileKey NUMBER(10) ,
  DepartureTimeKey NUMBER(10) ,
  FOREIGN KEY (DepartureDate) REFERENCES DateDim(DateKey),
  FOREIGN KEY (PassengerKey) REFERENCES PassengerDim(PassengerKey),
  FOREIGN KEY (ChannelKey) REFERENCES ChannelDim(ChannelKey),
  FOREIGN KEY (ClassKey) REFERENCES ClassDim(ClassKey),
  FOREIGN KEY (FBKey) REFERENCES FareBasisDim(FBKey),
  FOREIGN KEY (SrcAirportKey) REFERENCES AirportDim(AirportKey),
  FOREIGN KEY (DstAirportKey) REFERENCES AirportDim(AirportKey),
  FOREIGN KEY (ProfileKey) REFERENCES PassengerProfileDim(ProfileKey),
  FOREIGN KEY (DepartureTimeKey) REFERENCES TimeOfDayDim(TimeKey)
);


CREATE TABLE FrequentFlyers
(
  PointsRedeemed NUMBER(10) ,
  PointsEarned NUMBER(10) ,
  Cancelled NUMBER(10) ,
  OvernightStand NUMBER(10) ,
  ReservationID_#DD NUMBER(10) ,
  PassengerKey NUMBER(10) ,
  StatusKey NUMBER(10) ,
  FBKey NUMBER(10) ,
  ClassKey NUMBER(10) ,
  PromotionKey NUMBER(10) ,
  ReservationDate NUMBER(10) ,
  SrcAirportKey NUMBER(10) ,
  DstAirportKey NUMBER(10) ,
  ProfileKey NUMBER(10) ,
  BookingKey NUMBER(10) ,
  ChannelKey NUMBER(10) ,
  FlightKey NUMBER(10) ,
  FOREIGN KEY (PassengerKey) REFERENCES PassengerDim(PassengerKey),
  FOREIGN KEY (StatusKey) REFERENCES StatusDim(StutusKey),
  FOREIGN KEY (FBKey) REFERENCES FareBasisDim(FBKey),
  FOREIGN KEY (ClassKey) REFERENCES ClassDim(ClassKey),
  FOREIGN KEY (PromotionKey) REFERENCES PromotionDim(PromotionKey),
  FOREIGN KEY (ReservationDate) REFERENCES DateDim(DateKey),
  FOREIGN KEY (SrcAirportKey) REFERENCES AirportDim(AirportKey),
  FOREIGN KEY (DstAirportKey) REFERENCES AirportDim(AirportKey),
  FOREIGN KEY (ProfileKey) REFERENCES PassengerProfileDim(ProfileKey),
  FOREIGN KEY (BookingKey) REFERENCES BookingDim(BookingKey),
  FOREIGN KEY (ChannelKey) REFERENCES ChannelDim(ChannelKey),
  FOREIGN KEY (FlightKey) REFERENCES FlightDim(FlightKey)
);


CREATE TABLE CustomerCare
(
  RespondeDelay NUMBER(10) ,
  ResolutionDelay NUMBER(10) ,
  Duration NUMBER(10) ,
  ProfileKey NUMBER(10) ,
  FlightKey NUMBER(10) ,
  PassengerKey NUMBER(10) ,
  SubmissionDate NUMBER(10) ,
  ResponseDate NUMBER(10) ,
  ResolutionDate NUMBER(10) ,
  ChannelKey NUMBER(10) ,
  EmployeeKey NUMBER(10) ,
  InteractionKey NUMBER(10) ,
  SubmissionTime NUMBER(10) ,
  ResponseTime NUMBER(10) ,
  ResolutionTime NUMBER(10) ,
  FOREIGN KEY (ProfileKey) REFERENCES PassengerProfileDim(ProfileKey),
  FOREIGN KEY (FlightKey) REFERENCES FlightDim(FlightKey),
  FOREIGN KEY (PassengerKey) REFERENCES PassengerDim(PassengerKey),
  FOREIGN KEY (SubmissionDate) REFERENCES DateDim(DateKey),
  FOREIGN KEY (ResponseDate) REFERENCES DateDim(DateKey),
  FOREIGN KEY (ResolutionDate) REFERENCES DateDim(DateKey),
  FOREIGN KEY (ChannelKey) REFERENCES ChannelDim(ChannelKey),
  FOREIGN KEY (EmployeeKey) REFERENCES EmployeeDim(EmployeeKey),
  FOREIGN KEY (InteractionKey) REFERENCES Interaction(InteractionKey),
  FOREIGN KEY (SubmissionTime) REFERENCES TimeOfDayDim(TimeKey),
  FOREIGN KEY (ResponseTime) REFERENCES TimeOfDayDim(TimeKey),
  FOREIGN KEY (ResolutionTime) REFERENCES TimeOfDayDim(TimeKey)
);