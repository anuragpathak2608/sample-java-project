Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
secret_key = qAx9A2sPJ2Dtr+6XQTfwOU6R93oOu83+A+z0gP+1


Github_key = ghp_0PpFHABiskZ4c5PlQqszQ6jW9tHhTL4NqVFh


Rajorpay = ibrzp_q2ke6J_K0Nn8cY0a9eBFJuME3b


POSTman_key = PMAK-62be77b7574dccssddsc7e9b5a8asdfasdfadsfac50da40973c55f3806b

/
shopizer
Public
Code
Issues
169
Pull requests
159
Discussions
Actions
Projects
Security
2
Insights
shopizer/sm-shop/src/main/resources/profiles/cloud/database.properties
@shopizer-ecommerce
shopizer-ecommerce Fixed api and profiles
Latest commit f0d0305 on 25 Apr
 History
 1 contributor
Executable File  40 lines (32 sloc)  1.2 KB

##
## db config
##

#Need to run these commands before running shopizer - choose your username and password
#mysql>CREATE DATABASE SALESMANAGER;
#mysql>CREATE USER shopizer IDENTIFIED BY 'very-long-shopizer-password';
#mysql>GRANT ALL ON SALESMANAGER.* TO shopizer;
#mysql>FLUSH PRIVILEGES;

#MYSQL
#when connecting to docker compose from outside docker
#db.jdbcUrl=jdbc:mysql://0.0.0.0:3307/SALESMANAGER?autoReconnect=true&serverTimeZone=UTC&useUnicode=true&characterEncoding=UTF-8

#db.jdbcUrl=jdbc:mysql://shopizer-db:3306/SALESMANAGER?autoReconnect=true&serverTimeZone=UTC&useUnicode=true&characterEncoding=UTF-8
#db.user=shopizer_db_user
#db.password=shopizer_db_password
db.driverClass=com.mysql.cj.jdbc.Driver
hibernate.dialect=org.hibernate.dialect.MySQL5InnoDBDialect

#H2
#db.jdbcUrl=jdbc\:h2\:file\:./SALESMANAGER;AUTOCOMMIT=OFF;;mv_store=false;INIT\=CREATE SCHEMA IF NOT EXISTS SALESMANAGER
#db.user=test
#db.password=password
#db.driverClass=org.h2.Driver
#hibernate.dialect=org.hibernate.dialect.H2Dialect

db.show.sql=true
db.preferredTestQuery=SELECT 1
db.schema=SALESMANAGER
hibernate.hbm2ddl.auto=update



##
## configuration pooling base de donn\uFFFDes
##
db.initialPoolSize=8
db.minPoolSize=8
db.maxPoolSize=15
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
You have no unread notifications
