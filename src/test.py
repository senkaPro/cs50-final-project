import os, csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

engine = create_engine(os.getenv('DATABASE_URL'))
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open('flight.csv', 'r')
    reader = csv.reader(f)
    for origin,destination,duration in reader:
        db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)",
                    {"origin":origin, "destination": destination, "duration":duration})
    db.commit()

    flights = db.execute("SELECT * FROM flights")

    for flight in flights:
        print(f"{flight.origin}-{flight.destination} : {flight.duration} hours")


if __name__ == "__main__":
    main()