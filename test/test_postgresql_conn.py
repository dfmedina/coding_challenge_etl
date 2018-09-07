import unittest
import psycopg2

# Reference to testing.postgresql database instance
db = None

# Connection to the database used to set the database state before running each
# test
db_con = None

# Map of database connection parameters passed to the functions we're testing
db_conf = None


class TestPostgresqlConn(unittest.TestCase):

        def setUp(self):
            """ Module level set-up called once before any tests in this file are
            executed.  Creates a temporary database and sets it up """
            global db, db_con, db_conf
            db = psycopg2()
            # Get a map of connection parameters for the database which can be passed
            # to the functions being tested so that they connect to the correct
            # database
            db_conf = db.dsn()
            # Create a connection which can be used by our test functions to set and
            # query the state of the database
            db_con = psycopg2.connect(**db_conf)
            # Commit changes immediately to the database
            db_con.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
            with db_con.cursor() as cur:
                # Create the initial database structure (roles, schemas, tables etc.)
                # basically anything that doesn't change
                cur.execute(slurp('./setup.sql'))

        def tearDown(self):
            """ Called after all of the tests in this file have been executed to close
            the database connecton and destroy the temporary database """
            db_con.close()
            db.stop()

        def test_postgresql_conn(self):
            try:
                conn = psycopg2.connect("dbname='mydb' user='myuser' host='my_ip' password='mypassword' connect_timeout=1 ")
                conn.close()
                return True
            except:
                return False
