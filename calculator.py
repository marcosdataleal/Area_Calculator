class Calculator:
    __wall_area: float
    __ceiling_area: float

    def calculate_wall_area(self, room):
        self.__wall_area = 2 * (room.width + room.depth) * room.height
        return self.__wall_area

    def calculate_ceiling_area(self, room):
        self.__ceiling_area = room.width * room.depth
        return self.__ceiling_area

    def calculate_required_paint(self):
        if self.__wall_area <= 0 or self.__ceiling_area <= 0:
            print('It is not possible to calculate the paint volume with the provided values')
            exit()
        return (self.__wall_area + self.__ceiling_area) / 10