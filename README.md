6 WEEKS( June -15 to July 30) Executive Summary This report provides details of the Industrial Internship provided by upskill Campus and The IoT Academy in collaboration with Industrial Partner UniConverge Technologies Pvt Ltd (UCT). This internship was focused on a project/problem statement provided by UCT. We had to finish the project including the report in 6 weeks’ time. My project was (Tell about ur Project) This internship gave me a very good opportunity to get exposure to Industrial problems and design/implement solution for that. It was an overall great experience to have this internship.

Preface Summary of the whole 6 weeks’ work. About need of relevant Internship in career development. Brief about Your project/problem statement. Opportunity given by USC/UCT. How Program was planned
Your Learnings and overall experience. Thank to all (with names), who have helped you directly or indirectly. Your message to your juniors and peers. 

2. Introduction 2.1 About UniConverge Technologies Pvt Ltd A company established in 2013 and working in Digital Transformation domain and providing Industrial solutions with prime focus on sustainability and RoI. For developing its products and solutions it is leveraging various Cutting Edge Technologies e.g. Internet of Things (IoT), Cyber Security, Cloud computing (AWS, Azure), Machine Learning, Communication Technologies (4G/5G/LoRaWAN), Java Full Stack, Python, Front end etc.

i. UCT IoT Platform ( ) UCT Insight is an IOT platform designed for quick deployment of IOT applications on the same time providing valuable “insight” for your process/business. It has been built in Java for backend and ReactJS for Front end. It has support for MySQL and various NoSql Databases. • It enables device connectivity via industry standard IoT protocols - MQTT, CoAP, HTTP, Modbus TCP, OPC UA • It supports both cloud and on-premises deployments. It has features to • Build Your own dashboard • Analytics and Reporting • Alert and Notification • Integration with third party application(Power BI, SAP, ERP) • Rule Engine ii. Smart Factory Platform ( ) Factory watch is a platform for smart factory needs. It provides Users/ Factory • with a scalable solution for their Production and asset monitoring • OEE and predictive maintenance solution scaling up to digital twin for your assets. • to unleased the true potential of the data that their machines are generating and helps to identify the KPIs and also improve them. • A modular architecture that allows users to choose the service that they what to start and then can scale to more complex solutions as per their demands. Its unique SaaS model helps users to save time, cost and money.

(iii) based Solution UCT is one of the early adopters of LoRAWAN teschnology and providing solution in Agritech, Smart cities, Industrial Monitoring, Smart Street Light, Smart Water/ Gas/ Electricity metering solutions etc. iii. Predictive Maintenance UCT is providing Industrial Machine health monitoring and Predictive maintenance solution leveraging Embedded system, Industrial IoT and Machine Learning Technologies by finding Remaining useful life time of various Machines used in production process.

2.2 About upskill Campus (USC) upskill Campus along with The IoT Academy and in association with Uniconverge technologies has facilitated the smooth execution of the complete internship process. USC is a career development platform that delivers personalized executive coaching in a more affordable, scalable, and measurable way. 1 The IoT Academy The IoT academy is the EdTech Division of UCT that is running long executive certification programs in collaboration with EICT Academy, IITK, IITR, and IITG in multiple domains.

2.3 Objectives of this Internship Program

The objective of this internship program was to ☛ get practical experience working in the industry. ☛ to solve real-world problems. ☛ to have improved job prospects. ☛ to have an Improved understanding of our field and its applications. ☛ to have Personal growth like better communication and problem-solving.

2.4 Reference • Introduction to data science and machine learning and data science by Davy Cielen, Arno D.B. Meysman, Mohamed Ali. • An introduction to probability and statistics by Vijay K. Rohatgi and A.K.Md. Ehsanes Saleh. • Introduction to Machine Learning by Alex Smola and S.V.N. Viswanathan

2.5 Glossary Terms Acronym Numpy An Open First, I can’t library, that’s used in almost every field of Computer science and engineering Pandas A python Library used for working with data set Decision tree A type of supervised machine learning used to categorize or make predictions based on how a previous set of questions were answered Sklearn An open-source data analysis, library function, and the gold standard for machine learning in python ecosystem. Matplotlib Across play the song, database relation and graphical plotting library for python, and it’s numerical extension Numpy

Problem Statement:URL SHORTENER
Description: The Url shortener shortens the lengthy URLs into smaller and simpler ones!!

URL Shortener
Prepared by KEERTHI REDDY S A
Madanapalle institute of technolgy and science


Project Overview
The URL Shortener is a Python web application that converts long URLs into shorter, more manageable links. It allows users to enter a long URL, generate a unique short code for it, and store the mapping of the short code to the original URL. When users access the shortened link, they will be redirected to the original long URL.

Introduction
In the vast digital landscape, long URLs can be cumbersome, making them challenging to share or remember. The URL Shortener project addresses this issue by providing a simple and user-friendly solution to create shorter, shareable links.

Objectives
The primary objectives of the URL Shortener project are as follows:

1. Convert Long URLs to Short Codes: The application should take a long URL as input and generate a short code for it.

2. Redirect to Original URLs: When users access the short URL, the application should redirect them to the original long URL.

3. Persistent URL Mapping: The short code and its corresponding long URL should be stored for future access.

Techniques Used
The project leverages the following techniques and technologies:

1. Flask Framework: Flask is used to build the web application and handle HTTP requests.

2. String Manipulation: To generate random short codes for the long URLs.

3. Dictionary Data Structure: To store the mapping of short codes to long URLs.

Project Components
The URL Shortener project consists of the following components:

1. app.py: The main Python file containing the Flask web application and URL shortening logic.

2. templates Folder: Contains HTML templates for rendering web pages.

3. index.html: The home page where users can enter a long URL.

4. short_url.html: The page displaying the generated short URL for the entered long URL.

5. error.html: The page showing an error message if the short URL is not found.

System Architecture
The URL Shortener follows a simple client-server architecture:

1. Client-Side: Users interact with the web application using a web browser.

2. Server-Side: The Flask web application runs on the server and handles user requests.

Project Functionality
The URL Shortener provides the following functionalities:

1. Home Page: The home page allows users to enter a long URL to be shortened.

2. URL Shortening: When users submit a long URL, the application generates a unique short code for it.

3. Short URL Display: The application displays the shortened URL to the user.

4. URL Redirection: When users access the short URL, the application redirects them to the original long URL.

Implementation Details
The URL Shortener project is implemented in Python using the Flask web framework. The Flask application consists of two routes:

1. '/' (Home Page): The route renders the index.html template and handles the form submission to shorten the URL.

2. '/<string:short_code>' (URL Redirection): This route handles the redirection from the short URL to the original long URL.

The URL mapping is stored in a Python dictionary, where the short code is the key, and the long URL is the value. The mapping allows the application to retrieve the original long URL when users access the short URL.

Future Enhancements
The URL Shortener project can be further enhanced with the following features:

1. User Authentication: Implementing user accounts to track shortened URLs for different users.

2. Analytics: Adding analytics to track the number of clicks on each shortened URL.

3. Custom Short Codes: Allowing users to choose their custom short codes for URLs.

Conclusion
The URL Shortener project provides a practical and efficient solution to convert long URLs into short and shareable links. The use of Flask makes the application lightweight and easy to deploy. With possible enhancements, the URL Shortener can cater to a broader user base and offer a seamless experience for URL management.

GitHub Repository

https://github.com/Keerthirddy/Url-shortener/tree/27ae1153b5df8cbfca9dad0afbf7e24f8a04faf2
