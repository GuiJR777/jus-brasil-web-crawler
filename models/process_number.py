class ProcessNumber:
    def __init__(self, number) -> None:
        self.__number = number
        self.__process_id = None
        self.__process_date = None
        self.__judiciary_segment = None
        self.__court_id = None

        self.__handle_number(number)

    def __handle_number(self, number) -> None:
        """
        Processa dados do formato NNNNNNN-DD.AAAA.J.TR.OOOO

        Exemplo:
        INPUT: 0710802-55.2018.8.02.0001

        OUTPUT:
        {
            process_id: 0710802,
            process_date: 55.2018,
            judiciary_segment: 8.02,
            court_id: 0001,
        }
        """
        number_parts = number.split("-")
        self.__process_id = number_parts[0]
        self.__process_date = number_parts[1][:7]
        self.__judiciary_segment = number_parts[1][8:12]
        self.__court_id = number_parts[1][13:]

    @property
    def number(self) -> str:
        return self.__number

    @property
    def process_id(self) -> str:
        return self.__process_id

    @property
    def process_date(self) -> str:
        return self.__process_date

    @property
    def judiciary_segment(self) -> str:
        return self.__judiciary_segment

    @property
    def court_id(self) -> str:
        return self.__court_id
