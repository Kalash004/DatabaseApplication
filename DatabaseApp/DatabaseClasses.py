from SimpleSql import Base, Param, Types, Constraints, Reference


class cities(Base):
    table_name = "cities"
    city_id = Param(Types.INT, Constraints.PK)
    city_name = Param(Types.STRING, Constraints.NOT_NULL, Constraints.UNIQUE)

    def __repr__(self):
        return f"| id: {self.city_id} | name: {self.city_name} |"


class adreses(Base):
    table_name = "adreses"
    adress_id = Param(Types.INT, Constraints.PK)
    address = Param(Types.STRING, Constraints.NOT_NULL)
    f_city_id = Param(Types.INT, Constraints.NOT_NULL, references=Reference(cities, "city_id"))

    def __repr__(self):
        return f"| id: {self.adress_id} | address : {self.address} |"


class houses(Base):
    table_name = "houses"
    house_id = Param(Types.INT, Constraints.PK)
    f_adress_id = Param(Types.INT, Constraints.NOT_NULL, references=Reference(adreses, "adress_id"))
    house_number = Param(Types.STRING, Constraints.NOT_NULL)
    # type with check
    floors = Param(Types.INT, Constraints.NOT_NULL)

    def __repr__(self):
        return f"| id: {self.house_id} | number: {self.house_number} |"


class flats(Base):
    table_name = "flats"
    flat_id = Param(Types.INT, Constraints.PK)
    f_house_id = Param(Types.INT, references=Reference(houses, "house_id"))
    floor = Param(Types.INT, Constraints.NOT_NULL)
    flat_number = Param(Types.STRING, Constraints.NOT_NULL)
    flat_size_m2 = Param(Types.FLOAT, Constraints.NOT_NULL)

    def __repr__(self):
        return f"| id: {self.flat_id} | number: {self.flat_number} | size: {self.flat_size_m2} | floor: {self.floor} |"


class people(Base):
    table_name = "people"
    person_id = Param(Types.INT, Constraints.PK)
    person_name = Param(Types.STRING, Constraints.NOT_NULL)
    person_surename = Param(Types.STRING, Constraints.NOT_NULL)
    unique_identification = Param(Types.STRING, Constraints.NOT_NULL, Constraints.UNIQUE)
    is_male = Param(Types.BOOL, Constraints.NOT_NULL)

    def __repr__(self):
        return (f"| id: {self.person_id} | name: {self.person_name} | surename: {self.person_surename} "
                f"| unique number: {self.unique_identification} | male: {self.is_male}")


class people_in_flats(Base):
    table_name = "people_in_flats"
    person_in_flat_id = Param(Types.INT, Constraints.PK)
    f_person_id = Param(Types.INT, Constraints.NOT_NULL, references=Reference(people, "person_id"))
    f_flat_id = Param(Types.INT, Constraints.NOT_NULL, references=Reference(flats, "flat_id"))
    # added_date datetime ?


class All_tables:
    all_talbes = [cities, adreses, houses, flats, people, people_in_flats]
