from extensions import db
from sqlalchemy import text
SQL_SCRIPT_1 = "call quick_insert_location(:p1, :p2, 0, 0)"
SQL_SCRIPT_2 = "call InsertNoName()"
SQL_SCRIPT_3 = "call convinient_insert(:p1, :p2)"
SQL_SCRIPT_4 = "call GetRiverStats(:arg)"


class ProcDao:

    def quick_insert_location(self, location_name, region_name):
        result = db.session.execute(
            text(SQL_SCRIPT_1), {
                'p1': location_name,
                'p2': region_name
            })
        return result.mappings().all()

    def random_10(self):
        db.session.execute(text(SQL_SCRIPT_2))
        db.session.commit()

    def convinient_insert(self, river_name, location_name):
        result = db.session.execute(
            text(SQL_SCRIPT_3), {
                'p1': river_name,
                'p2': location_name
            })
        return result.mappings().all()

    def get_stat(self, func):
        result = db.session.execute(text(SQL_SCRIPT_4), {
            'arg': func
        })
        return result.fetchall()
