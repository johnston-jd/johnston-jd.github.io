### Jaymie Johnston

## Professional Self-Assessment

### Introduction
Welcome! I started my educational journey at Southern New Hampshire University in October of 2022. I am set to graduate with a Bachelor's degree in Computer Science in Spring of 2025. Over this period I have learned a lot from every course I participated in. I will be using this page to showcase my growth during my time at SNHU. The courses I took included not just coding, but also the software development lifecycle, databases, operating platforms, software testing, and software security. Working through these courses provided me with an understanding of the many different areas of computer science. In our Capstone project we aimed to enhance 1-3 projects from past courses in three areas - Software Engineering & Design, Data Structures & Algorithms, and Databases. For this Capstone, I used the same project for all three enhancements.

### Original Project
The original project that was used for all of the enhancements was from CS-340 Client/Server Development. In this course we used Jupyter Notebooks and MongoDB to create an interactive dashboard that showed animal data from the Austin Animal Center. This dashboard included a datatable with animals that can be sorted and selected, a map that showed the location of a selected animal, and a pie chart displaying the different animal breeds. The project was written in Python coding language and used a simple CRUD to create, read, update, and delete entries into the MongoDB database. The Jupyter Notebook was connected to the MongoDB database. For the enhancements, I continued to use Python language but utilized a different IDE (PyCharm), data structure, and database.
<a href="https://github.com/johnston-jd/johnston-jd.github.io/tree/3af820cb3ee64481ed68ebb4a020169910bbfa77/CS-340%20Originals" Original Project </a>
### Educational Experience
The courses at SNHU were able to create a team enviornment by using weekly discussion posts where we could communicate with out peers. While most projects and assignments were completed individually, there were opportunities for teamwork and collaboration. We were able to take on the roles of an Agile team, such as a product owner, scrum master, developers, and testers. By creating professional documents we learned how to communicate with stakeholders effectively and what is expected in real-world roles. We learned about the different data structures, such as arrays, linked lists, hash tables, and trees, and which algorithms are bested suited for the various data structures. We were introduced to databases and MySQL where we learned how to create and maintain a database using MySQL statements. We also learned the imortance of security with authentication, checksums, and encryption.

## Code Review
Code review of the project selected for the Capstone.

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1077123412?h=d6ec3db3a8&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Code_ Review_ J.Johnston"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>


## Enhancement 1 - Software Engineering & Design
I moved the project from the virtual IDE and Jupyter Notebooks to PyCharm IDE. This allowed all of the files to be contained in one place, keeping everything organized and clean. One aspect that the original project was lacking in was authentication. I used FastAPI and OAuth2 to create a level of security. This included a security key and hashed password. Adding this feature provided more security to the project that was not present before. To enhance the design aspect of the project, I made a lot of small, but important updates. First, I gave the user the ability to select more than one animal in the datatable. I also provided additional filtering options and updated the marker on the map to show the animal ID for easier identification. Originally the pie chart on the dashboard showed all animals from the table - a whopping 10,000 animals - which created a cluttered and unappealing visual. To enhance this, I changed the pie chart to just show the different animal types and also changed the color scheme to match the client's logo at the top of the page. These enhancements show my ability to recognize a need for security as well as anticipate user needs.

![image](https://github.com/user-attachments/assets/49ce20f2-efee-4587-bd97-2496b1e14e3a)
*Screen shot of partial FastAPI code*

![image](https://github.com/user-attachments/assets/2d1d4181-e62a-40a6-8037-399e98c3cae0)
*Screen shot of the dashboard with data table, pie chart, and map*

<a href="https://github.com/johnston-jd/johnston-jd.github.io/tree/ac2d78be9d57f07eac00f1825a29ea0ddfec445b/CS-499%20Enhancements/Enhancement%201%20-%20Software%20Engineering%20%26%20Design" Enhancement 1 Folder </a>
<a href="https://github.com/johnston-jd/johnston-jd.github.io/blob/c343ccfc5e407e92d6a246b7ce37856e09ec8f89/Narratives/CS-499%203-2%20Milestone%20Two%20Enhancement%20One%20Software%20Design%20and%20Engineering%20J.Johnston.docx" Enhancement 1 Narrative</a>


## Enhancement 2 - Data Structures & Algorithms
I implemented a hashmap to enhance the data structure. The database had a lot of records, and creating a hashmap allows for easy and quick access to records. Hashmaps have key-value pairs, which maps keys to their respective values and allows for quick retrevial. The hashmap connects to the MariaDB database that houses the animal shelter dataset. I decided on using a hashmap because of it's ability to store large amounts of data and the dataset I was working with had 10,000 records. It also allows for quick access, which improves the user experience with the interactive dashboard. By implementing a hashmap I am able to showcase my ability to recognize what data structures are appropriate for various projects.

![image](https://github.com/user-attachments/assets/38929ba2-00d8-4a1d-8718-e7968db5ce2a)
*Screen shot of partial hashmap code*

![image](https://github.com/user-attachments/assets/b026b3cb-ba34-451e-aa8b-80b4e9f30e5e)
*Screen shot of partial hashmap code*

<a href="https://github.com/johnston-jd/johnston-jd.github.io/blob/304c33b0a30efa35017d28e3980ac81e6042655c/Narratives/CS-499%204-2%20Milestone%20Three%20Enhancement%20Two%20Algorithms%20and%20Data%20Structure%20J.Johnston.docx" Enhancement 2 Narrative </a>

## Enhancement 3 - Databases
I moved the database from MongoDB to MariaDB/HeidiSQL, utilizing Amazon Web Services. By using Amazon Web Services for the database creation I am adding more security, and improving scalability and performance. I used MariaDB/HeidiSQL for the database and was able to connect the database in PyCharm. I used the original csv file and was able to successfully import it into MariaDB. I also used AWS and MySQL to create another database for FastAPI user authentication. I was able to connect the MySQL database using the username, password, host, port, database name. This enhancement shows my ability to use various database options and transfer datasets without issue.

![image](https://github.com/user-attachments/assets/b5d173af-c711-46b2-8d49-37974173ed41)
*Screen shot of the MariaDB database*

![image](https://github.com/user-attachments/assets/4cc3f856-cbc2-44bc-99c4-19da16857504)
*Screen shot showing PyCharm connected to the MariaDB database*

