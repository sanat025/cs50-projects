1  -- Keep a log of any SQL queries you execute as you solve the mystery.
2
3  SELECT description
4  FROM crime_scene_reports
5  WHERE month = 7
6    AND day = 28
7    AND street = 'Humphrey Street';
8
9  SELECT transcript
10 FROM interviews
11 WHERE year = 2024
12   AND month = 7
13   AND day = 28
14   AND transcript LIKE '%bakery%';
15
16 SELECT bakery_security_logs.activity,
17        bakery_security_logs.license_plate,
18        people.name
19 FROM people
20 JOIN bakery_security_logs
21   ON bakery_security_logs.license_plate = people.license_plate
22 WHERE bakery_security_logs.year = 2024
23   AND bakery_security_logs.month = 7
24   AND bakery_security_logs.day = 28
25   AND bakery_security_logs.hour = 10
26   AND bakery_security_logs.minute >= 15
27   AND bakery_security_logs.minute <= 25;
28
29 SELECT people.name,
30        atm_transactions.transaction_type
31 FROM people
32 JOIN bank_accounts
33   ON bank_accounts.person_id = people.id
34 JOIN atm_transactions
35   ON atm_transactions.account_number = bank_accounts.account_number
36 WHERE atm_transactions.year = 2024
37   AND atm_transactions.month = 7
38   AND atm_transactions.day = 28
39   AND atm_transactions.atm_location = 'Leggett Street'
40   AND atm_transactions.transaction_type = 'withdraw';
41
42 UPDATE phone_calls
43 SET receiver = people.name
44 FROM people
45 WHERE phone_calls.receiver = people.phone_number;
46
47 SELECT caller,
48        receiver
49 FROM phone_calls
50 WHERE year = 2024
51   AND month = 7
52   AND day = 28
53   AND duration < 60;
54
55 SELECT id,
56        hour,
57        minute,
58        origin_airport_id,
59        destination_airport_id
60 FROM flights
