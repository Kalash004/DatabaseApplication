from SimpleSql import Base, Param, Types, Constraints, Reference


class cities(Base):
    table_name = "cities"
    city_id = Param(Types.INT, Constraints.PK)
    city_name = Param(Types.STRING, Constraints.NOT_NULL)


class adreses(Base):
    table_name = "adreses"
    adress_id = Param(Types.INT, Constraints.PK)
    f_city_id = Param(Types.INT, Constraints.NOT_NULL, references=Reference(cities, "city_id"))


class houses(Base):
    table_name = "houses"
    house_id = Param(Types.INT, Constraints.PK)
    f_adress_id = Param(Types.INT, Constraints.NOT_NULL, references=Reference(adreses, "adress_id"))
    house_number = Param(Types.STRING, Constraints.NOT_NULL)
    floors = Param(Types.INT, Constraints.NOT_NULL)
    # type with check


class flats(Base):
    table_name = "flats"
    flat_id = Param(Types.INT, Constraints.PK)
    f_house_id = Param(Types.INT, references=Reference(houses, "house_id"))
    floor = Param(Types.INT, Constraints.NOT_NULL)
    flat_number = Param(Types.STRING, Constraints.NOT_NULL)
    flat_size_m2 = Param(Types.FLOAT, Constraints.NOT_NULL)


class people(Base):
    table_name = "people"
    person_id = Param(Types.INT, Constraints.PK)
    person_name = Param(Types.STRING, Constraints.NOT_NULL)
    person_surename = Param(Types.STRING, Constraints.NOT_NULL)
    unique_identification = Param(Types.STRING, Constraints.NOT_NULL, Constraints.UNIQUE)
    is_male = Param(Types.BOOL, Constraints.NOT_NULL)


class people_in_flats(Base):
    table_name = "people_in_flats"
    person_in_flat_id = Param(Types.INT, Constraints.PK)
    f_person_id = Param(Types.INT, Constraints.NOT_NULL, references=Reference(people, "person_id"))
    f_flat_id = Param(Types.INT, Constraints.NOT_NULL, references=Reference(flats, "flat_id"))
    # added_date datetime ?


class All_tables:
    all_talbes = [cities, adreses, houses, flats, people, people_in_flats]
