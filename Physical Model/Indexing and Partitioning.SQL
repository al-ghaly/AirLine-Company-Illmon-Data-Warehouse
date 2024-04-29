-- Indexing Fligh activity Fact table
CREATE INDEX idx_flightactivity_src_airport ON FlightActivity(SrcAirportKey);
CREATE INDEX idx_flightactivity_dst_airport ON FlightActivity(DstAirportKey);
CREATE INDEX idx_flightactivity_schedarrdt ON FlightActivity(ScheduledArrDateKey);
CREATE INDEX idx_flightactivity_actualarrdt ON FlightActivity(ActualArrDateKey);
CREATE INDEX idx_flightactivity_scheddepdt ON FlightActivity(ScheduledDepDateKey);
CREATE INDEX idx_flightactivity_actualdepdt ON FlightActivity(ActualDepDateKey);
CREATE INDEX idx_flightactivity_flight ON FlightActivity(FlightKey);
CREATE INDEX idx_flightactivity_aircraft ON FlightActivity(AircraftKey);
CREATE INDEX idx_flightactivity_captain ON FlightActivity(CaptinKey);
CREATE INDEX idx_flightactivity_cocaptain ON FlightActivity(CoCaptinKey);

-- Indexing Reservations Fact Table
CREATE INDEX idx_reservations_departuredt ON Reservations(DepartureDate);
CREATE INDEX idx_reservations_passenger ON Reservations(PassengerKey);
CREATE INDEX idx_reservations_channel ON Reservations(ChannelKey);
CREATE INDEX idx_reservations_class ON Reservations(ClassKey);
CREATE INDEX idx_reservations_fb ON Reservations(FBKey);
CREATE INDEX idx_reservations_src_airport ON Reservations(SrcAirportKey);
CREATE INDEX idx_reservations_dst_airport ON Reservations(DstAirportKey);
CREATE INDEX idx_reservations_profile ON Reservations(ProfileKey);
CREATE INDEX idx_res_departuretime ON Reservations(DepartureTimeKey);

-- Indexing Reservations Fact Table
CREATE INDEX idx_frequentflyers_passenger ON FrequentFlyers(PassengerKey);
CREATE INDEX idx_frequentflyers_status ON FrequentFlyers(StatusKey);
CREATE INDEX idx_frequentflyers_fb ON FrequentFlyers(FBKey);
CREATE INDEX idx_frequentflyers_class ON FrequentFlyers(ClassKey);
CREATE INDEX idx_frequentflyers_promotion ON FrequentFlyers(PromotionKey);
CREATE INDEX idx_frequentflyers_resdt ON FrequentFlyers(ReservationDate);
CREATE INDEX idx_frequentflyers_src_airport ON FrequentFlyers(SrcAirportKey);
CREATE INDEX idx_frequentflyers_dst_airport ON FrequentFlyers(DstAirportKey);
CREATE INDEX idx_frequentflyers_profile ON FrequentFlyers(ProfileKey);
CREATE INDEX idx_frequentflyers_booking ON FrequentFlyers(BookingKey);
CREATE INDEX idx_frequentflyers_channel ON FrequentFlyers(ChannelKey);
CREATE INDEX idx_frequentflyers_flight ON FrequentFlyers(FlightKey);

-- Indexing Customr Care Fact Table
CREATE INDEX idx_customercare_profile ON CustomerCare(ProfileKey);
CREATE INDEX idx_customercare_flight ON CustomerCare(FlightKey);
CREATE INDEX idx_customercare_passenger ON CustomerCare(PassengerKey);
CREATE INDEX idx_customercare_subdt ON CustomerCare(SubmissionDate);
CREATE INDEX idx_customercare_respdt ON CustomerCare(ResponseDate);
CREATE INDEX idx_customercare_reslvdt ON CustomerCare(ResolutionDate);
CREATE INDEX idx_customercare_channel ON CustomerCare(ChannelKey);
CREATE INDEX idx_customercare_employee ON CustomerCare(EmployeeKey);
CREATE INDEX idx_customercare_interaction ON CustomerCare(InteractionKey);
CREATE INDEX idx_customercare_subtime ON CustomerCare(SubmissionTime);
CREATE INDEX idx_customercare_resptime ON CustomerCare(ResponseTime);
CREATE INDEX idx_customercare_reslvtime ON CustomerCare(ResolutionTime);


-- Indexing Dimension Tables
-- PS: Bitmap Imdex is not available on my version of Oracle, so
-- All the create statements provided create a b-tree index


-- Indexes for FareBasisDim Table:

CREATE INDEX idx_farebasis_code ON FareBasisDim(Code);


-- Indexes for ClassDim Table:

CREATE INDEX idx_class_classchange ON ClassDim(ClassChange);
CREATE INDEX idx_class_classpurchased ON ClassDim(ClassPurchased);
CREATE INDEX idx_class_classflown ON ClassDim(ClassFlown);


-- Indexes for PromotionDim Table:

CREATE INDEX idx_promotion_type ON PromotionDim(Type);
CREATE INDEX idx_promotion_startdate ON PromotionDim(StartDate);
CREATE INDEX idx_promotion_enddate ON PromotionDim(EndDate);


-- Indexes for BookingDim Table:

CREATE INDEX idx_booking_bookingid ON BookingDim(BookingID);


-- Indexes for AirportDim Table:

CREATE INDEX idx_airport_name ON AirportDim(Name);
CREATE INDEX idx_airport_city ON AirportDim(City);
CREATE INDEX idx_airport_country ON AirportDim(Country);
CREATE INDEX idx_airport_region ON AirportDim(Region);


-- Indexes for EmployeeDim Table:

CREATE INDEX idx_employee_gender ON EmployeeDim(Gender);
CREATE INDEX idx_employee_role ON EmployeeDim(Role);


-- Indexes for DateDim Table:

CREATE INDEX idx_datedim_date ON DateDim("Date");
CREATE INDEX idx_datedim_day ON DateDim(Day);
CREATE INDEX idx_datedim_month ON DateDim(Month);
CREATE INDEX idx_datedim_year ON DateDim(Year);
CREATE INDEX idx_datedim_quarter ON DateDim(Quarter);
CREATE INDEX idx_datedim_season ON DateDim(Season);


-- Indexes for PassengerDim Table:

CREATE INDEX idx_passenger_gender ON PassengerDim(Gender);
CREATE INDEX idx_passenger_country ON PassengerDim(Country);
CREATE INDEX idx_passenger_region ON PassengerDim(Region);
CREATE INDEX idx_passenger_city ON PassengerDim(City);


-- Indexes for Status Table:

CREATE INDEX idx_status_name ON StatusDim(Name);


-- Indexes for ChannelDim Table:

CREATE INDEX idx_channel_name ON ChannelDim(Name);
CREATE INDEX idx_channel_type ON ChannelDim(Type);
CREATE INDEX idx_channel_category ON ChannelDim(Category);


-- Indexes for TimeOfDayDim Table:

CREATE INDEX idx_timeofday_time ON TimeOfDayDim(Time);
CREATE INDEX idx_timeofday_hour ON TimeOfDayDim(Hour);
CREATE INDEX idx_timeofday_minute ON TimeOfDayDim(Minute);


-- Indexes for Interaction Table:

CREATE INDEX idx_interaction_type ON Interaction(Type);
CREATE INDEX idx_interaction_when ON Interaction(When_);


-- Indexes for AircraftDim Table:

CREATE INDEX idx_aircraft_type ON AircraftDim(Type);

-- Indexes for PassengerProfile Table:

CREATE INDEX idx_passengerprofile_ff ON PassengerProfileDim(FrequentFlyerTier);
CREATE INDEX idx_passengerprofile_ha ON PassengerProfileDim(HomeAirport);
CREATE INDEX idx_passengerprofile_cm ON PassengerProfileDim(ClubMembershipStatus);
CREATE INDEX idx_passengerprofile_lmTier ON PassengerProfileDim(LifeTimeMileageTier);


--------------------------------------------------------------------------
-- Tables Partitioning
/* Table partitioning is not available for standard (non-enterprise) 
Oracle Edition so the following statement are not implemented.
*/
-------------------------------------------------------------
CREATE TABLE FlightActivity
(
  BookedSeats NUMBER(10),
  PassengersCount NUMBER(10),
  EmptySeats NUMBER(10),
  FuelConsumption NUMBER(10),
  CrewCount NUMBER(10),
  SrcAirportKey NUMBER(10),
  DstAirportKey NUMBER(10),
  ScheduledArrDateKey NUMBER(10),
  ActualArrDateKey NUMBER(10),
  ScheduledDepDateKey NUMBER(10),
  ActualDepDateKey NUMBER(10),
  FlightKey NUMBER(10),
  AircraftKey NUMBER(10),
  CaptinKey NUMBER(10),
  CoCaptinKey NUMBER(10),
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
)
PARTITION BY RANGE (ScheduledArrDateKey) 
(
  PARTITION fa_before_2022 VALUES LESS THAN (20220101),
  PARTITION fa_2022 VALUES LESS THAN (20230101),
  PARTITION fa_2023 VALUES LESS THAN (20240101),
  PARTITION fa_2024 VALUES LESS THAN (20250101),
  PARTITION fa_after_2024 VALUES LESS THAN (MAXVALUE)
);


CREATE TABLE Reservations
(
  TotalFare NUMBER(10),
  ReservationID_#DD NUMBER(10),
  AncillaryRevenue NUMBER(10),
  GovernmentalTaxes NUMBER(10),
  AirportTaxes NUMBER(10),
  SecurityFees NUMBER(10),
  OtherFees NUMBER(10),
  BaggageFees NUMBER(10),
  Discount NUMBER(10),
  UpgradeFees NUMBER(10),
  DepartureDate NUMBER(10),
  PassengerKey NUMBER(10),
  ChannelKey NUMBER(10),
  ClassKey NUMBER(10),
  FBKey NUMBER(10),
  SrcAirportKey NUMBER(10),
  DstAirportKey NUMBER(10),
  ProfileKey NUMBER(10),
  DepartureTimeKey NUMBER(10),
  FOREIGN KEY (DepartureDate) REFERENCES DateDim(DateKey),
  FOREIGN KEY (PassengerKey) REFERENCES PassengerDim(PassengerKey),
  FOREIGN KEY (ChannelKey) REFERENCES ChannelDim(ChannelKey),
  FOREIGN KEY (ClassKey) REFERENCES ClassDim(ClassKey),
  FOREIGN KEY (FBKey) REFERENCES FareBasisDim(FBKey),
  FOREIGN KEY (SrcAirportKey) REFERENCES AirportDim(AirportKey),
  FOREIGN KEY (DstAirportKey) REFERENCES AirportDim(AirportKey),
  FOREIGN KEY (ProfileKey) REFERENCES PassengerProfileDim(ProfileKey),
  FOREIGN KEY (DepartureTimeKey) REFERENCES TimeOfDayDim(TimeKey)
)
PARTITION BY RANGE (DepartureDate)
(
  PARTITION r_before_2022 VALUES LESS THAN (20220101),
  PARTITION r_2022 VALUES LESS THAN (20230101),
  PARTITION r_2023 VALUES LESS THAN (20240101),
  PARTITION r_2024 VALUES LESS THAN (20250101),
  PARTITION r_after_2024 VALUES LESS THAN (MAXVALUE)
);


CREATE TABLE FrequentFlyers
(
  PointsRedeemed NUMBER(10),
  PointsEarned NUMBER(10),
  Cancelled NUMBER(10),
  OvernightStand NUMBER(10),
  ReservationID_#DD NUMBER(10),
  PassengerKey NUMBER(10),
  StatusKey NUMBER(10),
  FBKey NUMBER(10),
  ClassKey NUMBER(10),
  PromotionKey NUMBER(10),
  ReservationDate NUMBER(10),
  SrcAirportKey NUMBER(10),
  DstAirportKey NUMBER(10),
  ProfileKey NUMBER(10),
  BookingKey NUMBER(10),
  ChannelKey NUMBER(10),
  FlightKey NUMBER(10),
  FOREIGN KEY (PassengerKey) REFERENCES PassengerDim(PassengerKey),
  FOREIGN KEY (StatusKey) REFERENCES StatusDim(StatusKey),
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
)
PARTITION BY RANGE (ReservationDate)
(
  PARTITION ff_before_2022 VALUES LESS THAN (20220101),
  PARTITION ff_2022 VALUES LESS THAN (20230101),
  PARTITION ff_2023 VALUES LESS THAN (20240101),
  PARTITION ff_2024 VALUES LESS THAN (20250101),
  PARTITION ff_after_2024 VALUES LESS THAN (MAXVALUE)
);


CREATE TABLE CustomerCare
(
  RespondeDelay NUMBER(10),
  ResolutionDelay NUMBER(10),
  Duration NUMBER(10),
  ProfileKey NUMBER(10),
  FlightKey NUMBER(10),
  PassengerKey NUMBER(10),
  SubmissionDate NUMBER(10),
  ResponseDate NUMBER(10),
  ResolutionDate NUMBER(10),
  ChannelKey NUMBER(10),
  EmployeeKey NUMBER(10),
  InteractionKey NUMBER(10),
  SubmissionTime NUMBER(10),
  ResponseTime NUMBER(10),
  ResolutionTime NUMBER(10),
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
)
PARTITION BY RANGE (SubmissionDate)
(
  PARTITION cc_before_2022 VALUES LESS THAN (20220101),
  PARTITION cc_2022 VALUES LESS THAN (20230101),
  PARTITION cc_2023 VALUES LESS THAN (20240101),
  PARTITION cc_2024 VALUES LESS THAN (20250101),
  PARTITION cc_after_2024 VALUES LESS THAN (MAXVALUE)
);
