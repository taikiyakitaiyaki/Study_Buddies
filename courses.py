class Courses:
    courses = {
        "BE-110": "Innføring i økonomisk styring",
        "BE-111": "Innføring i finansregnskap",
        "FYS123": "Fysikk",
        "IS-100": "The role of digitalization within society",
        "IS-104": "Digital Interaction Design",
        "IS-110": "Objektorientert programmering",
        "IS-211": "Algorithms and Data Structures",
        "IS-214": "Information Systems Security",
        "IS-217": "Universell utforming av informasjonssystemer",
        "IS-218": "Geografiske Informasjonssystemer, AI og IoT; Introduksjon og Anvendelse",
        "MF-207": "Tjenestemarkedsføring",
        "ORG110": "Organizational Theory for IT Students",
        "ORG209": "Strategisk ledelse",
        "ORG449": "Strategy",
        "SE-204": "Makroøkonomi",
        "SY-120K": "Grunnleggende sykepleie",
        "SY-120G": "Sykdomslære",
        "TFL126": "Etikk, bærekraft og bedrifters samfunnsanvar"
    }

    # Show all courses
    @classmethod
    def show_courses(cls):
        print("\nAvailable courses:")
        for code, name in cls.courses.items():
            print(f"{code}: {name}")

    # Allow user to choose courses from the list
    @classmethod
    def choose_courses(cls):
        cls.show_courses()

        user_input = input("\nWrite course code separated by commas (e.g. IS-110, IS-211):")

        input_list = user_input.upper().strip().replace(" ", "").split(",")

        selected_courses = {}

        for code in input_list:
            if code in cls.courses:
                selected_courses[code] = cls.courses[code]
            else:
                print(f"\nUnknown course code: {code}")
        return selected_courses