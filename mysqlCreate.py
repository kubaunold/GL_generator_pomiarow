import pymysql

print("Executing mysql command…")

hostname = 'localhost'
username = 'root'
password = ''
database = 'snakeydb'
myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
cursor = myConnection.cursor()

#dropDB
drop_measurements_table = "DROP TABLE measurements;"

#createDB
create_measurements_table = "CREATE TABLE measurements (\
                    id INT(11) NOT NULL AUTO_INCREMENT,\
                    sensorId INT(11) NOT NULL,\
                    pm_1_0 INT(11) NOT NULL,\
                    pm_2_5 INT(11) NOT NULL,\
                    pm_10 INT(11) NOT NULL,\
                    temp DOUBLE NOT NULL,\
                    hum DOUBLE NOT NULL,\
                    time DATETIME NOT NULL,\
                    PRIMARY KEY (id))"

cursor.execute(create_measurements_table)
# cursor.execute(drop_measurements_table)

myConnection.commit()
myConnection.close() 