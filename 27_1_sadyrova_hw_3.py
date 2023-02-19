class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @property
    def memory(self):
        return self.__memory

    def make_computations(self):
        print(self.__memory + self.__cpu)


    def __str__(self):
        return f'CPU: {self.__cpu}, memory: {self.__memory} '

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def __str__(self):
        return f'SIM: {self.__sim_cards_list} '

    def call(self, sim_card_number, call_to_number):
        print(f'Идет звонок на номер {call_to_number} с сим-карты {sim_card_number}')


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f'Локация: {location}')

    def __str__(self):
        return super().__str__() + f' SIM: {self.sim_cards_list}'


computer = Computer(4, 512)
print(computer)
computer.make_computations()


phone = Phone('05553036666')
print(phone)
phone.call('1-Megacom', '0556622988')


smartphone = SmartPhone(3.2, 12, '07014536876')
print(smartphone)
smartphone.use_gps('vostok_5')

print(f'Computer memory is larger than a SmartPhone: {computer > smartphone}')
print(f'Computer is smaller than SmartPhone: {computer < smartphone}')
print(f'The memory of a Computer and a SmartPhone is the same: {computer == smartphone}')
print(f'The memory of the Computer and SmartPhone do not match: {computer != smartphone}')

